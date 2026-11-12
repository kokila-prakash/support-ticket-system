pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/kokila-prakash/support-ticket-system.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building Support Ticket System...'
                sh 'ls -la'
            }
        }
        stage('Deploy Frontend to S3') {
            steps {
                echo 'Deploying to S3...'
                sh 'aws s3 sync . s3://support-ticket-frontend-s3-kokila --exclude Jenkinsfile --exclude README.md'
            }
        }
    }
    post {
        success {
            echo 'Deployment Successful!'
        }
    }
}
