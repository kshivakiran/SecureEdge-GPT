# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Create a non-root user for security (Requirement for Hugging Face)
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY --chown=user . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Hugging Face Spaces uses Port 7860
EXPOSE 7860

# Run streamlit when the container launches
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=7860", "--server.address=0.0.0.0"]
