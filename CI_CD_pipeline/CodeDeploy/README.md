# 🚀 CodeDeploy Hands-On: EC2 Instance Deployment with AppSpec

This hands-on lab demonstrates how to deploy a sample web app to an EC2 instance using **AWS CodeDeploy** with scripts defined in `appspec.yml`. You’ll set up IAM roles, EC2, CodeDeploy configurations, and deploy both initial and updated versions of your app using S3 as your source.

---

## 🔧 Setup Steps

### 1. 🛡️ IAM Roles
- Create a **CodeDeploy role**: Trusted entity = AWS service, use case = CodeDeploy.
- Create an **EC2 role**: Allows the EC2 instance to access S3 (for pulling code artifacts).

### 2. 💻 EC2 Instance
- Launch an EC2 instance (Amazon Linux 2)
- No key pair needed
- Attach the EC2 role
- Security group should allow HTTP (port 80) and SSH (port 22)

### 3. 📦 Install CodeDeploy Agent on EC2
```bash
sudo yum update -y
sudo yum install ruby -y
sudo yum install wget -y
cd /home/ec2-user
wget https://bucket-name.s3.region.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo service codedeploy-agent status
```
### 4. 🏷️ Tag EC2 Instance
- Add tag: Key = Name, Value = development (to match CodeDeploy deployment group)

## 🚀 Initial Deployment (Version 1)
- Create **S3 bucket** and upload ZIP file (sample-app-linux.zip)
- ZIP should include:
  - appspec.yml
  - index.html
  - Scripts: install_dependencies, start_server, stop_server, permissions.sh

### 📂 appspec.yml Example (Version 1)
```yaml
version: 0.0
os: linux
files:
  - source: index.html
    destination: /var/www/html
hooks:
  AfterInstall:
    - location: permissions.sh
      timeout: 300
      runas: root
  ApplicationStart:
    - location: start_server
      timeout: 300
      runas: root
  ApplicationStop:
    - location: stop_server
      timeout: 300
      runas: root
```

## 🛠️ Troubleshooting (Version 1)
- Initial deploy failed: forgot to attach EC2 role
- After fixing IAM role, deployment still failed due to missing permissions
- Restarted agent and monitored logs:
```bash
sudo service codedeploy-agent restart
sudo tail -f /var/log/aws/codedeploy-agent/codedeploy-agent.log
```
- Added a fix: script permissions.sh with:
```bash
sudo chmod -R 755 /var/www/html
sudo chown -R ec2-user:ec2-user /var/www/html
```
- ✅ This fixed permission issues during install.

## 🔁 Update Deployment (Version 2)
Goal: Change color in index.html
- Create a new ZIP (v2) with just:
  - New index.html
  - Shortened appspec.yml (no hooks/scripts)

### 📂 appspec.yml Example (Version 2)
```yaml
version: 0.0
os: linux
files:
  - source: index.html
    destination: /var/www/html
```
- Upload v2 to S3
- Create a new deployment group (or use same if safe)
- Success: index.html color changed!

## 📁 Included Files
- sample-app-linux.zip (v1)
- sample-app-linux-v2.zip (v2)
- appspec.yml (v1 + v2)
- index.html
- Scripts:
    - install_dependencies
    - start_server
    - stop_server
    - permissions.sh

## 🔗 Repo Link
- 📂 This repo:  Contains ZIP files, screenshots, and working YAML/scripts.
- [Screenshots](Screenshots/) – proof of success/failure cases
- Sample App: [SampleApp_Linux](SampleApp_Linux/)
- Sample App v2: [SampleApp_Linux_v2](SampleApp_Linux_v2/)
- 📂 [Main Hands-On Repo (aws--hands-on-lab-DVA)](https://github.com/MilosFaktor/aws--hands-on-lab-DVA)

 

### 🧠 Tags
#AWS #CodeDeploy #EC2 #AppSpec #IAM #S3 #DevOps #Cloud #InfrastructureAsCode #AWSHandsOn #DVA #CICD #Linux #CloudProjects #Deployment