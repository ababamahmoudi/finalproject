# 🌩️ CloudMart – Enterprise Cloud Architecture Project

A fully deployed, production-style cloud application built for CSP451.  
CloudMart demonstrates modern cloud engineering practices including:

- Multi-tier application design  
- Containerized microservices  
- Azure Load Balancer  
- Dedicated DB tier  
- Prometheus + Grafana monitoring  
- CI/CD automation  
- Cloud security controls  
- Disaster recovery planning  

---

## 📐 High-Level Architecture

![Architecture Diagram](./docs/architecture.png)

**Components:**

- **Frontend VM** — React app served via Nginx  
- **Backend VMs (2x)** — FastAPI microservice, Redis caching  
- **Database VM** — PostgreSQL (private-only network access)  
- **Load Balancer** — Azure LB distributing traffic across backend VMs  
- **Monitoring** — Prometheus + Grafana  
- **Serverless Functions** — Email, inventory, order processing  

---

## 🚀 Features

### Application Layer
- Product catalog API  
- Redis caching (improves performance)  
- Health endpoints  
- Auto-seeding database  
- Horizontal scalability via multiple backend VMs  

### Cloud Architecture
- Private subnets for backend + DB  
- Azure Load Balancer distributing load  
- Separate monitoring VM  
- Prometheus exporters for all VMs  

### DevOps
- CI/CD pipeline (GitHub Actions)  
- Build → test → security scan → deploy  
- Blue/green strategy (documented)  

### Security
- NSGs blocking all public traffic  
- Only LB frontend open  
- Private DB  
- Threat model  
- Encryption (TLS handled by Nginx or cert integration)  

---

## 📦 Folder Structure

# 🌩️ CloudMart – Enterprise Cloud Architecture Project

A fully deployed, production-style cloud application built for CSP451.  
CloudMart demonstrates modern cloud engineering practices including:

- Multi-tier application design  
- Containerized microservices  
- Azure Load Balancer  
- Dedicated DB tier  
- Prometheus + Grafana monitoring  
- CI/CD automation  
- Cloud security controls  
- Disaster recovery planning  

---

## 📐 High-Level Architecture

![Architecture Diagram](./docs/architecture.png)

**Components:**

- **Frontend VM** — React app served via Nginx  
- **Backend VMs (2x)** — FastAPI microservice, Redis caching  
- **Database VM** — PostgreSQL (private-only network access)  
- **Load Balancer** — Azure LB distributing traffic across backend VMs  
- **Monitoring** — Prometheus + Grafana  
- **Serverless Functions** — Email, inventory, order processing  

---

## 🚀 Features

### Application Layer
- Product catalog API  
- Redis caching (improves performance)  
- Health endpoints  
- Auto-seeding database  
- Horizontal scalability via multiple backend VMs  

### Cloud Architecture
- Private subnets for backend + DB  
- Azure Load Balancer distributing load  
- Separate monitoring VM  
- Prometheus exporters for all VMs  

### DevOps
- CI/CD pipeline (GitHub Actions)  
- Build → test → security scan → deploy  
- Blue/green strategy (documented)  

### Security
- NSGs blocking all public traffic  
- Only LB frontend open  
- Private DB  
- Threat model  
- Encryption (TLS handled by Nginx or cert integration)  

---

## 📦 Folder Structure

finalproject/
├── applications/
│ ├── backend/
│ └── frontend/
├── functions/
├── monitoring/
├── docker/
├── infra/
├── docs/
└── README.md


---

## 🛠️ How to Deploy Backend

SSH into VM:

```bash
cd ~/finalproject/docker
docker compose -f docker-compose.prod.yml up -d --build
```

Environment variables required:
```bash
DATABASE_URL=postgresql+psycopg2://cloudmart:cloudmartpass@<DB_PRIVATE_IP>:5432/cloudmart
REDIS_URL=redis://<DB_PRIVATE_IP>:6379/0
```
