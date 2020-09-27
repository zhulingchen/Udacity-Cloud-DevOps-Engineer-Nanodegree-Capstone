pipeline {
    agent { docker { image 'python:3.7.3-stretch' } }  // The user jenkins needs to be added to the group docker: sudo usermod -a -G docker jenkins
    stages {
        stage('prepare') {
            steps {
                sh 'python --version'
                sh 'pip --version'
                sh 'pip install --trusted-host pypi.python.org -r requirements.txt'
            }
        }
        stage('verify') {
            steps {
            	echo 'Hello, world!'
            	sh 'pwd'
            	sh 'ls -Rla'
            }
        }
        stage('run') {
            steps {
            	sh 'python main.py'
            }
        }
    }
}