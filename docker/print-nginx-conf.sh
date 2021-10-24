domains="${DOMAINS:-_}"
config_file="

server {
    listen 80;
    server_name $domains;
    server_tokens off;
    client_max_body_size 20M;

    # https://www.digitalocean.com/community/tutorials/how-to-improve-website-performance-using-gzip-and-nginx-on-ubuntu-20-04
    gzip on;
    gzip_disable \"msie6\";

    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_buffers 16 8k;
    gzip_http_version 1.1;
    gzip_min_length 256;
    gzip_types
        application/atom+xml
        application/geo+json
        application/javascript
        application/x-javascript
        application/json
        application/ld+json
        application/manifest+json
        application/rdf+xml
        application/rss+xml
        application/xhtml+xml
        application/xml
        font/eot
        font/otf
        font/ttf
        image/svg+xml
        text/css
        text/javascript
        text/plain
        text/xml;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
        try_files \$uri \$uri/ /index.html;
    }

    location /api {
        try_files \$uri @proxy_api;
    }
    location /admin {
        try_files \$uri @proxy_api;
    }

    location @proxy_api {
        #proxy_set_header X-Forwarded-Proto https;
        #proxy_set_header X-Url-Scheme \$scheme;
        #proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        #proxy_set_header Host \$http_host;
        #proxy_redirect off;
        #proxy_pass   http://backend:8000;
        include uwsgi_params;
        uwsgi_pass unix:///tmp/uwsgi.sock;
    }
}

"

echo "$config_file"
