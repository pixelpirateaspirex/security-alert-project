FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install flask numpy scikit-learn

CMD ["python", "app.py"]