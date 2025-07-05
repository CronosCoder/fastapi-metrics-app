# FastAPI Metrics Monitoring App 📊

A production-ready FastAPI application with integrated metrics monitoring using **Prometheus**, **Docker**, and **PostgreSQL**.

---

## 🏗️ System Architecture

```
                        ┌────────────┐
                        │  Prometheus│
                        │  (Metrics) │
                        └────┬───────┘
                             │ scrape /metrics
                             ▼
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│ PostgreSQL DB│◄────►│  FastAPI App │─────►│  /metrics API│
└──────────────┘      └──────────────┘      └──────────────┘
                             ▲
                             │ Background Task
                             ▼
                   (System Metrics Collection)
```

---

## 🚀 Features

- CRUD APIs with FastAPI & PostgreSQL
- Real-time system metrics collection using `psutil`
- Prometheus integration via `/metrics` endpoint
- Background task to update metrics
- Docker & Docker Compose for local setup

---

## 🐳 Run With Docker Compose

> Make sure you have Docker & Docker Compose installed.

```bash
git clone https://github.com/CronosCoder/fastapi-metrics-app
cd fastapi-metrics-app

# Run the application stack (FastAPI + PostgreSQL + Prometheus)
docker-compose up --build
```

📌 App: [http://localhost:8000](http://localhost:8000)  
📌 Docs: [http://localhost:8000/docs](http://localhost:8000/docs)  
📌 Prometheus: [http://localhost:9090](http://localhost:9090)  

---

## ⚙️ Configuration

`.env` file is used to manage environment variables:

```
DATABASE_URL=postgres://postgres:password@db:5432/metrics_db
```

---

## 📈 Custom System Metrics (via `psutil`)

```python
cpu_usage = Gauge("custom_process_cpu_seconds_total", "Total CPU time consumed by the process")
memory_rss = Gauge("custom_process_resident_memory_bytes", "Physical memory in bytes")
memory_vms = Gauge("custom_process_virtual_memory_bytes", "Virtual memory in bytes")
open_fds = Gauge("custom_process_open_fds", "Number of open file descriptors")
threads = Gauge("custom_process_num_threads", "Number of threads used")
gc_collections = Counter("custom_process_gc_collections_total", "Number of GC collections")
uptime = Gauge("custom_process_uptime_seconds", "Process uptime in seconds")
start_time = time.time()
```

### 🔄 Metrics Explanation

| Metric Name                            | Description                                 |
|----------------------------------------|---------------------------------------------|
| `custom_process_cpu_seconds_total`     | CPU time used by the FastAPI process        |
| `custom_process_resident_memory_bytes` | Physical memory usage                       |
| `custom_process_virtual_memory_bytes`  | Virtual memory usage                        |
| `custom_process_open_fds`              | Number of open file descriptors             |
| `custom_process_num_threads`           | Active threads used by the process          |
| `custom_process_gc_collections_total`  | Python garbage collection count             |
| `custom_process_uptime_seconds`        | App uptime since container started          |

---

## 📦 Prometheus Config (`prometheus.yml`)

```yaml
global:
  scrape_interval: 5s

scrape_configs:
  - job_name: "fastapi"
    static_configs:
      - targets: ["fastapi_app:8000"]
```

## 👨‍💻 Author

Developed by Foysal | Backend Python Developer