// The user jenkins needs to be added to the group docker: sudo usermod -a -G docker jenkins
@Library('github.com/releaseworks/jenkinslib') _
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
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'aws-key', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY']]) {
					AWS("--region=us-east-2 s3 ls")
				}
            }
        }
    }
}