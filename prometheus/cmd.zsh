# First, install the formula
brew install node_exporter

# Then, start it as a background service
brew services start node_exporter


curl http://localhost:9100/metrics


docker run -d --name=prometheus -p 9090:9090 -v $(pwd)/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus


docker run -d --name=grafana -p 3000:3000 grafana/grafana
