FROM python:3-alpine
WORKDIR /worker
COPY requirements.txt hello-responder/
RUN test ! -e hello-responder/requirements.txt || pip install --no-cache-dir -r hello-responder/requirements.txt
COPY . hello-responder/
ENTRYPOINT ["python", "hello-responder/hello.py"]
