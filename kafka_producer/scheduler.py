import schedule
import time
from data_generator import generate_key_value
from kafka_producer import send_to_kafka

def job():
    key, value = generate_key_value()
    send_to_kafka('user_events', key, value)

print("Scheduler started...")

# Виконувати `job` кожні 10 секунд
schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)