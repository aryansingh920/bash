# This tells the Vault Agent to log in using the Kubernetes Role
auto_auth {
  method "kubernetes" {
    mount_path = "auth/kubernetes"
    config = {
      role = "webapp-role"
    }
  }
}

# This template fetches a secret and writes it to a file the app can read
template {
  contents = <<EOH
    {{ with secret "database/creds/readonly" }}
    DB_USER="{{ .Data.username }}"
    DB_PASSWORD="{{ .Data.password }}"
    {{ end }}
  EOH
  destination = "/etc/secrets/config.env"
}
