import time
import schedule
from data_generator import generate_json_data
from kafka_producer import send_to_kafka

# Функція для періодичного надсилання даних
def job():
    key, value = generate_json_data()
    send_to_kafka('user_events', key, value)

# Планування задачі кожні 10 секунд
schedule.every(10).seconds.do(job)

print("Scheduler started...")

# Безкінечний цикл для виконання планувальника
while True:
    schedule.run_pending()
    time.sleep(1)
