# Huawei Cloud CCE - Cloud Native Autoscaling & Load Balancing Implementation

This project demonstrates a scalable web application architecture deployed on **Huawei Cloud CCE (Cloud Container Engine)**. The primary objective is to analyze system behavior under high traffic, simulate automatic scaling using the **Horizontal Pod Autoscaler (HPA)**, and manage traffic via an Ingress Controller.

## Project Overview
A Dockerized web application was stored in the Huawei SWR (SoftWare Repository) and deployed onto a CCE Turbo Cluster. The architecture utilizes Layer 7 Ingress and ELB (Elastic Load Balance) for traffic management. To validate system resilience, a custom Python-based stress test script was developed and executed from within the cluster environment.

## Architecture & Tech Stack
* **Cloud Provider:** Huawei Cloud
* **Container Engine:** CCE (Cloud Container Engine - Kubernetes)
* **Image Registry:** Huawei SWR
* **Load Balancer:** ELB (Elastic Load Balance) & Nginx Ingress Controller
* **Autoscaling:** Kubernetes HPA (Horizontal Pod Autoscaler)
* **Testing Tools:** Python (Threading & Requests libraries)

## Project Directory Structure

```text
.
├── app/
│   ├── Dockerfile          # Container image definition
│   └── index.html          # Web application source code
├── k8s/
│   ├── deployment.yaml     # Application deployment & resource limits
│   ├── service.yaml        # Internal networking & service discovery
│   ├── ingress.yaml        # Domain routing & external access rules
│   └── hpa.yaml            # Autoscaling policies
├── load-test/
│   ├── attack.py           # Multi-threaded stress test script
│   └── requirements.txt    # Required Python libraries
└── screenshots/            # Proof of concept & test results
