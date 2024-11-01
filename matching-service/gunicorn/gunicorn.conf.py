import os

bind = "0.0.0.0:8001"
workers = os.getenv("UVICORN_WORKERS")
worker_class = "uvicorn_worker.UvicornWorker"
backlog = 2048
timeout = 30
keepalive = 2
max_requests = 5000
worker_connections = 1000

errorlog = "-"
loglevel = "info"
accesslog = "-"

access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
