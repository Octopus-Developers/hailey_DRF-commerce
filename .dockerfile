FROM python:3

WORKDIR /Users/haileypark/projects/DRF-commerce

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "commerce.wsgi:application"]