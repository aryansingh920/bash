terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      # Pinned to 2.25.0 to support Docker API 1.41
      version = "2.25.0"
    }
  }
}

provider "docker" {
  # This tells Terraform where to find the Docker socket on Mac/Linux/WSL2
  host = "unix:///var/run/docker.sock"
}

# Pull the Ubuntu image
resource "docker_image" "ubuntu" {
  name         = "ubuntu:latest"
  keep_locally = true
}

# Create the container
resource "docker_container" "ansible_target" {
  image = docker_image.ubuntu.latest
  name  = "ansible_playground"
  
  # Keeping it alive so Ansible has time to work
  command = ["tail", "-f", "/dev/null"]
  
  # Ensure the container is removed when terraform destroy is run
  rm = true
}

output "container_name" {
  value = docker_container.ansible_target.name
}
