# CloudMart

CloudMart is a Docker-based e-commerce platform deployed on Azure VMs.

It demonstrates:

- Multi-tier architecture (web VMs + database VM + background services VM)
- Backend API (FastAPI) in Docker
- React frontend in Docker
- PostgreSQL + Redis in Docker on a database VM
- Background services for order processing and email
- CI/CD with GitHub Actions + GHCR + SSH deploy to VMs
- Monitoring with Prometheus + Grafana

