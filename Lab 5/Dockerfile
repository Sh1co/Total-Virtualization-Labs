FROM python:3.10-slim-buster

RUN adduser --disabled-password app && chown -R app /home/app

WORKDIR /home/app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the main code
COPY --chown=app:app app.py .

CMD [ "python", "app.py", "localhost", "5672", "guest", "guest" ]