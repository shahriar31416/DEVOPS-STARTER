# DevOps Starter Project

A production-grade scaffold with API app, tests, Docker, Kubernetes (with Kustomize), GitHub Actions CI/CD, and a Terraform stub.

## Features
- **FastAPI** example service (`/healthz`, `/items`)
- **Tests** with `pytest`
- **Dockerfile** and **docker-compose**
- **Kubernetes** manifests with **Kustomize**
- **GitHub Actions** CI (lint, test, build, push) and CD (kubectl apply -k)
- **Terraform** stub (AWS provider + S3 artifacts bucket)
- **Pre-commit** hooks: black, flake8, mypy

## Quick Start (Local)
```bash
# 1) Python virtualenv
make install
make run   # http://localhost:8000/docs

# 2) Docker
make up    # builds and runs container
# visit http://localhost:8000/healthz
make down
```

## Kubernetes
```bash
# assuming you have a cluster and kubectl context set
kubectl apply -k k8s
kubectl get svc devops-starter-svc
```

Edit image in `k8s/kustomization.yaml` to point to your registry:
```
images:
  - name: ghcr.io/your-username/devops-starter
    newTag: latest
```

## CI/CD (GitHub Actions)
- **CI**: runs on push/PR to `main`. Lints, tests, builds, and pushes image to GHCR.
- **CD**: triggers after CI success; applies k8s manifests using `KUBECONFIG_DATA` secret.
  - Add repo secret `KUBECONFIG_DATA` (base64-encoded kubeconfig).

## Terraform (stub)
The `terraform/` folder shows the provider setup and a safe example (S3 bucket). Customize to add EKS/ECR as needed.

## Project Structure
```
.
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── uvicorn_start.sh
├── tests/
│   └── test_app.py
├── Dockerfile
├── docker-compose.yml
├── k8s/
│   ├── deployment.yaml
│   ├── ingress.yaml
│   └── kustomization.yaml
├── .github/workflows/
│   ├── ci.yml
│   └── cd.yml
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── providers.tf
├── Makefile
├── requirements-dev.txt
├── .pre-commit-config.yaml
├── .flake8
├── mypy.ini
├── pyproject.toml
└── README.md
```

## Next Steps
- Replace `ghcr.io/your-username/devops-starter` with your registry path.
- (Optional) Extend Terraform to create ECR/EKS.
- Add observability (Prometheus/Grafana) and logging stack (Loki/ELK).
- Add staging/prod overlays with Kustomize.
```
