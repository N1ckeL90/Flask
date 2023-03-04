FROM python:3.8.10-buster

WORKDIR /app

COPY req.txt req.txt
RUN pip install -r req.txt

COPY wsgi.py wsgi.py
COPY blog ./blog

EXPOSE 5000

CMD ["python", "wsgi.py"]