
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Clone the GitHub repository
RUN apt-get update && apt-get install -y git \
    && git clone https://github.com/GRoxo-B/flask-test.git /app

# Change to the docs directory where app.py is located
WORKDIR /app/docs

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port 5000 to allow access
EXPOSE 5000

# Set environment variables to specify the app location and host
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run Flask app
CMD ["flask", "run"]