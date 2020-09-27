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
		    	}
		    }
            steps {
            	echo 'verify python environment'
				sh 'python --version'
				sh 'pip --version'
				withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'pip install --user -r requirements.txt'
					echo 'test running the python code'
					sh 'python main.py'
				}  // https://stackoverflow.com/a/51688905
				echo 'install aws-cli v2'
				sh 'curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip'
				sh 'unzip -q awscliv2.zip'
				sh './aws/install -i ./aws-cli -b ./bin'
				echo 'test aws-cli v2'
				withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
				    sh './bin/aws iam get-user'
				}  // see https://support.cloudbees.com/hc/en-us/articles/360027893492-How-To-Authenticate-to-AWS-with-the-Pipeline-AWS-Plugin
            }
        }
    }
}