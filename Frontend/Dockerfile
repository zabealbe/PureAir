FROM busybox:latest
EXPOSE 80
COPY . /var/www
ENTRYPOINT ["busybox", "httpd", "-f", "-p", "80", "-h", "/var/www"]