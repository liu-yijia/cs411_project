FROM python:3.6

WORKDIR /code

COPY requirement.txt .

RUN pip install -r requirement.txt

EXPOSE 5000

CMD ["export FLASK_APP=app.py", "flask run"]
