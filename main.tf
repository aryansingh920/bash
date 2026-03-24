terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.25.0" # This version is the sweet spot for Docker Desktop on Mac
    }
  }
}

provider "docker" {
  # Mac uses this path for the Docker socket
  host = "unix:///var/run/docker.sock"
}

resource "docker_image" "ubuntu" {
  name         = "ubuntu:latest"
  keep_locally = true
}

resource "docker_container" "ansible_target" {
  # Changed from .latest to .name for compatibility
  image = docker_image.ubuntu.name 
  name  = "ansible_playground"
  
  command = ["tail", "-f", "/dev/null"]
  rm      = true
}

output "container_name" {
  value = docker_container.ansible_target.name
}
