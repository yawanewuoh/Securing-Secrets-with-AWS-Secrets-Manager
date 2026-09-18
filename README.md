# Secure Secrets with Secrets Manager

**Project Link:** [View Project](https://nextwork.ai/positive_beige_noble_river_dolphin/docs/aws-security-secretsmanager)

---

![Image](http://nextwork.ai/positive_beige_noble_river_dolphin/uploads/aws-security-secretsmanager_r7s8t9u0)

---
In this project, I secured hardcoded credentials using AWS Secrets Manager.

AWS Secrets Manager is a fully managed cloud service that helps you securely store, manage, and retrieve sensitive information like database credentials, API keys, OAuth tokens, and passwords. 

### Tools and concepts

Services I used were AWS Secrets Manager and AWS IAM. 

Key concepts I learnt include Version control (Git) and Github.

### Project reflection

The most challenging part where I needed to remove the AWS credentials that got tracked in the git commit history.

The most rewarding part was the experience I gained from doing this project. 

I chose to do this project because I wanted to learn how to handle credential and secret leakage incidents in the real world.

---

## Hardcoding credentials

It is unsafe to harcode credentials because it poses a major security risk and is extremely unsafe for production applications. Once someone else gets access to your credentials, they can use them to access your AWS account, delete resources, steal data, and cause damage.

For a realistic scenario, I cloned a repository on GitHub that had empty credentials exposed in config.py. 

The repo owner intentionally made it vulnerable for security practice.

I placed random AWS credentials in there to simulate a real-world incident.

![Image](http://nextwork.ai/positive_beige_noble_river_dolphin/uploads/aws-security-secretsmanager_j2k3l4m5)

---

## Using my own AWS credentials

---

## Pushing Insecure Code to GitHub

Once I updated the web app code with credentials, I forked the repository because I wanted the original copy of the web app.

To connect my local repository to the forked repository, I added the remote url to my git. Then I used git add and git commit to keep track the files. Finally, git push uploads the code to github.

I was surprised GitHub allowed my files including the config.py that contains the AWS credentials.

However, I got an email from them alerting me of an incident.

![Image](http://nextwork.ai/positive_beige_noble_river_dolphin/uploads/aws-security-secretsmanager_o2p3q4r5)

---

## Secrets Manager

Secrets Manager is a service that helps you securely store and manage secrets, such as database credentials, API keys, and other sensitive information.  

I used it to store my AWS credentials. Other common use cases include:

1. Centralized management: Manage all your secrets in one place.

2. Rotation: Automate secret rotation to improve security posture.

3. Auditing: Track access to secrets for compliance and security monitoring.

Another feature in Secrets Manager is secret rotation which means automatic rotation of secrets. It's useful in situations where high-risk credentials like database passwords, privileged API keys, and service account credentials need to be highly secured. 

When access credentials are regularly rotated, hackers getting access to them wouldn't cause much harm.

Secrets Manager provides sample code in various languages, like Python, Java and Go. This is helpful because it helps developers integrate them in their code for fast retrieval of stored credentials.

![Image](http://nextwork.ai/positive_beige_noble_river_dolphin/uploads/aws-security-secretsmanager_h2i3j4k5)

---

## Updating the web app code

I updated the config.py file to retrieve the stored AWS credentials using sample code from Secrets Manager. The get_secret() function is the main function that fetches the credentials. 

I also added code to config.py to extract the credentials served from Secrets Manager. This is important because I want to allocate each credential respectively.

![Image](http://nextwork.ai/positive_beige_noble_river_dolphin/uploads/aws-security-secretsmanager_v0w1x2y3)

---

## Rebasing the repository

Git rebasing is the process of moving or combining a sequence of commits to a new base commit. 

I used it to remove AWS credentials that were left in my Git history. The goal was to keep a fresh commit history on top of the new code in the main branch.

I resolved the merge conflicts by repeatedly deleting the sensitive file with git rm config.py, continuing the rebase until all steps were processed, and finally skipping a redundant empty commit.

Once the merge conflict was resolved, I verified that the config.py, containing AWS secrets manager sample code, is uploaded on Github.

![Image](http://nextwork.ai/positive_beige_noble_river_dolphin/uploads/aws-security-secretsmanager_t5u6v7w8)

---

---
