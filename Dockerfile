# Step 1: Use Python base image
FROM python:3.11-slim

# Step 2: Set working directory
WORKDIR /app

# Step 3: Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy application files (including templates and static folders)
COPY . .

# Step 5: Expose Flask port
EXPOSE 5000

# Step 6: Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Step 7: Run the app using flask instead of python (better for containers)
CMD ["flask", "run"]
