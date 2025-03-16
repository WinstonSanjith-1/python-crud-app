pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "username/python-crud-app:latest"
        K8S_DEPLOYMENT = "k8s-deployment.yaml"
    }
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/username/python-crud-app.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Push Docker Image') {
            steps {
                withDockerRegistry([url: '', credentialsId: 'docker-hub-credentials']) {
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f $K8S_DEPLOYMENT'
            }
        }
    }
}
