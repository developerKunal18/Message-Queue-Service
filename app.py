from flask import Flask, request, jsonify
from queue import Queue
from threading import Thread
import time

app = Flask(__name__)

# Message Queue
message_queue = Queue()

# Processed messages
processed_messages = []


# ---------- Consumer ----------
def worker():

    while True:

        message = message_queue.get()

        print(
            f"Processing: {message}"
        )

        time.sleep(3)

        processed_messages.append(
            message
        )

        message_queue.task_done()


# Start background worker
Thread(
    target=worker,
    daemon=True
).start()


# ---------- Producer ----------
@app.route(
    "/enqueue",
    methods=["POST"]
)
def enqueue():

    data = request.get_json()

    message_queue.put(
        data["message"]
    )

    return jsonify({
        "message":
        "Added to queue"
    })


# ---------- Queue Status ----------
@app.route("/queue")
def queue_status():

    return jsonify({
        "messages_waiting":
        message_queue.qsize()
    })


# ---------- Processed Messages ----------
@app.route("/processed")
def processed():

    return jsonify(
        processed_messages
    )


# ---------- Health ----------
@app.route("/health")
def health():

    return jsonify({
        "status":
        "healthy"
    })


if __name__ == "__main__":

    app.run(
        debug=True
    )
