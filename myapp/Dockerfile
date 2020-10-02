FROM python:3.7.3-stretch

ARG PORT=80

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY *.py requirements.txt .

## Step 3:
# Install packages from requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

## Step 4:
# Expose port 80
EXPOSE $PORT

## Step 5:
# Run app.py at container launch
CMD ["python", "myapp.py"]