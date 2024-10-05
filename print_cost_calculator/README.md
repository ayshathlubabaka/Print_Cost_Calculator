
# Print Cost Calculator

A Django project for calculating print costs.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Creating a Superuser](#creating-a-superuser)

## Requirements

- Python 3.x
- Django 3.x or above
- PostgreSQL (optional, if you decide to use it instead of the default SQLite)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ayshathlubabaka/Print_Cost_Calculator.git
   cd print_cost_calculator
   ```

2. Create a virtual environment:

   ```bash
   python -m venv cenv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     cenv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source cenv/bin/activate
     ```

4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

## Setup

### Create PostgreSQL Database

1. **Install PostgreSQL**: If you haven't already, download and install PostgreSQL from [the official website](https://www.postgresql.org/download/).

2. **Open the PostgreSQL command line** or use a GUI tool like pgAdmin.

3. **Create a new database**:

   ```sql
   CREATE DATABASE print_cost_calculator;
   ```

4. **Create a database user** (if necessary) and grant privileges:

   ```sql
   CREATE USER yourusername WITH PASSWORD 'yourpassword';
   GRANT ALL PRIVILEGES ON DATABASE print_cost_calculator TO yourusername;
   ```

5. **Update your Django `settings.py`** to connect to the PostgreSQL database:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'print_cost_calculator',
           'USER': 'yourusername',
           'PASSWORD': 'yourpassword',
           'HOST': 'localhost',  # Or the address of your database server
           'PORT': '',  # Default is 5432
       }
   }
   ```

### Run Migrations

1. Run migrations to set up the database schema:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. Create a superuser to access the Django admin:

   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to set up the superuser account. For example:
   - Email: admin@example.com
   - Password: admin

3. Follow the prompts to set up your superuser credentials.

## Running the Application

To start the development server, run:

```bash
python manage.py runserver
```

You can now access the application at `http://127.0.0.1:8000/`.