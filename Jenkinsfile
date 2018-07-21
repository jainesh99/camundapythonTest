pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        bat 'python -m py_compile complete.py externalTask.py fetchAndLock.py main.py pyautoguiTest.py'
      }
    }
    stage('Create Installer') {
      steps {
        bat 'pyinstaller --onefile -d -y main.py'
      }
    }
    stage('Delivery') {
      steps {
        cifsPublisher(publishers: [[configName: 'windows', transfers: [[cleanRemote: true, excludes: '', flatten: false, makeEmptyDirs: true, noDefaultExcludes: false, patternSeparator: '[,]+', remoteDirectory: '$JOB_NAME', remoteDirectorySDF: false, removePrefix: 'dist', sourceFiles: 'dist/**/**']], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: true]])
      }
    }
    stage('Execute') {
      steps {
        node(label: 'test') {
          bat(script: 'cd C:\\Jenkins\\workspace\\$JOB_NAME', returnStatus: true, returnStdout: true)
          powershell(script: 'main', returnStatus: true, returnStdout: true)
        }

        echo '$JOB_NAME'
      }
    }
  }
}