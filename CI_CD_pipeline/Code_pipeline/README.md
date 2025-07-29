# 🚀 Hands-On AWS Project – CI/CD Pipeline with Elastic Beanstalk

As part of my AWS Developer Associate hands-on practice, I created a **CI/CD pipeline** using **AWS CodePipeline** and **Elastic Beanstalk** to deploy a Node.js application automatically whenever code is pushed to a GitHub repository.

---

## 🎯 Goal

Build a fully automated pipeline so that:
- Every push to GitHub triggers the pipeline
- The pipeline deploys the updated code to **Elastic Beanstalk**
- The live **Node.js application** reflects the changes instantly

---

## ✅ What I Built

### Elastic Beanstalk Environments

1. Created the main application and environment:
   - **Application Name**: `First-app-beanstalk`
   - **Environment Name**: `First-app-beanstalk-env`
   - **Platform**: Node.js 22
   - **Version**: Sample application
   - IAM Role: `aws-elasticbeanstalk-ec2-role` (predefined)

2. Created a second environment for production:
   - **Environment Name**: `First-app-beanstalk-prod`
   - Used the same app version
   - Attached same IAM role
   - Fast-tracked configuration

---

## 🔄 CodePipeline Setup

1. Created pipeline:
   - **Pipeline Name**: `MyFirstPipeline`
   - **Execution Mode**: Queued
   - **Service Role**: Created automatically

2. Source Stage:
   - **GitHub (via GitHub App)**
   - Connected repo + branch (e.g., `main`)
   - Enabled **webhook** for automatic triggers

3. Build & Test:
   - Skipped (for now)

4. Deploy Stage:
   - **Provider**: Elastic Beanstalk
   - **Deploy Action**: `Deploy to First-app-beanstalk-env`
   - **Target App**: `First-app-beanstalk`

---

## 🧠 Real-World Debugging & Workflow

During the hands-on, the **video tutorial** used a different UI and codebase than what AWS deployed to my Beanstalk instance.

### Problem:
I wanted to **only change a color and a heading** in the deployed website — but I couldn't find the deployed files anywhere in GitHub or the AWS Console.

### Solution:
I created a **new environment** with:
- SSH access (with key pair)
- Connected to the underlying **EC2 instance**
- Located and copied the actual application files:
  - `index.html`
  - `app.js`
  - `chrome.yaml`
  - *(and one more file used in the sample app)*

Then I:
- Created a **GitHub repo** from these files  
- Edited the **hero section color** and the `<h1>` header  
- Committed and pushed to GitHub  
- ✅ Pipeline automatically triggered and deployed the updated version to `First-app-beanstalk-env`

---

## ⚠️ IAM Permissions Fix

Pipeline deployment initially failed due to **insufficient IAM permissions**.  
✅ I resolved it by attaching the following policies temporarily:

- `AdministratorAccess-AWSElasticBeanstalk`
- `AWSCodePipeline_FullAccess`

> *For production: always follow least-privilege best practices.*

---

## ✅ Outcome

- Changes pushed to GitHub were deployed to Beanstalk automatically  
- I retrieved and reused the actual deployed files via EC2  
- I modified the frontend safely and validated full pipeline flow  
- The hands-on taught me how to **reverse-engineer a sample app**, connect CodePipeline + GitHub, and fix IAM + deployment issues under pressure

---

## 🧼 Cleanup

Don't forget to:
- Terminate `First-app-beanstalk-env` and `First-app-beanstalk-prod`
- Delete the Beanstalk application
- Delete the CodePipeline

> 💡 To avoid charges from running EC2 instances

---

## 🔗 Related Links

- [Main Hands-On Repo (aws--hands-on-lab-DVA)](https://github.com/MilosFaktor/aws--hands-on-lab-DVA)

---

## 🏷️ Tags

`#AWS` `#CodePipeline` `#ElasticBeanstalk` `#CI_CD` `#DeveloperAssociate` `#HandsOnCloud` `#NodeJS` `#GitHub` `#SSH` `#EC2` `#IAM`