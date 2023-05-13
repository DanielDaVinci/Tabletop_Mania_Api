FROM python:3.8.2
ADD . /api
WORKDIR /api

RUN chmod +x ./docker-entrypoint.sh
EXPOSE 8080
CMD ["./docker-entrypoint.sh"]