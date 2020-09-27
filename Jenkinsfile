// The user jenkins needs to be added to the group docker: sudo usermod -a -G docker jenkins
pipeline {
    agent {
    	docker {
    		image 'python:3.7.3-stretch'
			args '-u root'  // run as user root in the docker container
    	}
    }
    stages {
        stage('verify') {
            steps {
            	echo 'Hello, world!'
            	sh 'pwd'
            	sh 'ls -Rla'
            }
        }
        stage('run') {
            steps {
            	echo 'verify python environment'
				sh 'python --version'
				sh 'pip --version'
				sh 'pip install --trusted-host pypi.python.org -r requirements.txt'
            }
            steps {
            	sh 'python main.py'
            }
        }
    }
}