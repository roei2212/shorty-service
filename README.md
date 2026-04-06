🚀 Features

Shorten long URLs into compact identifiers

Redirect users to the original URL

Auto‑generated API documentation via Swagger

Dockerized application

CI pipeline for linting, testing, building, and pushing images

CD pipeline for validating Kubernetes manifests

Separate Kubernetes configs for staging and production



🧱 Project Structure

shorty-service/
│
├── app/                    # FastAPI application code
│
├── k8s/
│   ├── staging/            # Staging Kubernetes manifests
│   └── production/         # Production Kubernetes manifests
│
├── .github/workflows/      # CI/CD pipelines
│   ├── ci.yml
│   └── cd.yml
│
├── Dockerfile
├── requirements.txt
└── README.md



🐳 Docker
Build the image
bash
docker build -t shorty-service .
Run the container
bash
docker run -p 8000:8000 shorty-service
Access the API


http://localhost:8000/docs

🏗 CI Pipeline (GitHub Actions)
The CI workflow runs on every push to main or develop and performs:

Linting with flake8

Unit tests with pytest

Docker image build

Authentication to GHCR

Pushing the image with the commit SHA as the tag

Images are stored at:


ghcr.io/<username>/shorty-service:<sha>


🚀 CD Pipeline (GitHub Actions)
The CD workflow runs on every push to main and includes:

YAML validation using yamllint

Separate validation for staging and production manifests

No real Kubernetes cluster required

This ensures all manifests are syntactically correct and ready for deployment.

☸ Kubernetes Manifests
Each environment contains:

deployment.yaml

service.yaml

configmap.yaml

secret.yaml

These files define the application’s runtime configuration and service exposure.

🔗 API Endpoints
Shorten a URL

POST /shorten
Redirect to original URL

GET /{short_id}
API documentation

/docs

🧪 Local Testing
bash
pytest
📦 GHCR Packages
All Docker images built by the CI pipeline are pushed to:


https://github.com/users/<username>/packages


✔ Summary
This project includes:

A functional FastAPI service

Docker packaging

Automated CI/CD pipelines

GHCR integration

Kubernetes manifests for two environments

YAML validation in CD

A clean, production‑ready structure