# Create Flask app (app.py)
cat > app.py << EOF
from flask import Flask
import redis
import socket

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    return cache.incr('hits')

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello! I have been seen {count} times.\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
EOF

# Create requirements.txt
cat > requirements.txt << EOF
flask
redis
EOF

# Create Dockerfile
cat > Dockerfile << EOF
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "app.py"]
EOF

# Create docker-compose.yml
cat > docker-compose.yml << EOF
version: '3'
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - redis
  redis:
    image: redis:alpine
    volumes:
      - redis_data:/data

volumes:
  redis_data:
EOF

# Run application
docker-compose up -d
