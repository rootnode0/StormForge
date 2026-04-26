# 🌩️ StormForge

> A controlled chaos simulation platform for testing distributed systems under load.

---

## 🚀 What is StormForge?

StormForge is a lightweight chaos engineering playground where you can:

- Trigger distributed jobs via API
- Simulate failures, retries, and delays
- Generate logs and files across services
- Create both internal and external system load

---

## 🧠 Features

- 🔥 Chaos Engine (random failures & delays)
- 🔁 Background workers (Celery)
- 📜 Log generation per mission
- 🌐 External API simulation (httpbin)
- ⚡ Internal scheduled load (Celery Beat)
- 🚀 External load testing support (Locust / scripts)

---

## 🏗️ Architecture

- FastAPI (API layer)
- Celery (worker system)
- Redis (queue + broker)
- Shared volumes (logs + files)
- Docker Compose (orchestration)

---

## ⚙️ Setup

### 1. Clone repo

```bash
git clone <your-repo>
cd stormforge
```

---

### 2. Start services

```bash
docker compose -p stormforge up --build
```

---

### 3. Access API

```
http://localhost:8080
```

---

## 🔥 Usage

### Start a mission

```bash
curl -X POST http://localhost:8080/mission/start
```

---

### Watch logs

```bash
tail -f shared/logs/<mission_id>.log
```

---

## 🌊 Generate Load

### Simple script

```python
import requests, time

while True:
    requests.post("http://localhost:8080/mission/start")
    time.sleep(0.2)
```

---

### Advanced load

Use:

- Locust
- k6

---

## 🧪 What You Can Test

- High traffic scenarios
- Retry behavior
- Log tracing
- Worker queue buildup
- Failure handling

---

## ⚡ Roadmap

- Multi-node API (Nginx)
- Log streaming UI
- File processing pipeline
- Kubernetes deployment

---

## 🛑 Notes

- Do not use production ports (80/443)
- Designed for local / LAN testing
- Safe to run alongside other Docker setups

---

## 💡 Philosophy

StormForge is not a toy.

It’s a controlled environment to:

> Break things → Observe → Learn → Improve

---

## 👨‍💻 Author

Built for deep system understanding and real-world debugging practice.
