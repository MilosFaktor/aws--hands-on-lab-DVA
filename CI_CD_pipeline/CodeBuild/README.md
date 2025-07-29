# 🚀 Hands-On AWS Project – CodeBuild Validation in CI/CD Pipeline

As part of my AWS Developer Associate hands-on learning, I extended an existing **CI/CD pipeline** to include an automated **validation stage using AWS CodeBuild**. The goal was to verify that a specific success phrase was present in the website's content before allowing deployment to Elastic Beanstalk.

---

## 🎯 Goal

- Integrate **CodeBuild** into an existing CodePipeline  
- Ensure that **only approved content** (based on validation) is deployed  
- Use a **buildspec.yml** to check for a success phrase in `index.html`

---

## ✅ What I Built

1. **Initial Setup**:
   - Created a **CodeBuild project**
   - Connected it to the same **GitHub repository** as my pipeline
   - Set filter: trigger only on **`push`**
   - Created a **default IAM role** for CodeBuild

2. **Validation Logic**:
   - Wrote a `buildspec.yml` that checks if `index.html` contains:  
     `"Successfully deployed to Elastic Beanstalk"`
   - Placed the `buildspec.yml` in the root of the repo

---

## 🔄 First Test

- Ran CodeBuild → ❌ **Failed**  
  - Reason: `buildspec.yml` was missing  
- Added `buildspec.yml`, committed, and pushed  
- ✅ CodeBuild was triggered → **Success**  
  - Validation passed — phrase was found

---

## 🔗 CodePipeline Integration

- Edited the existing **CI/CD pipeline**  
- Removed CodeBuild’s own webhook trigger  
- Added **CodeBuild as a new stage** in the pipeline:  
  - **After** the GitHub source stage  
  - **Before** deploy-to-environment stage  
  - Named it: `code-build-test`
- Selected the existing CodeBuild project

---

## ⚠️ IAM Permissions Issue

- Pipeline failed to trigger CodeBuild  
- ✅ Solved by attaching `AWSCodeBuildDeveloperAccess` policy to the pipeline role *(temporary loose permission for testing)*

---

## 🧪 Negative Test (Expected Failure)

- Changed `index.html` to:
  `"Unsuccessfully deployed to Elastic Beanstalk"`
- Committed and pushed  
- ✅ Pipeline triggered  
- ❌ CodeBuild **failed** — phrase mismatch  
- ✅ Code was **not deployed** to any environment

---

## 🧪 Positive Test (Expected Success)

- Reverted `index.html` to the correct phrase:
  `"Successfully deployed to Elastic Beanstalk"`
- Pushed to GitHub  
- ✅ Pipeline triggered  
- ✅ CodeBuild passed  
- ✅ Manually approved  
- ✅ Changes deployed to the Elastic Beanstalk environment  
- Final page displayed the correct updated content

---

## ✅ Outcome

- Verified that **CodeBuild can block bad deployments** via simple checks  
- Successfully integrated CodeBuild into a multi-stage CI/CD flow  
- Practiced pipeline editing, IAM permissions, and buildspec scripting  
- Full automation from GitHub push → validation → approval → deployment

---

## 📁 Files Included

- [buildspec.yml](nodejs-v2-blue/buildspec.yml) – validation logic  
- [index.html](nodejs-v2-blue/index.html) – tested content file  
- [Screenshots/](Screenshots/) – proof of success/failure cases

---

## 🔗 Related Links

- [Main Developer Associate Repo (aws--hands-on-lab-DVA)](https://github.com/MilosFaktor/aws--hands-on-lab-DVA)

---

## 🏷️ Tags

`#AWS` `#CodePipeline` `#CodeBuild` `#CI_CD` `#ElasticBeanstalk` `#DeveloperAssociate` `#HandsOnCloud` `#IAM` `#Automation` `#buildspec`
