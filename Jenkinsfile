pipeline {
    agent any

    environment {
        IMAGE_NAME = "your-dockerhub-username/flask-api"
        DOCKER_CREDENTIALS_ID = "docker-hub-credentials" // в Jenkins: Manage Credentials
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Revarine/lesta-stop.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Lint') {
            steps {
                sh 'pip install flake8 && flake8 app'
            }
        }

        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: "$DOCKER_CREDENTIALS_ID", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Deploy') {
            steps {
                sshagent(['remote-server-ssh']) {
                    sh '''
                    ssh -o StrictHostKeyChecking=no user@remote-ip << EOF
                    cd /path/to/deploy/folder
                    git pull
                    docker-compose down
                    docker-compose pull
                    docker-compose up -d
                    EOF
                    '''
                }
            }
        }
    }
}
