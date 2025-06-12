# Base image
FROM python:3.10.0-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files to container
COPY . .

# Set environment variables (but override with .env at runtime)
ENV PYTHONUNBUFFERED=1

# Expose the default Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "voice.py"]
