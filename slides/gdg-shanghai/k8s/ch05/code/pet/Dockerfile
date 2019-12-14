FROM python:alpine-3.8
copy ./ /opt/app
RUN pip3 install connexion swagger-ui-bundle flask_cors
ENV PYTHONPATH /opt/app
WORKDIR /opt/app
CMD ["python",  "app"]  