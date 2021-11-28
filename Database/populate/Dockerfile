FROM python:3.7-alpine3.14
COPY . /tmp/workspace
WORKDIR /tmp/workspace
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "/tmp/workspace/populate.py"]
