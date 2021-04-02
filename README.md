# `Jenkins colin_jenkins01`
git config --global user.name "colinsarah"

docker run  -u root -p 8080:8080 --name jenkins -v jenkins-data:/var/jenkins_home  -v /var/run/docker.sock:/var/run/docker.sock -v /home:/home jenkinsci/blueocean
docker run -u root -p 8080:8080  -v jenkins-data:/var/jenkins_home  -v /var/run/docker.sock:/var/run/docker.sock -v "D:/test12":/home jenkinsci/blueocean
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

docker run -u root --name jenkins -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -v /home:/home -v jenkins_home:/var/jenkins_home  jenkins/jenkins

f8ddeead5c4a469b8df0c28f88e532f6

docker run -u root --name jenkins -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock -v $(which docker):/usr/bin/docker -v /home:/home -v jenkins_home:/var/jenkins_home  jenkins

9e55f3521afc48e885b84069bc02f2f5
https://mirrors.tuna.tsinghua.edu.cn/jenkins/plugins/cloudbees-folder/6.9/


https://mirrors.tuna.tsinghua.edu.cn/jenkins/updates/update-center.json

b685a4a2b7ef4400830cd3fa8f2623f1

1.构建>测试
2.打包镜像上传到容器仓库
3.发送指令,(通过docker拉取服务)部署测试环境服务器
a27bf184-51f2-4dfb-86bd-906916c11158