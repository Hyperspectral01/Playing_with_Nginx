
---

# 🚀 NGINX Deployment Scenarios — A Simple Hands-On Guide

This repo is a quick, practical walkthrough of how real deployments work using **Flask**, **Waitress**, and **NGINX**.  
Each scenario builds on the previous one — starting from a basic dev server and moving all the way to **HTTPS, virtual hosting, static file serving, and load balancing**.  
Perfect for understanding how modern web apps are actually deployed in the real world.

These scenarios have been given to us by our professor [Dr. Priyank Thakkar](https://www.kaggle.com/priyankdl)


📄 **Full Documentation:**
👉 [`Detailed_Steps.docx`](Detailed_Steps.docx)

---

# 📚 Table of Contents

* [🎯 Aim of the Practical](#-aim-of-the-practical)
* [📦 Repository Structure](#-repository-structure)
* [🧠 Concepts You Will Learn](#-concepts-you-will-learn)
* [🚀 Scenarios Overview](#-scenarios-overview)
* [⚙️ Setup & Usage Instructions](#️-setup--usage-instructions)
* [📝 Scenario Descriptions](#-scenario-descriptions)
* [🐳 Commands Reference](#-commands-reference)
* [🔒 SSL / HTTPS Notes](#-ssl--https-notes)
* [⚡ Load Balancing Notes](#-load-balancing-notes)

---

# 🎯 Aim of the Practical

This project helps you **understand how real industry deployments work**, including:

✔ How a **web server** operates
✔ How to configure **NGINX** for different environments
✔ How a **dev server** differs from a **prod server**
✔ How to set up **reverse proxies**, **virtual hosting**, **SSL**, **static file servers**, and **load balancing**

By going through each scenario, you will gain the confidence to build **robust production-grade deployments**.

---

# 📦 Repository Structure

```
Deployment_Scenarios/
│
├── Scenario_1/
├── Scenario_2/
├── Scenario_3/
├── Scenario_4/
├── Scenario_5/
├── Scenario_6/
├── Scenario_7/
├── Scenario_8/
├── Scenario_9/
├── Scenario_10/
├── Scenario_11/
│
└── Detailed_Steps.docx   <-- Full documentation
```

Each scenario folder contains:

* Flask app
* Nginx configuration
* HTML templates
* Additional config files if required

---

# 🧠 Concepts You Will Learn

### 🔹 Development vs Production Servers

* How Flask dev server works
* Why dev servers should **never** be deployed
* How Waitress serves production traffic

### 🔹 NGINX as:

* Reverse Proxy
* Load Balancer
* Static asset server
* SSL / HTTPS termination proxy
* Virtual host manager (multiple domains on one or multiple apps)

### 🔹 Deployment Essentials

* Host-to-IP mapping on Windows (`C:/Windows/System32/drivers/etc/hosts`)
* Handling multiple apps on different ports
* Running apps on different systems
* Sticky sessions & ip_hash

---

# 🚀 Scenarios Overview

| Scenario | Description                                                      |
| -------- | ---------------------------------------------------------------- |
| **1**    | Basic Flask Dev Server                                           |
| **2**    | Production Server using Waitress                                 |
| **3**    | NGINX Reverse Proxy to a Single App                              |
| **4**    | NGINX + Waitress — Single App Handling Multiple Domains          |
| **5**    | NGINX with Multiple Server Blocks (two domains → one app)        |
| **6**    | Two Separate Apps on Same Machine (different ports)              |
| **7**    | Two Apps Running on Different Machines                           |
| **8**    | HTTPS Setup with Self-Signed Certificate                         |
| **9**    | HTTPS with Real CA (Let’s Encrypt / GoDaddy) *(not implemented)* |
| **10**   | Serving Static Files Efficiently                                 |
| **11**   | Load Balancing + Sticky Sessions                                 |

---

# ⚙️ Setup & Usage Instructions

## 1️⃣ Running Application Servers

Open a terminal in your scenario folder and run:

```bash
python <app-file-name>.py
```

To run multiple apps simultaneously → open multiple terminals.

---

## 2️⃣ Running NGINX

Go to:

```
/nginx-1.26.3/
```

Start NGINX:

```bash
nginx.exe
```

Stop NGINX:

```bash
nginx -s stop     # Force stop
nginx -s quit     # Graceful stop
```

Reload configuration:

```bash
nginx -s reload
```

If NGINX refuses to stop:

```bash
taskkill /F /IM nginx.exe /T
```

---

## 3️⃣ Editing NGINX Configurations

Edit:

```
/nginx-1.26.3/conf/nginx.conf
```

Each scenario folder includes the required configuration blocks.

---

# 📝 Scenario Descriptions

Below is a **high-level summary** of each scenario. Full configurations are present inside each folder.

---

## **🔥 Scenario 1 – Basic Flask Dev Server**

* Runs using `app.run()`
* Debug mode enabled
* Auto reload
* Meant only for development

---

## **🔥 Scenario 2 – Production Server (Waitress)**

* Replace Flask dev server with **Waitress**
* Proper production WSGI server
* Accessible via system IP (`0.0.0.0`)

---

## **🔥 Scenario 3 – NGINX Reverse Proxy to One App**

* NGINX listens on port 80/1400
* Proxies requests to Waitress at `127.0.0.1:5001`
* No domain names yet (local development)

---

## **🔥 Scenario 4 – Virtual Hosting (One App, Multiple Domains)**

* Domains: `my_site_1.com`, `my_site_2.com`
* One app decides response based on `request.host`
* NGINX server block handles both domains
* Proxy pass → `127.0.0.1:5005`

---

## **🔥 Scenario 5 – Two Server Blocks (Both Proxying to One App)**

* Each domain gets its own server block
* Same app receives both requests
* App identifies domain using `request.host`

---

## **🔥 Scenario 6 – Two Apps, Same Machine**

* App1 → port 5000
* App2 → port 5001
* NGINX routes based on domain name

---

## **🔥 Scenario 7 – Two Apps on Different Machines**

* NGINX routes traffic to different backend systems
* Realistic distributed deployment
* Example:

  * `my_site_1.com → 10.53.163.247:5001`
  * `my_site_2.com → 10.53.163.45:5000`

---

## **🔥 Scenario 8 – HTTPS with Self-Signed SSL**

* Generate certs using OpenSSL
* Use:

  ```
  ssl_certificate
  ssl_certificate_key
  ssl_protocols
  ssl_ciphers HIGH
  ```
* NGINX listens using SSL on port 1400

---

## **🔥 Scenario 9 – HTTPS with Real CA** *(Not Implemented)*

You can use:

* **Let’s Encrypt (Free)**
* **GoDaddy / ZeroSSL / DigiCert (Paid)**

---

## **🔥 Scenario 10 – Static File Serving**

Use either:

```nginx
location /static/ {
    alias C:/path/to/static/;
}
```

or

```nginx
location /static/ {
    root C:/path/to/project/;
}
```

---

## **🔥 Scenario 11 – Load Balancing + Sticky Sessions**

NGINX upstream block:

```nginx
upstream my_waitress_servers {
    ip_hash;
    server 10.65.49.45:5000;
    server 10.65.49.154:5000;
    server 127.0.0.1:5000;
}
```

---

# 🐳 Commands Reference

### Kill all Nginx processes:

```bash
taskkill /F /IM nginx.exe /T
```

### Check IP of system:

```bash
ipconfig
```

### Reload NGINX after changes:

```bash
nginx -s reload
```

---

# 🔒 SSL / HTTPS Notes

### With OpenSSL you can generate:

* Private key
* CSR (Certificate Signing Request)
* Self-signed certificate

Used in Scenario 8.

For production, use CA-signed certs (Let’s Encrypt recommended).

---

# ⚡ Load Balancing Notes

NGINX supports:

* **Round robin** (default)
* **Least Connections**
* **ip_hash** (sticky sessions)

Used in Scenario 11 for session persistence.

---

**By Shrey Vyas**
MLOps | Deployment | Cloud | NGINX | DevOps Learner

