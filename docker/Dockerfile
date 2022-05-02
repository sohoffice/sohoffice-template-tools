FROM python:3-slim

RUN mkdir -p /app/vars && mkdir -p /app/src
COPY requirements.txt /app/src
COPY src /app/src

RUN pip install -r /app/src/requirements.txt
WORKDIR /app

# Use CMD to allow caller override
CMD ["python", "/app/src/main.py", "/app/main.tmpl", "/app/vars"]
