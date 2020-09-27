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
				echo 'test running the python code'
				sh 'python main.py'
				echo 'install aws-cli v1'
				sh 'pip install awscli'
				echo 'test aws-cli v1'
				withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
				    sh 'aws iam get-user'
				}  // see https://support.cloudbees.com/hc/en-us/articles/360027893492-How-To-Authenticate-to-AWS-with-the-Pipeline-AWS-Plugin
            }
        }
    }
}