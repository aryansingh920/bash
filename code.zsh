#!/bin/zsh

history -n -30 > commands.zsh  


terraform init

terraform apply


docker run -d -p 8080:8080 -p 50000:50000 --name jenkins-local -v jenkins_home:/var/lib/jenkins -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
docker logs jenkins-local
