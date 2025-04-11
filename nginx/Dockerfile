# Use the official NGINX image as the base image
FROM nginx:latest

# Install OpenSSL for generating TLS certificates
RUN apt-get update && apt-get install -y openssl && apt-get clean

# Generate a self-signed SSL certificate
RUN mkdir -p /etc/nginx/ssl && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/nginx/ssl/nginx.key \
    -out /etc/nginx/ssl/nginx.crt \
    -subj "/C=US/ST=State/L=City/O=Organization/OU=Department/CN=example.com"

