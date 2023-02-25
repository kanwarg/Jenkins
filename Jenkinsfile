pipeline {
  agent {
    node {
      label 'ubuntu-agent01'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh ''' ls
 hostname'''
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