// The user jenkins needs to be added to the group docker: sudo usermod -a -G docker jenkins
pipeline {
	agent {
		label 'jenkins-agent-1'
	}  // add a new agent: https://medium.com/@_oleksii_/how-to-deploy-jenkins-agent-and-connect-it-to-jenkins-master-in-microsoft-azure-ffeb085957c0
    stages {
        stage('verify the build system') {
            steps {
            	sh 'pwd'
            	sh 'ls -la'
            	echo 'verify python environment'
				sh 'python3 --version'
				sh 'pip3 --version'
				withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'printenv'
				}  // see https://stackoverflow.com/a/51688905
            }
        }
        stage('test aws-cli v2') {
        	steps {
				withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
					sh 'aws --version'
				    sh 'aws iam get-user'
				}  // see https://support.cloudbees.com/hc/en-us/articles/360027893492-How-To-Authenticate-to-AWS-with-the-Pipeline-AWS-Plugin
        	}
        }
        stage('lint') {
            steps {
				sh 'cd myapp'
				sh 'pwd'
				sh 'cat Makefile'
				sh 'make env'
				sh 'which pip'
				sh 'make install'
				sh 'make lint'
            }
        }
    }
}