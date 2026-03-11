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
                // Wait 2 seconds for Nginx to start
                sleep 2
                
                // Test 1: Check if the server returns a 200 OK status
                sh 'curl -s -o /dev/null -w "%{http_code}" http://localhost:3001 | grep 200'
                
                // Test 2: Check if our "Built on" timestamp exists in the HTML
                sh 'curl -s http://localhost:3001 | grep "Built on"'
                
                echo 'Tests passed! Dev environment is healthy.'
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
