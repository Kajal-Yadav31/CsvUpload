from django.template import loader
import pdfkit
import base64
from io import StringIO, BytesIO
import seaborn as sns
import matplotlib.pyplot as plt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import Upload
import pandas as pd
import matplotlib
matplotlib.use('Agg')

# Create your views here.


def home(request):
    return render(request, 'CsvApp/home.html')


def uploadCsvfile(request):
    """1. Implement a form that allows users to upload CSV files.
Store the uploaded files in sqlite database for processing"""
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save()
            return redirect('analyze', upload.id)
    else:
        form = UploadForm()

    return render(request, 'CsvApp/csvfileupload.html', {'form': form})


def analysingfile(request, upload_id):
    """2. Implement the Data Processing and Data Visualization upon the uploaded data."""
    try:
        upload = Upload.objects.get(id=upload_id)
        csv_file = upload.file
        dataset_name = upload.Dataset_name

        # 2.1 - Read and process the CSV file
        file_data = csv_file.read().decode("utf-8")
        io_string = StringIO(file_data)
        df = pd.read_csv(io_string)

        # 2.2 - Perform Data processing
        head = df.head().to_html()
        sample = df.sample(5).to_html()
        shape = pd.DataFrame([df.shape], columns=["Rows", "Columns"]).to_html()

        description = df.describe(include='all').to_html()
        missing = df.isnull().sum().to_frame(
            name='Missing Values').reset_index().to_html()

        # 2.3 - Check for missing values
        missing_values = df.isnull().sum()
        if missing_values.any():
            # Fill missing values with a placeholder
            filled_df = df.fillna(value="FILL_VALUE")
            filled_data = filled_df.head().to_html()

            # Drop rows with any missing values
            dropped_rows_df = df.dropna()
            dropped_rows_data = dropped_rows_df.head().to_html()

            missing_html = missing_values.to_frame(
                name='Missing Values').reset_index().to_html(index=False)
        else:
            filled_data = dropped_rows_data = "No missing values to handle"
            missing_html = "No missing values in the dataset"

        # 2.4 - Plot histograms for numeric data
        numeric_columns = df.select_dtypes(include=['number']).columns
        if not numeric_columns.empty:
            fig, ax = plt.subplots(len(numeric_columns), figsize=(10, 8))
            df[numeric_columns].hist(ax=ax, bins=30)
            plt.tight_layout()
            buffer = BytesIO()
            fig.savefig(buffer, format='png')
            buffer.seek(0)
            hist_plot = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plt.close(fig)
        else:
            hist_plot = None

        # Create and encode Bar Plot for numeric data
        if not numeric_columns.empty:
            fig, ax = plt.subplots()
            df[numeric_columns].mean().plot(kind='bar', ax=ax)
            buffer = BytesIO()
            fig.savefig(buffer, format='png')
            buffer.seek(0)
            bar_plot = base64.b64encode(buffer.getvalue()).decode('utf-8')
            plt.close(fig)
        else:
            bar_plot = None

        # Prepare data for rendering
        context = {
            "dataset_name": dataset_name,
            "shape": shape,
            "head": head,
            "sample": sample,
            "description": description,
            "missing": missing,
            "filled_data": filled_data,
            "dropped_rows_data": dropped_rows_data,
            "missing_html": missing_html,
            "hist_plot": hist_plot,
            "bar_plot": bar_plot,
        }

        return render(request, "CsvApp/analyze.html", context)

    except Upload.DoesNotExist:
        return HttpResponse("Upload not found", status=404)
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}", status=500)


def dataset_list(request):
    """Fetch all the distinct dataset names."""
    datasets = Upload.objects.all().distinct()
    return render(request, 'CsvApp/dataset_list.html', {'datasets': datasets})
