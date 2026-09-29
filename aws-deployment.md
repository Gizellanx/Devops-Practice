# AWS Deployment

This document will track the deployment of the Project Log Monitor application to AWS.

## Deployment Plan

1. Create an AWS EC2 instance
2. Configure the instance for Docker
3. Deploy the Project Log Monitor container
4. Verify the application runs successfully
5. Connect the deployment to GitHub Actions
6. Automate future deployments

## Current Status

- Docker containerisation: Complete
- GitHub Actions CI: Complete
- AWS EC2 instance: Complete
- Docker configured on EC2: Complete
- GitHub repository cloned to EC2 using SSH: Complete
- Docker image built successfully on EC2: Complete
- Container verification: In progress
- Continuous deployment (CD): Planned
- Terraform infrastructure: Planned

## What I Practiced

This deployment gave me hands-on experience moving my project from GitHub onto an AWS EC2 Linux server.

I configured the EC2 instance, connected to it using SSH, installed Git and Docker, authenticated the server with GitHub using SSH keys, cloned my repository, and built the Docker image directly on the EC2 instance.

During the first container test, I encountered a JSON configuration error. I used Linux commands and Python's JSON validation tools to investigate the issue. The container verification is still in progress.

This was my first hands-on deployment of my own containerised application to AWS.

## Key Technologies

- AWS EC2
- Amazon Linux
- Linux
- SSH
- Git and GitHub
- Docker
- GitHub Actions
- Python
- JSON
