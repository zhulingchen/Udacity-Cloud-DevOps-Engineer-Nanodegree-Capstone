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
        stage('verify aws-cli v2') {
        	steps {
				withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
					sh 'aws --version'
				    sh 'aws iam get-user'
				}  // see https://support.cloudbees.com/hc/en-us/articles/360027893492-How-To-Authenticate-to-AWS-with-the-Pipeline-AWS-Plugin
        	}
        }
        stage('lint') {
            steps {
            	dir("myapp"){
					//sh 'pwd'
					//sh 'cat Makefile'
					sh """
					python3 -m venv devops
					. devops/bin/activate
					make install
					make lint
					""" // https://stackoverflow.com/a/40937525
            	}  // see https://stackoverflow.com/a/52372748
            }
        }
        stage('build docker image') {
            steps {
            	dir("myapp"){
	            	sh 'docker build --tag=udacity-cloud-devops-capstone .'
            	}
            }
        }
		stage('test the docker container') {
			steps {
				sh 'docker image ls'
				sh 'docker container ls'
				sh 'docker run -d -p 8000:80 udacity-cloud-devops-capstone'
				sh 'sleep 2'
				sh 'curl http://localhost:8000'
				sh 'docker stop $(docker ps -a -q)'
				sh 'docker rm -f $(docker ps -a -q)'
				sh 'docker container ls'
			}
		}
		stage('push docker image') {
			steps {
				withDockerRegistry([credentialsId: "3dc42f63-9520-4e9a-82cf-6bf459307d79", url: ""]) {
					sh 'docker tag udacity-cloud-devops-capstone zhulingchen/udacity-cloud-devops-capstone'
					sh 'docker push zhulingchen/udacity-cloud-devops-capstone'
				}  // see https://www.brightbox.com/blog/2018/01/22/push-builds-to-dockerhub/
				sh 'docker rmi -f $(docker images -q)'
				sh 'docker image ls'
			}
		}
    }
}