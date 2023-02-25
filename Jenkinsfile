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
java --version 
echo $JAVA_HOME
cd demo 
 mvn clean
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
mvn test '''
      }
    }

  }
}