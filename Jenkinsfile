pipeline {
  agent {
    node {
      label 'ubuntu-agent01'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh ''' hostname
 cd demo 
 ./mvnw spring0-boot:run'''
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