# Application Security Hafifa

> A structured, self-paced onboarding knowledge base covering the core domains of Application Security, DevSecOps, Cloud, and modern infrastructure — written in Hebrew with English technical terminology.

---

## Table of Contents

- [About](#about)
- [Who Is This For](#who-is-this-for)
- [Repository Structure](#repository-structure)
- [Recommended Reading Order](#recommended-reading-order)
- [Topics Covered](#topics-covered)
  - [Networks (רשתות)](#1-networks-רשתות)
  - [Linux](#2-linux)
  - [Virtualization (וירטואליזציה)](#3-virtualization-וירטואליזציה)
  - [Git & GitHub](#4-git--github)
  - [CI/CD](#5-cicd)
  - [DevSecOps](#6-devsecops)
  - [Security](#7-security)
  - [Cloud Providers (ספקי ענן)](#8-cloud-providers-ספקי-ענן)
  - [Cloud (ענן)](#9-cloud-ענן)
  - [Additional Topics](#10-additional-topics)
  - [WIZ](#11-wiz)
- [How to Use This Repository](#how-to-use-this-repository)
- [Contributing](#contributing)

---

## About

This repository is a comprehensive **Application Security onboarding (חפיפה)** knowledge base. It is designed as a structured learning path for security professionals, developers, and engineers who want to build a solid foundation in AppSec, DevSecOps, cloud infrastructure, and networking.

The materials are organized into topical folders, each containing focused Markdown notes. A [Reading Order Flowchart](AppSec-Hafifa/Reading%20Order%20Flowchart.md) is provided to guide you through the content in a logical, dependency-aware sequence.

---

## Who Is This For

- New team members onboarding into an AppSec or DevSecOps role
- Security engineers looking to consolidate knowledge across multiple domains
- Developers who want to understand the security landscape around their applications
- Anyone preparing for interviews or certifications in cloud security or DevSecOps

---

## Repository Structure

```
AppSec-Hafifa/
├── Attachments/                ← Images and assets
├── Code-Projects/              ← Code samples (e.g. tracert.py)
├── Reading Order Flowchart.md  ← Start here
├── Reading Order.canvas
├── Learn_Flow_Canvas.canvas
├── CI-CD/
├── DevSecOps/
├── GIT & GITHUB/
├── Linux/
├── Security/
├── WIZ/
├── וירטואליזציה/               (Virtualization)
├── נושאים נוספים שצריך ללמוד לדעתי/  (Additional Topics)
├── ספקי ענן/                   (Cloud Providers)
├── ענן/                        (Cloud)
└── רשתות/                      (Networks)
```

---

## Recommended Reading Order

A detailed, visual flowchart of the recommended reading order is available here:

📄 [Reading Order Flowchart](AppSec-Hafifa/Reading%20Order%20Flowchart.md)

The recommended high-level order is:

```
Networks → Linux → Virtualization → Git & GitHub → CI/CD →
DevSecOps → Security → Cloud Providers → Cloud → Additional Topics → WIZ
```

Each section builds on concepts introduced in the previous one.

---

## Topics Covered

### 1. Networks (רשתות)

Foundational networking knowledge covering the OSI model from the ground up.

| File | Description |
|------|-------------|
| מודל שבע השכבות | The 7-layer OSI model overview |
| השכבה השנייה – השביעית הרחבה | Deep dives into OSI Layers 2–7 |
| TLS-SSL | Transport Layer Security and SSL explained |
| Wireshark | Packet capture and traffic analysis |
| Tunneling | VPN tunneling protocols and concepts |

---

### 2. Linux

| File | Description |
|------|-------------|
| לינוקס בסיסי | Core Linux commands, filesystem, permissions, and CLI essentials |

---

### 3. Virtualization (וירטואליזציה)

| File | Description |
|------|-------------|
| Cloud – High Level | High-level overview of cloud computing |
| מה זה on-prem | On-premises vs. cloud environments |
| בסיס של ענן | Cloud fundamentals |
| Containers | Docker and container concepts |
| Kubernetes | Container orchestration with Kubernetes |

---

### 4. Git & GitHub

| File | Description |
|------|-------------|
| Git | Version control fundamentals |
| GitHub | Collaboration, branching strategies, and GitHub workflows |

---

### 5. CI/CD

| File | Description |
|------|-------------|
| What Is CI/CD | Continuous Integration and Continuous Delivery explained |
| Blue-Green Deployment | Zero-downtime deployment strategy |
| Canary Deployments | Incremental, risk-controlled rollout strategy |
| DevOps Pipeline | End-to-end pipeline architecture and stages |

---

### 6. DevSecOps

Security integrated throughout the software development lifecycle.

| File | Description |
|------|-------------|
| DevSecOps Explained | Core principles and culture of DevSecOps |
| SAST | Static Application Security Testing |
| SCA | Software Composition Analysis |
| Posture Management | Security posture and compliance tracking |
| Secret Detection | Preventing credential and secret leakage |
| Other Tools | Additional DevSecOps tooling |
| JFrog | Artifact management and security with JFrog |

---

### 7. Security

Core application and infrastructure security concepts.

| File | Description |
|------|-------------|
| Cryptography | Symmetric/asymmetric encryption, hashing, and more |
| PKI | Public Key Infrastructure and certificate management |
| Authentication and Authorization | Identity, OAuth, RBAC, MFA, and access control |
| Vulnerabilities and Exploits | CVEs, vulnerability classes, and exploit techniques |
| Web Attacks | OWASP Top 10, XSS, SQLi, CSRF, and more |
| AppSec | Application security testing and secure SDLC |
| Secret Management | Vault, secrets lifecycle, and best practices |
| Network Security | Firewalls, IDS/IPS, segmentation |
| Endpoint Security | EDR, host-based security controls |
| SIEM | Security Information and Event Management (Microsoft Sentinel) |
| Concepts | General security concepts and terminology |

---

### 8. Cloud Providers (ספקי ענן)

| File | Description |
|------|-------------|
| What is a Cloud Provider | Overview of major cloud providers |
| Shared Responsibility Model | Security responsibilities in cloud environments |
| Threat Modeling | Identifying and mitigating cloud threats |
| What is SDN | Software-Defined Networking |
| Horizontal vs Vertical Scaling | Scaling strategies and trade-offs |
| Hub & Spoke Network Topology | Network architecture patterns |
| East-West / North-South Traffic | Internal vs. external traffic flows |
| Egress and Ingress | Inbound and outbound traffic in cloud |
| AWS | Amazon Web Services core services and security |
| GCP | Google Cloud Platform overview |
| AZURE | Microsoft Azure overview |

---

### 9. Cloud (ענן)

Advanced cloud security and architecture services.

| File | Description |
|------|-------------|
| CWPP | Cloud Workload Protection Platform |
| DSPM | Data Security Posture Management |
| SASE | Secure Access Service Edge |
| CASB | Cloud Access Security Broker |
| API בענן | API security in the cloud |

---

### 10. Additional Topics

| File | Description |
|------|-------------|
| Networking | Supplemental networking deep dives |

---

### 11. WIZ

| File | Description |
|------|-------------|
| Topics to add in Wiz Hafifa | Wiz platform topics and study agenda |

---

## How to Use This Repository

1. **Clone the repository**
   ```bash
   git clone https://github.com/Nturdsh27/AppSec.git
   ```

2. **Open in [Obsidian](https://obsidian.md/)** (recommended)  
   This vault is optimized for Obsidian. Open the `AppSec-Hafifa/` folder as an Obsidian vault to get full support for:
   - Rendered Mermaid diagrams (Reading Order Flowchart)
   - Canvas files (`.canvas`)
   - Linked images and attachments
   - Internal note linking and graph view

3. **Follow the reading order**  
   Begin with the [Reading Order Flowchart](AppSec-Hafifa/Reading%20Order%20Flowchart.md) and progress through each section sequentially.

4. **Use the Attachments folder**  
   All images referenced in notes are stored in `AppSec-Hafifa/Attachments/`. Do not move or rename this folder.

---

## Contributing

Contributions, corrections, and additions are welcome.

1. Fork the repository
2. Create a feature branch: `git checkout -b topic/your-topic-name`
3. Add or edit Markdown files following the existing style
4. Open a Pull Request with a clear description of your changes

---

> **Note:** This knowledge base is written primarily in Hebrew. Technical terms and tool names are kept in English throughout.
