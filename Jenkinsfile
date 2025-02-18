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
                sh '. .venv/bin/activate && pytest --junit-xml test-reports/results.xml test_devise_api.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        stage('Package_Docker') {
            steps {
                //sh 'docker build -t my_rest_api:1 .'
                //with Pipeline docker plugin:
				node{
					app = docker.build("my_rest_api:1")
				}
            }
        }
    }
}
