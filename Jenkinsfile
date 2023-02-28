pipeline {
  agent {
    node {
      label 'ubuntu-agent01'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh '''hostname
cd demo 
mvn -B -DskipTests clean package
ls
'''
      }
    }

    stage('test') {
      agent {
        node {
          label 'jenkins-slave-test'
        }

      }
      steps {
        sh '''hostname
cd demo
ls -a
mvn  clean test'''
        junit '**/target/surefire-reports/TEST-*.xml'
      }
    }

  }
}