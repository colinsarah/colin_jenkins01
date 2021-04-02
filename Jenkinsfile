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
    //    stage('Deliver') { 
    //         agent {
    //             docker {
    //                 image 'cdrx/pyinstaller-linux:python2' 
    //             }
    //         }
    //         steps {
    //             sh 'pyinstaller --onefile sources/add2vals.py' 
    //         }
    //         post {
    //             success {
    //                 archiveArtifacts 'dist/add2vals' 
    //             }
    //         }
    //     }
       stage('Build镜像') {
           steps{
                 sh 'docker build -t colinsarah/jenkins_test01 .'
           }
       }
        // stage('打包成docker镜像发送dockerhub') {
          
        //     steps{
        //           withCredentials([usernamePassword(credentialsId: 'a27bf184-51f2-4dfb-86bd-906916c11158', passwordVariable: 'password', usernameVariable: 'username')]) {
        //             echo '打包成docker镜像发送dockerhub'
        //             sh 'docker login -u ${username} -p${password}&&docker push colinsarah/jenkins_test01'
        //         // some block
        //         }
                
        //     }
            
        // }

        stage('DeployProject') {
            steps{
                echo 'Deploy Project'
            }
        }
       
    }
}

