FROM python:3.9-slim
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY . /usr/src/app/
WORKDIR /usr/src/app
CMD ["pytest"]