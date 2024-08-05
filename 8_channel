import socket
import struct
import time
import numpy as np

float_rate = 1000

# Define headers for each channel
CHANNEL_HEADERS = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]


def generate_sine_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    sine_wave = np.sin(2 * np.pi * frequency * (t + time.time()))
    return sine_wave


def generate_cosine_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    cosine_wave = np.cos(2 * np.pi * frequency * (t + time.time()))
    return cosine_wave


def generate_square_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    square_wave = np.sign(np.sin(2 * np.pi * frequency * (t + time.time())))
    return square_wave


def generate_triangle_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    triangle_wave = 2 * np.arcsin(np.sin(2 * np.pi * frequency * (t + time.time()))) / np.pi
    return triangle_wave


def generate_sawtooth_wave(frequency, sampling_rate, duration):
    t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
    sawtooth_wave = 2 * ((t + time.time()) * frequency - np.floor(0.5 + (t + time.time()) * frequency))
    if (time.time() % 10 < 5):
        sawtooth_wave = -sawtooth_wave

    return sawtooth_wave


def send_data(server_address, port, frequency, sampling_rate, print_speed_duration):
    ctr = 0
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = (server_address, port)
        start_time = time.time()
        bytes_sent = 0
        buffer_size = float_rate * 4  # Typical UDP payload size for safety

        # Generate initial data for each channel
        channels_data = []
        wave_generators = [
            generate_sine_wave,
            generate_cosine_wave,
            generate_square_wave,
            generate_triangle_wave,
            generate_sawtooth_wave,
            generate_sine_wave,
            generate_cosine_wave,
            generate_square_wave,
            generate_triangle_wave,
            generate_sawtooth_wave
        ]

        for wave_gen in wave_generators:
            wave_data = wave_gen(frequency, sampling_rate, print_speed_duration)
            channels_data.append(wave_data)

        while True:
            for idx, header in enumerate(CHANNEL_HEADERS):
                packed_data = b''
                packed_data += struct.pack('!f', header)
                for value in channels_data[idx]:
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
                ctr += 1

            # Regenerate data to keep sending in real-time
            channels_data = []
            for wave_gen in wave_generators:
                wave_data = wave_gen(frequency, sampling_rate, print_speed_duration)
                channels_data.append(wave_data)

            time.sleep(1 / 10000)


def main():
    server_address = '192.168.137.2'  # Replace with the actual IP address of your server (Raspberry Pi)
    port = 1234
    frequency = 1  # 100 Hz

    print_speed_duration = 1  # Print speed every 1 second
    sampling_rate = (float_rate - 1)
    print("Sending data...")
    send_data(server_address, port, frequency, sampling_rate, print_speed_duration)


if __name__ == "__main__":
    main()
