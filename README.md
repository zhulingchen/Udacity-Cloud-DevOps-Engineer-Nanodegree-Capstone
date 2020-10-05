# Udacity Cloud DevOps Engineer Nanodegree Program
# Capstone Project

## Project Overview
In this project, I applied the skills and knowledge which were developed throughout the Cloud DevOps Nanodegree program. These include:

* Working with AWS
* Using Jenkins to implement Continuous Integration and Continuous Deployment
* Building Jenkins pipelines
* Building Docker containers in the pipelines
* Working with eksctl and kubectl to build and deploy Kubernetes clusters

As a capstone project, the directions are rather more open-ended than they were in the previous projects in the program. I developed a CI/CD pipeline for micro services applications with rolling deployment.

## Project Steps

* Create an AWS EC2 instance for Jenkins server and another AWS EC2 instance for a Jenkins agent
    * The Jenkins server itself is the "master" agent for build pipelines, so having another AWS EC2 instance as a Jenkins agent is optional.
    * After installing the Jenkins server, install necessary plugins such as Blue Ocean, Pipeline: AWS Steps, and Docker Pipeline.
    * Add credentials of Jenkins agent(s)' SSH private key(s), AWS, and dockerhub.
    * Do not forget to associate Elastic IP addresses to both two instances.
    * [Add a new Jenkins agent](https://medium.com/@_oleksii_/how-to-deploy-jenkins-agent-and-connect-it-to-jenkins-master-in-microsoft-azure-ffeb085957c0)
    * The Linux user `jenkins` needs to be added to the group `docker`.
        * `sudo usermod -a -G docker jenkins`
    * Install docker, hadolint, aws-cli, eksctl, kubectl, and other necessary system-level utilities in the Jenkins build agent(s).

* Use [Jenkinsfile](./Jenkinsfile) to build a Declarative Pipeline
    * [Validate Jenkinfiles in VSCode](https://llu.is/validate-jenkinfiles-in-vscode/)
    * [Jenkins Pipelines: What I Wish I Knew Starting Out](https://medium.com/garbage-collection/jenkins-pipelines-what-i-wish-i-knew-starting-out-6e3d4eb2ff5b)
        * difference between single and double quoted strings
    * Stages
        * verify the build system
        * verify aws-cli v2, eksctl, kubectl
        * lint
        * build docker image
        * test the docker container
        * push docker image
        * deploy to AWS EKS
        * verify deployment
        * check rollout