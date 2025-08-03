# Base Image
FROM python:3.9

# Install the MySQL client dependencies
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y gcc pkg-config default-libmysqlclient-dev

# Set the working directory in the container
WORKDIR /app

# Copy files into the container
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port 5000 (default for Flask)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
