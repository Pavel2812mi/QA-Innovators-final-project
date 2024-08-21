FROM python:3.9-slim
RUN apt-get update && apt-get install -y python3-venv
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
RUN pip install pytest
COPY . /usr/src/app/
WORKDIR /usr/src/app
CMD ["pytest", "--alluredir=allure-results"]