FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# command to run the FastAPI app:
# CMD ["python3", "app.py"]

EXPOSE 5000

CMD ["python3", "app.py"]
# CMD ["uvicorn", "app.py", "--host", "0.0.0.0", "--port", "8080"]