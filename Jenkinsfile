pipeline {
    agent { docker { image 'python:3.7.3-stretch' } }  // The user jenkins needs to be added to the group docker: sudo usermod -a -G docker jenkins
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }

        stage('test') {
            steps {
            	echo 'Hello, world!'
            	sh 'pwd'
            	sh 'ls -la'
            }
        }
    }
}