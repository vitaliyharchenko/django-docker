FROM tutum/nginx

RUN rm /etc/nginx/sites-enabled/default
ADD sites-enabled/ /etc/nginx/sites-enabled

COPY certs/harchenko_pro.crt /etc/nginx/ssl/harchenko_pro.crt
COPY certs/harchenko_pro.key /etc/nginx/ssl/harchenko_pro.key