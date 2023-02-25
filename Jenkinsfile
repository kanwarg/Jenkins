pipeline {
  agent {
    node {
      label 'ubuntu-agent01'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh '''cd demo 
mvnw compile'''
      }
    }

    stage('test') {
      agent {
        node {
          label 'jenkins-slave-test'
        }

      }
      steps {
        sh 'env'
      }
    }

  }
}