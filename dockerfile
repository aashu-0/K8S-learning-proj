# 1. Base image
FROM python:3.10-slim

# 2. Environment variables (good practice)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 3. Set working directory
WORKDIR /app

# 4. Install uv
RUN pip install --no-cache-dir uv

# 5. Copy dependency file first (layer caching)
COPY requirements.txt .

# 6. Install dependencies using uv
RUN uv pip install --system --no-cache -r requirements.txt

# 7. Copy application files
COPY app.py .
COPY templates ./templates
COPY static ./static

# 8. Expose port
EXPOSE 8000

# 9. Run FastAPI
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
