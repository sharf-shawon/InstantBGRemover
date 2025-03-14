#!/bin/bash

# Exit immediately if any command fails
set -e

# Activate the virtual environment (if applicable)
# Uncomment and modify the path to your virtual environment if needed
# source /path/to/your/virtualenv/bin/activate

echo "Running Production Post Deployment tasks!"
# Navigate to the Django project directory
cd ./app

# Collect static files (optional)
# Uncomment if you need to collect static files as part of your deploy
# echo "Collecting static files..."
# python manage.py collectstatic --noinput

# Run database migrations
echo "Making database migrations..."
python manage.py  makemigrations --noinput
echo "Running database migrations..."
python manage.py migrate --noinput

# Optionally, you can apply some additional commands here, e.g.,:
# - Clear caches
# - Restart services like Celery or Redis
# - Run custom management commands

echo "Completed Production Post Deployment tasks!"
