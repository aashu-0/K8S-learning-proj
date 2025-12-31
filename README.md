
# Project Flow: FastAPI Greeting App on Kubernetes (Minikube)

## 1. Prerequisites

Ensure the following tools are installed and properly configured on your system:

1. **Docker Desktop**

   * Docker daemon must be running.
   * Verify using:

     ```bash
     docker version
     ```

2. **Docker Hub Account**

   * Required if you plan to push images to a remote registry.
   * Login using:

     ```bash
     docker login
     ```

3. **kubectl**

   * Kubernetes command-line tool.
   * Verify using:

     ```bash
     kubectl version --client
     ```

4. **Minikube**

   * Local single-node Kubernetes cluster for development and learning.
   * Verify installation:

     ```bash
     minikube version
     ```

---

## 2. Application Setup and Local Testing

1. Create a simple FastAPI application with:

   * `app.py`
   * `templates/index.html`
   * `static/style.css`

2. Run the application locally (without Docker) to confirm functionality:

   ```bash
   uvicorn app:app --host 127.0.0.1 --port 8000
   ```

3. Verify in browser:

   ```
   http://localhost:8000
   ```

This step ensures application-level issues are resolved before containerization.

---

## 3. Docker Image Creation and Testing

### 3.1 Create Dockerfile

Create a `Dockerfile` in the project root using `uv` for dependency installation.

### 3.2 Build Docker Image

```bash
docker build -t greeting-fastapi:latest .
```

### 3.3 Verify Image

```bash
docker images
```

### 3.4 Test Container Locally

```bash
docker run -p 8000:8000 greeting-fastapi:latest
```

Access the app at:

```
http://localhost:8000
```

This confirms the image works independently of Kubernetes.

---

## 4. Minikube Setup

### 4.1 Install Minikube

Download and install Minikube from:
[https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)

On Windows:

* Install using the `.exe`
* Run PowerShell as Administrator
* Restart terminal (or system if required)

### 4.2 Start Minikube

```bash
minikube start
# or (if certificate-related issues occur)
minikube start --embed-certs
```

---

## 5. Troubleshooting Minikube Startup

### Common Error

```
Failing to connect to https://registry.k8s.io/
```

### Possible Fixes

1. **If using a proxy**

   ```bash
   minikube start \
     --docker-env HTTP_PROXY=http://your-proxy:port \
     --docker-env HTTPS_PROXY=https://your-proxy:port
   ```

2. **If not using a proxy**

   ```bash
   unset HTTP_PROXY
   unset HTTPS_PROXY
   unset NO_PROXY
   ```

3. **Check DNS resolution**

   ```bash
   nslookup registry.k8s.io
   ```

4. **Clean restart**

   ```bash
   minikube stop
   minikube delete --all
   minikube start
   ```

---

## 6. Verify Kubernetes Cluster Status

Check Minikube status:

```bash
minikube status
```

Verify cluster resources:

```bash
kubectl get nodes
kubectl get pods -A
kubectl get all -A
```

---

## 7. (Optional) Multi-Node Minikube Cluster

To simulate a multi-node cluster:

```bash
minikube start --nodes=2
# or
minikube start --nodes=2 --embed-certs
```

---

## 8. Load Docker Image into Minikube

Since Minikube runs its own container runtime, load the local image explicitly.

1. Verify images:

   ```bash
   docker images
   minikube image list
   ```

2. Load image:

   ```bash
   minikube image load greeting-fastapi:latest
   ```

---

## 9. Kubernetes Deployment

### 9.1 Create Deployment YAML

Create `deployment.yaml` defining:

* Deployment
* Container image
* Ports
* Resource requests and limits

### 9.2 Apply Deployment

```bash
kubectl apply -f deployment.yaml
```

Verify:

```bash
kubectl get deployments
kubectl get pods
```

To delete:

```bash
kubectl delete deployment greeting-fastapi
```

---

## 10. Expose Application via Service

Create a `service.yaml` (NodePort type).

Apply:

```bash
kubectl apply -f service.yaml
```

Verify:

```bash
kubectl get services
```

Access application:

```bash
minikube service greeting-fastapi
```

---

## 11. Testing and Validation

1. Check pod health:

   ```bash
   kubectl get pods
   ```

2. Test self-healing (optional):

   ```bash
   kubectl delete pod <pod-name>
   ```

3. Scale application (optional):

   ```bash
   kubectl scale deployment greeting-fastapi --replicas=3
   ```

---
