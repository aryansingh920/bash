FROM nginx:alpine
# Copy your current directory into the web server directory
COPY . /usr/share/nginx/html/
# Just a simple index to show it worked
RUN echo "<h1>Local CI/CD Success!</h1><p>Environment: $NODE_ENV</p>" > /usr/share/nginx/html/index.html
