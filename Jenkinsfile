pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                //sh 'python -m venv venv'
                sh 'python -m venv .venv && . .venv/bin/activate && python -m pip install -r requirements.txt'
                //stash(name: 'compiled-results', includes: 'sources/*.py*')
                echo 'build'
            }
        }
		stage('Test') {
            steps {
                sh '. .venv/bin/activate && py.test --junit-xml test-reports/results.xml test_devise_api.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
