# Use the official Python image as base
FROM python:3.12

# Set the working directory in the container
WORKDIR /Python/api

# Copy the api directory into the container
COPY . .

WORKDIR /Python
# Copy the simple_python directory into the container
COPY simple_python /Python/api/simple_python

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port that Flask runs on
EXPOSE 12345

# Define the command to run the Flask app
CMD ["python3", "api/api.py"]