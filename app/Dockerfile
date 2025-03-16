# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir flask gunicorn

# Copy application files, excluding the Dockerfile
COPY run.py search.py ./
COPY templates/ ./templates/

# Make port 5500 available outside the container
EXPOSE 5500

# Set environment variables
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Run the application with gunicorn as the production server
CMD ["gunicorn", "--bind", "0.0.0.0:5500", "run:app"]