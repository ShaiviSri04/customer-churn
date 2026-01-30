# 1️⃣ Base image (lightweight Python)
FROM python:3.10-slim

# 2️⃣ Set working directory inside container
WORKDIR /app

# 3️⃣ Copy dependency list
COPY requirements.txt .

# 4️⃣ Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copy project files
COPY api/ api/
COPY src/ src/
COPY artifacts/ artifacts/

# 6️⃣ Expose FastAPI port
EXPOSE 8000

# 7️⃣ Start FastAPI server
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
