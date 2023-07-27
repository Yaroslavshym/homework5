FROM python:alpine3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "run_main.py"]
CMD ["pytest", "test_main.py"]
