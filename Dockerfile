FROM python:3.9-slim

WORKDIR /app

COPY ./app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app .
COPY ./logs /logs
# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "main:app","--reload","--host", "0.0.0.0", "--port", "8080", "--log-config", "/logs/log_config.json"]