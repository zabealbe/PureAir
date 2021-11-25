FROM busybox:latest
EXPOSE 18080
COPY . /var/www
ENTRYPOINT ["busybox", "httpd", "-f", "-p", "18080", "-h", "/var/www"]