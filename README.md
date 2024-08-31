# Network_Project
A twitter like social networking app. Only for educational purpose.
\
**Features:**
- New Post
- All Posts
- Profile Page
- Following
- Pagination
- Edit Post
- “Like” and “Unlike”
\
**App link:** https://network-project-5q7j.onrender.com/


## Prerequisites
Docker
Docker Compose
Python 3.11

## Installation
1. Clone the repository

**bash**

`git clone https://github.com/yourusername/network_project.git`

`cd network_project`

2. Create a .venv file

Create a .venv file in the root of your project and add the following environment variables:
`python -m venv .venv`

3. Build and run the Docker containers

Build and run the containers using Docker Compose:

bash

`docker-compose up --build`

This command will:

    Start a PostgreSQL database container using the db_social service.
    Start a Django web application container using the web service.

4. Apply database migrations

Run the following command to apply database migrations:

bash
`docker-compose run web python manage.py makemigrations`
`docker-compose run web python manage.py migrate`

5. Create a superuser

To create an admin user for accessing the Django admin panel, run:

bash

`docker-compose run web python manage.py createsuperuser`

Follow the prompts to set up your admin user credentials.
6. Access the application

Once the containers are running, you can access the application at:

    Web application: http://localhost:8000
    Django Admin: http://localhost:8000/admin

Using Gunicorn

Gunicorn is used as the WSGI HTTP server to serve the Django application. It's configured to run in the web service of the Docker setup with the following command:

bash

`gunicorn project4.wsgi:application --bind 0.0.0.0:8000`

Customizing Gunicorn Settings

If you need to customize Gunicorn settings such as the number of worker processes or timeout settings, you can modify the command in the docker-compose.yml file under the web service.
Running Tests

To run tests, use the following command:

bash

`docker-compose run web python manage.py test`

Stopping the Application

To stop the Docker containers, run:

bash

`docker-compose down`

Requirements

The `requirements.txt` file includes all necessary Python dependencies:


Project Structure

    docker-compose.yml: Configuration for Docker Compose, which defines services for the database and web application.
    Dockerfile: Defines the environment and instructions for building the Django web application container.
    requirements.txt: Lists Python dependencies required for the project.
    project4/wsgi.py: WSGI configuration used by Gunicorn to serve the Django application.

Deployment

For deployment, the application is set up to use Gunicorn as the WSGI server, which is a common choice for running Python web applications in a production environment due to its performance and scalability.