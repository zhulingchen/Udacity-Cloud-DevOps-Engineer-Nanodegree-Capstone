// The user jenkins needs to be added to the group docker: sudo usermod -a -G docker jenkins
pipeline {
	agent none
    stages {
        stage('verify the build system') {
        	agent any
            steps {
            	sh 'pwd'
            	sh 'ls -la'
            }
        }
        stage('prepare python environment') {
		    agent {
		    	docker {
		    		image 'python:3.7.3-stretch'
					args '-u root'  // run as user root in the docker container
		    	}
		    }
            steps {
            	echo 'verify python environment'
				sh 'python --version'
				sh 'pip --version'
				sh 'pip install --trusted-host pypi.python.org -r requirements.txt'
				sh 'python main.py'
            }
        }
        stage('prepare aws-cli environment') {
		    agent {
		    	docker {
		    		image 'amazon/aws-cli'
					args '-u root'  // run as user root in the docker container
		    	}
		    }
            steps {
            	echo 'verify aws-cli environment'
				sh 'aws --version'
            }
        }
    }
}