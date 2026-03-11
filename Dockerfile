FROM nginx:alpine
# Copy your current directory into the web server directory
COPY . /usr/share/nginx/html/
# Just a simple index to show it worked
# RUN echo index.html > /usr/share/nginx/html/index.html
RUN echo "Built on: $(date)" >> /usr/share/nginx/html/index.html
