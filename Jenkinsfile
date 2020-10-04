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
        stage('verify aws-cli v2, eksctl, kubectl') {
        	steps {
				withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
					sh 'aws --version'
				    sh 'aws iam get-user'
					sh 'eksctl version'
					sh 'kubectl version --short --client'
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
				sh 'sleep 1'
				sh 'curl http://localhost:8000'
				sh 'docker stop $(docker ps -a -q)'
				sh 'docker rm -f $(docker ps -a -q)'
				sh 'docker container ls'
			}
		}
		stage('push docker image') {
			steps {
				withDockerRegistry([credentialsId: "dockerhub", url: ""]) {
					sh 'docker tag udacity-cloud-devops-capstone zhulingchen/udacity-cloud-devops-capstone'
					sh 'docker push zhulingchen/udacity-cloud-devops-capstone'
				}  // see https://devops4solutions.com/publish-docker-image-to-dockerhub-using-jenkins-pipeline/
				sh 'docker rmi -f $(docker images -q)'
				sh 'docker image ls'
				//sh 'docker system prune'
			}
		}
        stage('deploy to AWS EKS') {
        	steps {
				withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
					sh 'aws eks update-kubeconfig --name udacity-cloud-devops-capstone'
					sh 'kubectl config use-context arn:aws:eks:us-east-2:732721007089:cluster/udacity-cloud-devops-capstone'
					sh 'kubectl config current-context'
					//sh 'kubectl delete -f deploy-k8s.yml'  // https://stackoverflow.com/a/41095466
					sh 'kubectl apply -f deploy-k8s.yml'
					sh 'kubectl rollout restart deployments/simple-web-app'
					sh 'sleep 90'
					sh 'kubectl get nodes'
					sh 'kubectl get deployments'
					sh 'kubectl get pod -o wide'
					sh 'kubectl get service/simple-web-app'
				}
        	}
        }
		stage('verify deployment') {
			steps {
				withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
					script {
						def EKS_HOSTNAME = sh(
							script: 'kubectl get svc simple-web-app -o jsonpath="{.status.loadBalancer.ingress[*].hostname}"',
							returnStdout: true
							).trim()
						sh "curl ${EKS_HOSTNAME}:8080"  // see https://stackoverflow.com/a/40078286
					}
				}
			}
		}
        stage('check rollout') {
        	steps {
				withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
					sh 'kubectl rollout status deployments/simple-web-app'
				}
        	}
        }
		//stage('stop the running pods') {
		//	steps {
		//		withAWS(credentials: 'aws-credentials', region: 'us-east-2') {
		//			sh "kubectl delete -f deploy-k8s.yml"
		//		}
		//	}
		//}
    }
}