pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8-alpine'
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
        }
        stage("Test"){
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                    echo "test success!!!"
                }
            } 
        }
        stage("打包成docker镜像发送dockerhub") {
            agent none
            steps{
                echo "打包成docker镜像发送dockerhub"
            }
        }

        stage("Deploy Project") {
            agent none
            steps{
                echo "Deploy Project"
            }
        }
       
    }
}

