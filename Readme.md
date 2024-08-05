# Django CSV uploader

This project is a Django-based web application that allows users to upload datasets, perform data analysis, and visualize the results. The application includes functionalities to handle missing data.

## Features

- **Dataset Upload**: Users can upload datasets in CSV format.
- **Data Analysis**: Perform basic data analysis, including handling missing values.
- **Data Visualization**: Visualize data using Matplotlib and Seaborn.
- **Viewing Datasets**: User can see the uploaded datasets.

## Getting Started

### Clone the Repository

1) First, clone the repository to your local machine:

git clone https://github.com/Kajal-Yadav31/CsvUpload.git


2) cd `CsvUpload`


## Docker Setup

### Running the project

1) To Build and Start the Docker Container :
    `docker-compose up -d`

2) Apply Migrations :
   ` docker-compose exec web python manage.py migrate`

3) Create a Superuser :to access admin panel
    `docker-compose exec web python manage.py createsuperuser`














