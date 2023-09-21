# Python Celery learning
Show how to use celery in python

## Download
```bash
git clone git@github.com:Lay3r8/python-redis-learning.git
```

## Setup
```bash
cd python-redis-learning

# Create virtual environment (alternatively, use pyenv and pyenv virtualenv)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Start redis and RabbitMQ
docker compose up -d
```

## Run
```bash
# In one terminal tab
celery -A app worker --loglevel=INFO

# In another terminal tab, run the following commands to start downloading with Celery
python main.py

# Pure Python single thread test
python single_thread.py

# Pure Python multi thread test
python multithread.py
```

## Todo
Setup celery on multiple nodes using minikube

## Troubleshooting
Test Redis connection
```bash
python test_redis.py
```
