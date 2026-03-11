pipeline {
    agent any
    stages {
        stage('Unit Test') {
            steps {
                echo 'Testing Bash scripts and Terraform files...'
                sh 'ls -R' // Just to prove Jenkins can see your files
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
