pipeline {
  agent {
    node {
      label 'ubuntu-agent01'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh '''echo hostname
java --version 
$JAVA_HOME
cd demo 

mvn clean
mvn validate 
mvn compile
ls
chmod -R 777 ./target 
./mvnw spring-boot:run'''
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
./mvnw test '''
      }
    }

  }
}