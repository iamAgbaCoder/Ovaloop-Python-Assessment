#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Print commands to the terminal.
set -x

# Navigate to the directory containing manage.py
cd SalesAPI/  # Replace with the actual path to your SalesAPI project

# Install the required packages.
pip install -r requirements.txt

# Collect static files without user input.
python manage.py collectstatic --noinput

# Run migrations.
python manage.py migrate

# Create superuser
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@mail.com', 'password')" | python manage.py shell

# Optional: You can start the server or run tests here if needed.
# Uncomment the following line if you want to run the server.
# python manage.py runserver
