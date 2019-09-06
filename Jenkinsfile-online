pipeline {
  agent {
    node {
      label 'base'
    }
  }
  environment {
    DOCKER_CREDENTIAL_ID = 'dockerhub'
    KUBECONFIG_CREDENTIAL_ID = 'kubeconfig'
    REGISTRY = 'docker.io'
    DOCKERHUB_NAMESPACE = 'shaowenchen'
    APP_NAME = 'devops-python-sample'
    SONAR_CREDENTIAL_ID = 'sonar-token'
  }
  parameters {
    string(name: 'BRANCH_NAME', defaultValue: 'master', description: '')
  }

  stages {
    stage('拉取代码') {
      steps {
        container('base') {
          checkout([$class: 'GitSCM', branches: [[name: '*/$BRANCH_NAME']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/shaowenchen/devops-python-sample.git']]])
        }
        /* if in scm, you can use: checkout scm  */
      }
    }

    stage('代码检查') {
      steps {
        container('base') {
          withCredentials([string(credentialsId : "$SONAR_CREDENTIAL_ID" ,variable : 'SONAR_TOKEN' ,)]) {
            withSonarQubeEnv('sonar') {
              sh '''pip install pkgs/base/* & pip install pkgs/extra/*
  coverage erase
  cd ./src/
  coverage run --source='.' manage.py test
  coverage xml -i
  '''
              sh "sonar-scanner -Dsonar.branch=$BRANCH_NAME -Dsonar.login=$SONAR_TOKEN"
            }

          }

        }

      }
    }

    stage('推送镜像') {
      steps {
        container('base') {
          withCredentials([usernamePassword(credentialsId : "$DOCKER_CREDENTIAL_ID" ,passwordVariable : 'DOCKER_PASSWORD' ,usernameVariable : 'DOCKER_USERNAME' ,)]) {
            sh 'echo "$DOCKER_PASSWORD" | docker login $REGISTRY -u "$DOCKER_USERNAME" --password-stdin'
            sh 'docker build -f Dockerfile-online -t $REGISTRY/$DOCKERHUB_NAMESPACE/$APP_NAME:$BUILD_NUMBER .'
            sh 'docker push $REGISTRY/$DOCKERHUB_NAMESPACE/$APP_NAME:$BUILD_NUMBER'
          }

        }

      }
    }

    stage('部署') {
      steps {
        kubernetesDeploy(enableConfigSubstitution: true, kubeconfigId: "$KUBECONFIG_CREDENTIAL_ID", configs: 'deploy/**')
      }
    }
  
  }
}
