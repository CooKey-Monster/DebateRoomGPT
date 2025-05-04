# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app/DebateGPT

# Copy your project files
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Run migrations and start server 
CMD ["daphne", "DebateGPT.asgi:application", "--bind", "0.0.0.0", "--port", "8000"]

