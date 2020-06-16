pipeline {
  agent {
    node {
      label 'Test'
    }

  }
  stages {
    stage('Git pull') {
      steps {
        git(url: 'https://github.com/helary1211/demo.git', branch: 'master')
      }
    }

    stage('Build') {
      steps {
        bat 'python 2.py'
      }
    }

  }
}