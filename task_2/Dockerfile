# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 9200 (Elasticsearch) available to the world outside the container
EXPOSE 9200

# Run your app when the container launches
CMD ["python", "your_app.py"]
