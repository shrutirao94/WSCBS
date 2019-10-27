FROM python:3.7-stretch

COPY . /app

WORKDIR /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

ENV LC_AL C.UTF-8
ENV LANG C.UTF-8
ENV http_proxy host:port
ENV https_proxy host:port
ENV FLASK_APP url_shortner
ENV FLASK_ENVIRONMENT development

RUN flask init-db

ENV NAME urlshortner

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000" ]


