# Base Image

FROM python:3.11-slim

# Set Working Directory

WORKDIR /app

# Copy Files

COPY . .

# Install Dependencies

RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit Port

EXPOSE 7860

# Run Streamlit Application

CMD ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]