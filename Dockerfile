FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src ./src
COPY data ./data
EXPOSE 8000
CMD ["uvicorn", "src.backend:app", "--host", "0.0.0.0", "--port", "8000"]
