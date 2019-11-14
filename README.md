# devops-python-sample

## 项目简介

这是一个在 Kubesphere 上使用 DevOps 发布 Python 应用的一个 Demo 。

[KubeSphere](https://kubesphere.io) 是在目前主流容器调度平台 Kubernetes 之上构建的企业级分布式多租户容器管理平台。

## 环境依赖

- Kubesphere 平台
- Github 账户
- DockerHub 账户

## 部署步骤

1. 在 Kubesphere 平台，创建命名为 django-proj 的工程。

在 Kubesphere 中，项目对应 namespace 。如果不使用 django-proj 命名空间，则需要修改 Jenkinsfile 文件，保持一致。

2. 在 sonarqube 平台创建命名为 django 的工程。

key 设置为 django，获取 token 值。

3. 创建 DockerHub 、Kubeconfig 、sonar-token 凭证。

建议将 Dockerhub 凭证命名为 dockerhub ，将 Kubeconfig 凭证命名为 kubeconfig ，将 sonarqube 凭证命名为 sonar-token。如果使用其他命名，则需要修改 Jenkinsfile 文件中相关变量，保持一致。

4. 修改基本信息

将 Jenkinsfile 中 DOCKERHUB_NAMESPACE 和拉取代码的 URL 修改为合适的值

5. 创建一个 DevOps 工程。

选择使用图形化构建，点击 【编辑 Jenkinsfile】，将项目下的 Jenkinsfile 文件粘贴保存，点击运行即可。

6. 在 django-proj 项目中，找到 django-demo 服务，可以查看到相关的访问 NodePort 端口。

通过集群外部访问 IP + NodePort 端口，就可以访问到 Django 提供的页面。
