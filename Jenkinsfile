pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'python -m pip venv venv'
                //sh 'virtualenv venv && . venv/bin/activate && python -m pip install -r requirements.txt'
                //stash(name: 'compiled-results', includes: 'sources/*.py*')
                echo 'build'
            }
        }
		stage('Test') {
            steps {
                sh 'py.test --junit-xml test-reports/results.xml test_devise_api.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}
