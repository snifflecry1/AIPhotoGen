FROM python:3.13.3-slim-bookworm as base 

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

FROM base as dev

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM base as prod 

RUN pip install --prefix=/install --no-cache-dir -r requirements.txt

FROM python:3.13.3-slim-bookworm

ENV PATH="/usr/local/lib/python3.13/site-packages/bin:/usr/local/bin:$PATH"

WORKDIR /app

COPY --from=prod /install/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=prod /install/bin /usr/local/bin

COPY . /app/

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]







