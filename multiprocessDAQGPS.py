import random
import time
from multiprocessing import Process, Queue

'''
def read_data(port, baudrate, queue, timestamp_queue):
    ser = serial.Serial(port, baudrate)
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            timestamp = time.time()
            queue.put((timestamp, line))
            timestamp_queue.put(timestamp)
'''

def read_data(dummy_data, queue, timestamp_queue):
    for data in dummy_data:
        timestamp = time.time()
        queue.put((timestamp, data))
        timestamp_queue.put(timestamp)
        time.sleep(0.1)

def process_data(queue1, queue2, timestamp_queue, write_queue):
    while True:
        if not queue1.empty() and not queue2.empty() and not timestamp_queue.empty():
            timestamp1, data1 = queue1.get()
            timestamp2, data2 = queue2.get()
            timestamp = timestamp_queue.get()
            while timestamp1 < timestamp:
                if queue1.empty():
                    break
                timestamp1, data1 = queue1.get()
            while timestamp2 < timestamp:
                if queue2.empty():
                    break
                timestamp2, data2 = queue2.get()
            # Process the received data simultaneously and continuously here
            processed_data = f'Data from stream 1: {data1}, Data from stream 2: {data2}'
            write_queue.put(processed_data)

def write_data(write_queue):
    while True:
        if not write_queue.empty():
            data = write_queue.get()
            # Write the processed data to the bidirectional data stream here
            print(f'Writing processed data to bidirectional data stream: {data}')
            time.sleep(0.1)

if __name__ == '__main__':
    dummy_data1 = [random.randint(0, 100) for _ in range(20)]  # Replace with your dummy data for stream 1
    dummy_data2 = [random.randint(0, 100) for _ in range(30)]  # Replace with your dummy data for stream 2

    queue1 = Queue()
    queue2 = Queue()
    timestamp_queue = Queue()
    write_queue = Queue()

    process1 = Process(target=read_data, args=(dummy_data1, queue1, timestamp_queue))
    process2 = Process(target=read_data, args=(dummy_data2, queue2, timestamp_queue))
    process3 = Process(target=process_data, args=(queue1, queue2, timestamp_queue, write_queue))
    process4 = Process(target=write_data, args=(write_queue,))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()
