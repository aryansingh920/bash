pipeline {
    agent any
    stages {
        stage('Unit Test') {
            steps {
                echo 'Validating Terraform syntax...'
                // If you have terraform installed in the Jenkins container:
                // sh 'terraform validate'
                
                echo 'Checking Bash scripts...'
                // This finds all .sh files and checks for basic syntax
                sh 'find . -name "*.sh" -exec bash -n {} +' 
                
                sh 'ls -R'
            }
        }
        stage('Build Container') {
            steps {
                // Build the image using the Dockerfile in this folder
                sh 'docker build -t local-practice-app:latest .'
            }
        }
        stage('Deploy to Dev') {
            steps {
                // Remove old dev container if it exists, then run new one on port 3001
                sh 'docker rm -f dev-env || true'
                sh 'docker run -d --name dev-env -p 3001:80 local-practice-app:latest'
                echo 'Dev is running at http://localhost:3001'
            }
        }
        stage('Integration Test') {
            steps {
                echo 'Verifying Dev Server is reachable...'
                sleep 5 // Give Nginx a bit more time
                
                // Use host.docker.internal to route out of the container back to your Mac's ports
                sh 'curl -s -o /dev/null -w "%{http_code}" http://host.docker.internal:3001 | grep 200'
            }
        }
        stage('Wait for Approval') {
            steps {
                // This is your "When I say publish" requirement
                input message: 'Dev looks good? Deploy to Production?'
            }
        }
        stage('Deploy to Prod') {
            steps {
                // Run on port 80 (standard prod port)
                sh 'docker rm -f prod-env || true'
                sh 'docker run -d --name prod-env -p 80:80 local-practice-app:latest'
                echo 'Prod is running at http://localhost'
            }
        }
    }
}
