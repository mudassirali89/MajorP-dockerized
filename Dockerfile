# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install system dependencies required for mysqlclient
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && apt-get clean

# Copy the project files
COPY . /app

# Install Python dependencies
RUN pip install  -r predicting_at_risk_students/requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Run the Django development server
CMD ["python", "predicting_at_risk_students/manage.py", "runserver", "0.0.0.0:8000"]
