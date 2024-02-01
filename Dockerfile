# Use an official Python runtime as a parent image
FROM python:3.10

# Declare GITHUB_PAT as an argument
ARG GITHUB_PAT

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    GITHUB_PAT=${GITHUB_PAT}

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Copy project requirements file
COPY ./requirements.txt /app/requirements.txt

# Install project dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the private dependencies installation script
COPY ./install_private_dependencies.sh /app/install_private_dependencies.sh

# Make the script executable
RUN chmod +x /app/install_private_dependencies.sh

RUN ./install_private_dependencies.sh

# Copy the current directory contents into the container at /app
COPY . /app/

# Uvicorn will listen on this port
EXPOSE 5000

# Install private dependencies and run uvicorn server
CMD uvicorn main:app --host 0.0.0.0 --port 5000
