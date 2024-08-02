"""

import socket
import struct
import time
import numpy as np


def generate_sine_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi * frequency * t)
    return sine_wave


def send_data(server_address, port, frequency, sampling_rate, print_speed_duration):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_address, port))
        start_time = time.time()
        bytes_sent = 0
        while True:
            sine_wave_data = generate_sine_wave(frequency, sampling_rate, print_speed_duration)
            for value in sine_wave_data:
                packed_data = struct.pack('!f', value)  # Use network byte order (big-endian)
                s.sendall(packed_data)
                bytes_sent += len(packed_data)

                # Calculate and print speed at specified intervals
                elapsed_time = time.time() - start_time
                if elapsed_time >= print_speed_duration:
                    speed_mbps = (bytes_sent * 8) / (elapsed_time * 1_000_000)
                    print(f"Data rate: {speed_mbps:.2f} Mbps")
                    start_time = time.time()
                    bytes_sent = 0


def main():
    server_address = '192.168.137.2'  # Replace with the actual IP address of your server
    port = 1234
    frequency = 1  # 1 Hz
    sampling_rate = 100  # 1000 samples per second
    print_speed_duration = 10  # Print speed every 1 second

    print("Sending data...")
    send_data(server_address, port, frequency, sampling_rate, print_speed_duration)


if __name__ == "__main__":
    main()
"""

"""
import socket
import struct
import time
import numpy as np


def generate_sine_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi * frequency * t)
    return sine_wave


def send_data(server_address, port, frequency, sampling_rate, print_speed_duration):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_address, port))
        start_time = time.time()
        bytes_sent = 0
        while True:
            sine_wave_data = generate_sine_wave(frequency, sampling_rate, print_speed_duration)
            for value in sine_wave_data:
                packed_data = struct.pack('!f', value)  # Use network byte order (big-endian)
                s.sendall(packed_data)
                bytes_sent += len(packed_data)

                # Calculate and print speed at specified intervals
                elapsed_time = time.time() - start_time
                if elapsed_time >= print_speed_duration:
                    speed_mbps = (bytes_sent * 8) / (elapsed_time * 1_000_000)
                    print(f"Data rate: {speed_mbps:.2f} Mbps")
                    start_time = time.time()
                    bytes_sent = 0


def main():
    server_address = '192.168.137.2'  # Replace with the actual IP address of your server (Raspberry Pi)
    port = 1234
    frequency = 10  # 1 Hz
    sampling_rate = 1000  # 1000 samples per second
    print_speed_duration = 1  # Print speed every 1 second

    print("Sending data...")
    send_data(server_address, port, frequency, sampling_rate, print_speed_duration)


if __name__ == "__main__":
    main()
    
    
    """
"""
import socket
import struct
import time
import numpy as np


def generate_sine_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi * frequency * t)
    return sine_wave


def send_data(server_address, port, frequency, sampling_rate, print_speed_duration):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = (server_address, port)
        start_time = time.time()
        bytes_sent = 0
        buffer_size = 1000  # Number of floats to send at once
        while True:
            sine_wave_data = generate_sine_wave(frequency, sampling_rate, print_speed_duration)
            for i in range(0, len(sine_wave_data), buffer_size):
                chunk = sine_wave_data[i:i + buffer_size]
                packed_data = struct.pack(f'!{len(chunk)}f', *chunk)  # Use network byte order (big-endian)
                s.sendto(packed_data, server_address)
                bytes_sent += len(packed_data)

                # Calculate and print speed at specified intervals
                elapsed_time = time.time() - start_time
                if elapsed_time >= print_speed_duration:
                    speed_mbps = (bytes_sent * 8) / (elapsed_time * 1_000_000)
                    print(f"Data rate: {speed_mbps:.2f} Mbps")
                    start_time = time.time()
                    bytes_sent = 0


def main():
    server_address = '192.168.137.2'  # Replace with the actual IP address of your server (Raspberry Pi)
    port = 1234
    frequency = 1  # 1 Hz
    sampling_rate = 1000  # 1000 samples per second
    print_speed_duration = 1  # Print speed every 1 second

    print("Sending data...")
    send_data(server_address, port, frequency, sampling_rate, print_speed_duration)


if __name__ == "__main__":
    main()
"""

"""
import socket
import struct
import time
import numpy as np


def generate_sine_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi  * t)
    return sine_wave


def send_data(server_address, port, frequency, sampling_rate, print_speed_duration):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = (server_address, port)
        start_time = time.time()
        bytes_sent = 0
        buffer_size = 30  # Number of floats to send at once
        while True:
            sine_wave_data = generate_sine_wave(frequency, sampling_rate, print_speed_duration)
            for i in range(0, len(sine_wave_data), buffer_size):
                chunk = sine_wave_data[i:i + buffer_size]
                packed_data = struct.pack(f'!{len(chunk)}f', *chunk)  # Use network byte order (big-endian)
                s.sendto(packed_data, server_address)
                bytes_sent += len(packed_data)
               
                # Calculate and print speed at specified intervals
                elapsed_time = time.time() - start_time
                if elapsed_time >= print_speed_duration:
                    speed_mbps = (bytes_sent * 8) / (elapsed_time * 1_000_000)
                    print(f"Data rate: {speed_mbps:.2f} Mbps")
                    start_time = time.time()
                    bytes_sent = 0


def main():
    server_address = '192.168.137.2'  # Replace with the actual IP address of your server (Raspberry Pi)
    port = 1234
    frequency = 1000# 10 Hz
    sampling_rate = 100  # 1000 samples per second
    print_speed_duration = 1  # Print speed every 1 second

    print("Sending data...")
    send_data(server_address, port, frequency, sampling_rate, print_speed_duration)


if __name__ == "__main__":
    main()
"""
"""
import socket
import struct
import time
import numpy as np


def generate_sine_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi * frequency * t)
    return sine_wave/2


def generate_custom_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    wave = np.sign(np.sin(2 * np.pi * frequency * t))  # Generates -1, 0, 1 pattern
    return wave / 2


def send_data(server_address, port, frequency, sampling_rate, print_speed_duration):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = (server_address, port)
        start_time = time.time()
        bytes_sent = 0
        buffer_size = 200  # Max UDP payload size is 65507 bytes, using 1440 for safety

        while True:
            sine_wave_data = generate_sine_wave(frequency, sampling_rate, print_speed_duration)
            custom_wave_data = generate_custom_wave(frequency, sampling_rate, print_speed_duration)

            packed_data = struct.pack(f'!{len(sine_wave_data)+len(custom_wave_data)}f', *sine_wave_data, *custom_wave_data)

            data_length = len(packed_data)

            for i in range(0, data_length, buffer_size):
                chunk = packed_data[i:i + buffer_size]
                s.sendto(chunk, server_address)
                bytes_sent += len(chunk)

            elapsed_time = time.time() - start_time
            if elapsed_time >= print_speed_duration:
                speed_mbps = (bytes_sent * 8) / (elapsed_time * 1_000_000)
                print(f"Data rate: {speed_mbps:.2f} Mbps")
                start_time = time.time()
                bytes_sent = 0


def main():
    server_address = '192.168.137.2'  # Replace with the actual IP address of your server (Raspberry Pi)
    port = 1234
    frequency = 10  # 1000 Hz
    sampling_rate = 400 # 10000 samples per second
    print_speed_duration = 1  # Print speed every 1 second

    print("Sending data...")
    send_data(server_address, port, frequency, sampling_rate, print_speed_duration)


if __name__ == "__main__":
    main()
"""

import socket
import struct
import time
import numpy as np

float_rate = 1000

# Define headers for each channel
CHANNEL_1_HEADER = 1.0
CHANNEL_2_HEADER = 2.0
CHANNEL_3_HEADER = 3.0


def generate_sine_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi * frequency * (t+ time.time() ))
    return sine_wave


def generate_custom_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    wave = np.sign(np.sin(2 * np.pi * frequency * (t+ time.time() )))  # Generates -1, 0, 1 pattern
    return wave


def send_data(server_address, port, frequency, sampling_rate, print_speed_duration):
    ctr = 0
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = (server_address, port)
        start_time = time.time()
        bytes_sent = 0
        buffer_size = (float_rate) * 4  # Typical UDP payload size for safety

        sine_wave_data = generate_sine_wave(frequency, sampling_rate, print_speed_duration)
        custom_wave_data = generate_custom_wave(frequency, sampling_rate, print_speed_duration)
        third_channel_data = sine_wave_data + custom_wave_data  # Example of third channel data


        CHANNEL_3_HEADER = 3.0
        CHANNEL_2_HEADER = 2.0
        CHANNEL_1_HEADER = 1.0
        while True:
            # Pack and send data for channel 1 with header
            packed_data = b''
            packed_data += struct.pack('!f', CHANNEL_1_HEADER)
            for value in sine_wave_data:
                packed_data += struct.pack('!f', value)

            data_length = len(packed_data)

            for i in range(0, data_length, buffer_size):
                chunk = packed_data[i:i + buffer_size]
                s.sendto(chunk, server_address)
                bytes_sent += len(chunk)

                # Unpack and print float values from the chunk
                num_floats = len(chunk) // 4  # Each float is 4 bytes
                unpacked_chunk = struct.unpack(f'!{num_floats}f', chunk)
                # print(unpacked_chunk)

            # Pack and send data for channel 2 with header
            packed_data = b''
            packed_data += struct.pack('!f', CHANNEL_2_HEADER)
            for value in custom_wave_data:
                packed_data += struct.pack('!f', value)
            data_length = len(packed_data)
            for i in range(0, data_length, buffer_size):
                chunk = packed_data[i:i + buffer_size]
                s.sendto(chunk, server_address)
                bytes_sent += len(chunk)

                # Unpack and print float values from the chunk
                num_floats = len(chunk) // 4  # Each float is 4 bytes
                unpacked_chunk = struct.unpack(f'!{num_floats}f', chunk)
                # print(unpacked_chunk)

            # Pack and send data for channel 3 with header
            packed_data = b''
            packed_data += struct.pack('!f', CHANNEL_3_HEADER)
            for value in third_channel_data:
                packed_data += struct.pack('!f', value)
            data_length = len(packed_data)
            for i in range(0, data_length, buffer_size):
                chunk = packed_data[i:i + buffer_size]
                s.sendto(chunk, server_address)
                bytes_sent += len(chunk)

                # Unpack and print float values from the chunk
                num_floats = len(chunk) // 4  # Each float is 4 bytes
                unpacked_chunk = struct.unpack(f'!{num_floats}f', chunk)
                # print(unpacked_chunk)

            elapsed_time = time.time() - start_time
            if elapsed_time >= print_speed_duration:
                speed_mbps = (bytes_sent * 8) / (elapsed_time * 1_000_000)
                print(f"Data rate: {speed_mbps:.3f} Mbps")
                start_time = time.time()
                bytes_sent = 0
                ctr = ctr + 1
            """
            if ((ctr % 5) == 0):
                temp3 = CHANNEL_3_HEADER
                temp2 = CHANNEL_2_HEADER
                temp1 = CHANNEL_1_HEADER
                CHANNEL_3_HEADER = temp2
                CHANNEL_2_HEADER = temp1
                CHANNEL_1_HEADER = temp3
            """


            # Regenerate data to keep sending in real-time
            sine_wave_data = generate_sine_wave(frequency, sampling_rate, print_speed_duration)
            custom_wave_data = generate_custom_wave(frequency, sampling_rate, print_speed_duration)
            third_channel_data = sine_wave_data + custom_wave_data  # Example of third channel data

            


def main():
    # server_address = '192.168.137.2'  # Replace with the actual IP address of your server (Raspberry Pi)
    server_address = '192.168.137.2'
    port = 1234
    frequency = 1  # 10 Hz

    print_speed_duration = 1  # Print speed every 1 second
    sampling_rate = (float_rate - 1)
    print("Sending data...")
    send_data(server_address, port, frequency, sampling_rate, print_speed_duration)


if __name__ == "__main__":
    main()
