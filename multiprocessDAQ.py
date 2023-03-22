import multiprocessing
import time
import serial
import numpy as np
import matplotlib.pyplot as plt

# Define the function for capturing GPS data
def capture_gps_data(nmea_queue, ntrip_queue):
    # Set up the serial connections for NMEA and NTRIP
    nmea_serial = serial.Serial('COM1', 9600, timeout=1)
    ntrip_serial = serial.Serial('COM2', 9600, timeout=1)

    # Read data continuously from both serial connections
    while True:
        # Read NMEA data
        nmea_data = nmea_serial.readline().decode()
        if nmea_data.startswith('$GPGGA'):
            nmea_queue.put(nmea_data)

        # Read NTRIP data
        ntrip_data = ntrip_serial.readline().decode()
        ntrip_queue.put(ntrip_data)

# Define the function for capturing DAQ data
def capture_daq_data(data_queue):
    # Set up the DAQ connection
    daq_serial = serial.Serial('COM3', 9600, timeout=1)

    # Read data continuously from the DAQ connection
    while True:
        # Read DAQ data
        data = daq_serial.readline().decode()
        data_queue.put(data)

# Define the function for processing captured data
def process_data(nmea_queue, ntrip_queue, data_queue):
    while True:
        # Check if there is new data in the queues
        if not nmea_queue.empty() and not ntrip_queue.empty() and not data_queue.empty():
            nmea_data = nmea_queue.get()
            ntrip_data = ntrip_queue.get()
            data = data_queue.get()

            # Process the data here
            processed_data = np.array([float(x) for x in data.split(',')])

            # Plot the data
            plt.plot(processed_data)
            plt.show()

# Set up the queues for inter-process communication
nmea_queue = multiprocessing.Queue()
ntrip_queue = multiprocessing.Queue()
data_queue = multiprocessing.Queue()

# Create the processes
gps_process = multiprocessing.Process(target=capture_gps_data, args=(nmea_queue, ntrip_queue))
daq_process = multiprocessing.Process(target=capture_daq_data, args=(data_queue,))
process_data_process = multiprocessing.Process(target=process_data, args=(nmea_queue, ntrip_queue, data_queue))

# Start the processes
gps_process.start()
daq_process.start()
process_data_process.start()

# Wait for the processes to finish
gps_process.join()
daq_process.join()
process_data_process.join()
