🧠 Why This Is Important

Instead of:
Client
   ↓
Service A
   ↓
Service B

We can decouple systems:
Producer
    ↓
Message Queue
    ↓
Consumer

Benefits:
✅ Asynchronous processing
✅ Better scalability
✅ Fault tolerance
✅ Decoupled services

Used By
RabbitMQ
Apache Kafka
AWS SQS
Celery

🛠 Tech Stack
Python
Flask
Queue module
Threading

📂 Project Structure
message-queue-service/
│
├── app.py
└── README.md
