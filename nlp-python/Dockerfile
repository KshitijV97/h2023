# Base image
FROM python:3.7.9-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

RUN apk add build-base linux-headers
RUN python -m pip install psutil

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Set the environment variable for ADC
ENV GOOGLE_APPLICATION_CREDENTIALS /app/application_default_credentials.json

# Expose the port that the Flask application is listening on
EXPOSE 8080

# Set the entrypoint command to run the Flask application
CMD ["python3", "main.py"]
