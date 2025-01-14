# Simple App Template

A minimal template for deploying an application to AWS using Terraform and Helm.

## Project Structure

The project's structure is designed to be clear and maintainable, enabling efficient development and deployment processes.

```
My Simple App/
├── app/          # Application source code (e.g. Python Flask app) (modify as needed)
│   └── ...
├── deploy/       # Terraform code for infrastructure deployments
│   ├── app/      # Helm deployments for the application
│   ├── infra/    # Terraform resources for infrastructure (Databases, Storage, IAM)
├── .github/      # GitHub Actions workflows (for deployment)
│   └── workflows/ # Folder containing deployment workflows
│       └── ...    # GitHub workflow files to deploy and test
```

## Application

The application, located in the `app/` directory, is a simple Python Flask application that is used purely for demonstration purposes and should be replaced with your application code.

## Infrastructure Deployment

The `deploy/infra/` directory contains Terraform code for deploying the infrastructure.

-   It utilizes reusable modules like `iam-role-for-service-accounts-eks` for creating IAM Roles for EKS service accounts (IRSA) and other modules for managing RDS, Secrets, and other supporting resources.
-   The project uses a single terraform configuration that is shared for all environments.
-   It leverages GitHub Actions to automate deployments to different environments.  The `deploy/app/` directory contains configuration for deploying your application using Helm.

