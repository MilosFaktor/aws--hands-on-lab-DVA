# 🚀 Hands-On AWS Project – CI/CD Pipeline with Elastic Beanstalk

As part of my AWS Developer Associate hands-on practice, I created a **CI/CD pipeline** using **AWS CodePipeline** and **Elastic Beanstalk** to deploy a Node.js application automatically whenever code is pushed to a GitHub repository.

---

## 🎯 Goal

Build a fully automated pipeline so that:
- Every push to GitHub triggers the pipeline
- The pipeline deploys the updated code to **Elastic Beanstalk**
- The live **Node.js application** reflects the changes instantly
- Include a **Manual Approval** step before deploying to production

---

## ✅ What I Built

### Elastic Beanstalk Environments

1. Created the main application and staging environment:
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

2. **Source Stage**:
   - GitHub (via GitHub App)
   - Connected repo + branch (`main`)
   - Enabled webhook for automatic triggers

3. **Build & Test Stages**:
   - Skipped (for now)

4. **Deploy to Staging**:
   - Provider: Elastic Beanstalk
   - Deploy Action: `Deploy to First-app-beanstalk-env`
   - Target App: `First-app-beanstalk`

5. **Manual Approval Stage**:
   - Added between staging and production
   - Requires manual confirmation before deploying to production

6. **Deploy to Production**:
   - Provider: Elastic Beanstalk
   - Deploy Action: `Deploy to First-app-beanstalk-prod`
   - Environment: `First-app-beanstalk-prod`

---

## 🧠 Real-World Debugging & Workflow

During the hands-on, the video tutorial used a different UI and codebase than what AWS deployed to my Beanstalk instance.

### Problem:
I wanted to only change a color and a heading in the deployed website — but I couldn't find the deployed files anywhere in GitHub or the AWS Console.

### Solution:
I created a new environment with:
- SSH access (with key pair)
- Connected to the underlying EC2 instance
- Located and copied the actual application files:
  - `index.html`
  - `app.js`
  - `chrome.yaml`
  - `package.json`
  - [`node_modules/`](nodejs-v2-blue)

Then I:
- Created a GitHub repo from these files
- Edited the **hero section color** and the `<h1>` header
- Committed and pushed to GitHub:
  ```bash
  git add .
  git commit -m "Update index.html with new hero section color and header text"
  git push origin main
  ```
✅ Pipeline automatically triggered and deployed to `First-app-beanstalk-env`

✅ After manual approval, the production stage deployed to `First-app-beanstalk-prod`

---

## ⚠️ IAM Permissions Fix

Pipeline deployment initially failed due to **insufficient IAM permissions**.  
✅ I resolved it by attaching the following policies temporarily:

- `AdministratorAccess-AWSElasticBeanstalk`
- `AWSCodePipeline_FullAccess`

> *For production: always follow least-privilege best practices.*

---

## ✅ Outcome

- Full CI/CD pipeline from **GitHub → Staging → Manual Approval → Production**
- Changes deployed safely after confirmation
- Successfully retrieved, edited, and deployed the actual Beanstalk sample app
- The hands-on taught me how to **reverse-engineer a sample app**, fix IAM issues, and configure pipelines with approval flows

---

## 🧼 Cleanup

Don’t forget to:
- Terminate `First-app-beanstalk-env` and `First-app-beanstalk-prod`
- Delete the Beanstalk application
- Delete the CodePipeline

> 💡 To avoid charges from running EC2 instances

---

## 🔗 Related Links

- [Main Hands-On Repo (aws--hands-on-lab-DVA)](https://github.com/MilosFaktor/aws--hands-on-lab-DVA)
- [Screenshots of the Project](Screenshots/)

---

## 🏷️ Tags

`#AWS` `#CodePipeline` `#ElasticBeanstalk` `#CI_CD` `#DeveloperAssociate` `#HandsOnCloud` `#NodeJS` `#GitHub` `#SSH` `#EC2` `#IAM`