# Cloud SQL App – DevOps / SRE Project

A production-style Flask web application deployed on a Microsoft Azure Virtual Machine with full CI/CD automation and monitoring stack.

---

## 🚀 Architecture Overview

Client → Nginx (Reverse Proxy) → Dockerized Flask App  
Monitoring Stack: Node Exporter → Prometheus → Grafana  

---

## 🛠 Tech Stack

- Python (Flask)
- SQLite
- Docker
- Nginx
- GitHub Actions (CI/CD)
- Prometheus (Metrics scraping)
- Node Exporter (System metrics)
- Grafana (Visualization)
- Linux (Ubuntu)
- Microsoft Azure VM
- Git & GitHub

---

## ⚙️ Key Implementations

### CI/CD Pipeline
- Automated deployment using GitHub Actions
- SSH-based deployment to Azure VM
- Auto Docker image build and container restart on push

### Containerization
- Dockerized Flask application
- Managed container lifecycle and restart policies

### Reverse Proxy
- Configured Nginx to expose application on port 80

### Monitoring & Observability
- Deployed Node Exporter for system metrics
- Configured Prometheus to scrape VM metrics
- Built Grafana dashboards for CPU and memory monitoring

---

## 📊 Monitoring Example

Prometheus and Grafana used to monitor:

- CPU Usage
- Memory Usage
- System Metrics
- Container Health

---

## ☁️ Cloud Deployment

- Hosted on Microsoft Azure Linux VM
- Configured NSG rules for ports 80, 3000, 9090
- Managed systemd services for monitoring tools

---

## 🧠 Skills Demonstrated

- DevOps Automation
- Cloud Infrastructure Management
- Linux System Administration
- Monitoring & Observability
- CI/CD Implementation
- Troubleshooting & Debugging
