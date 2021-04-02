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
        stage('Test'){
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
        stage('Delivery') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python3'
                }
            }
            steps {
              sh 'pyinstaller -F sources/add2vals.py'  
            }
            post {
                success {
                    archiveArtifacts  'dist/add2vals'
                }
            }
        }
        stage('打包成docker镜像发送dockerhub') {
            steps{
                echo '打包成docker镜像发送dockerhub'
            }
        }

        stage('DeployProject') {
            steps{
                echo 'Deploy Project'
            }
        }
       
    }
}

