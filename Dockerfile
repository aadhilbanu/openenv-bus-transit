FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn pydantic

CMD ["uvicorn", "inference:app", "--host", "0.0.0.0", "--port", "7860"]
