FROM python:3.7

ENV PYTHONUNBUFFERED 1
RUN groupadd -r flask && useradd -r -g flask flask
COPY --chown=flask . /app
RUN pip install --upgrade pip  \
    && pip install -r /app/api/requirements.txt
WORKDIR /app
