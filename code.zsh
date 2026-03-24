#!/bin/zsh

history -n -30 > commands.zsh  


terraform init
terraform plan
terraform fmt
terraform apply


docker run -d -p 8080:8080 -p 50000:50000 --name jenkins-local -v jenkins_home:/var/lib/jenkins -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
docker logs jenkins-local
docker exec -u 0 -it jenkins-local bash
docker exec -u 0 -it jenkins-local chmod 666 /var/run/docker.sock

