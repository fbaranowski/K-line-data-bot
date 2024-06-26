FROM python:3.12-alpine
WORKDIR /app
COPY Pipfile Pipfile.lock ./
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir pipenv && pipenv install --dev --system --deploy
COPY main.py .env ./
CMD ["python", "main.py"]
