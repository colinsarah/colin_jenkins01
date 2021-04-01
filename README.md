# `Jenkins colin_jenkins01`
git config --global user.name "colinsarah"

docker run  -p 8080:8080  -v jenkins-data:/var/jenkins_home  -v /var/run/docker.sock:/var/run/docker.sock -v "%HOMEPATH%":/home jenkinsci/blueocean
docker run -u root -p 8080:8080  -v jenkins-data:/var/jenkins_home  -v /var/run/docker.sock:/var/run/docker.sock -v "D:/test12":/home jenkinsci/blueocean