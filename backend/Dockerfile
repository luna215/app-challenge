FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /backend

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc libc-dev libpq-dev tesseract-ocr poppler-utils \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /backend
COPY ./requirements.txt /backend/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /backend
COPY . /backend/

# Set the port to expose
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]