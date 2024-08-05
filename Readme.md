# Django CSV uploader

This project is a Django-based web application that allows users to upload datasets, perform data analysis, and visualize the results. The application includes functionalities to handle missing data.

## Demo

### Project Demo video:

https://github.com/user-attachments/assets/8c9c9463-b684-4d1c-bd29-147558bb3dcc


### ScreenShots of project:

![Screenshot 2024-08-05 191929](https://github.com/user-attachments/assets/1959369d-2e87-4d26-91f4-ce8136863e19)

![Screenshot 2024-08-05 192517](https://github.com/user-attachments/assets/7a110ffa-f41e-4be8-86e3-eff573132f2e)

![data](https://github.com/user-attachments/assets/5db44e6f-55a7-4f07-ad7e-27e4e2d80dec)

![Screenshot 2024-08-05 193816](https://github.com/user-attachments/assets/e3eca64d-dc83-4572-b339-78f582ad7494)


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














