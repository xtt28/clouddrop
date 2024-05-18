# CloudDrop

A file uploading and sharing web application.

## Features

- Upload files and view them in your personal dashboard
- Control access to your individual files
- Share and access files with one link

## Development

### Setting up

```shell
# Clone the repository with Git
git clone https://github.com/xtt28/clouddrop.git

# Switch to the repository directory
cd clouddrop

# Create a virtual environment
python3 -m venv .venv

# Use the virtual environment
source .venv/bin/activate

# Install the dependencies
pip install -r requirements.txt
```

### Usage

```shell
# Switch to the Django project directory
# (you will have run `cd clouddrop` twice)
cd clouddrop

# Set up your database
./manage.py migrate

# Run the development server
./manage.py runserver
```

#### How do I deploy a Django project?

Follow the Django [deployment checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
and run `manage.py check --deploy` to prepare your instance of the software for
deployment.

## Tech Stack

### Frontend

- UIKit

### Backend

- Django
- SQLite (by default)