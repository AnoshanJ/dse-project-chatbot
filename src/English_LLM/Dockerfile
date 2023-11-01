# Use the official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install required Python packages
RUN pip install -r requirements.txt 

# Copy all files from the current directory to the container
COPY . .

# Expose the port that the application runs on
EXPOSE 8000

# Define the command to run the application
CMD ["uvicorn", "model:app", "--host", "0.0.0.0", "--port", "8000"]