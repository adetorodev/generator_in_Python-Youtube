#Generators

# def cookie_maker():
#     yield "First cookie"
#     yield "Second cookie"
#     yield "Third cookie"
#     yield "Forth Cookie"


# cookies = cookie_maker()  # This is the cookie machine
# print(next(cookies))  # You get the first cookie
# print(next(cookies))  # Now the second cookie
# print(next(cookies))  # Finally, the third cookie
# print(next(cookies))

# def counter():
#     yield 1
#     yield 2
#     yield 3


# count = counter()
# print(next(count))
# print(next(count))
# print(next(count))

# Generator with Loop and infinite

def count_to():
    count = 1
    while True:
        yield count
        count += 1

# counter = count_to()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# # for num in counter:
# #     print(num)

squares = (x * x for x in range(8))

# for square in squares:
#     print(square)

def greet_generator():
    while True:
        recieved =yield
        print(f"Hello: {recieved}")

# greet_user = greet_generator()
# next(greet_user)
# print(greet_user.send("John"))
# print(greet_user.send("Doe"))
# print(greet_user.send("Linux"))

def read_file_line(file_path):
    with open(file_path) as file:
        for line in file:
            yield line

# for line in read_file_line("text.txt"):
#     print(line.strip())

def generator_one():
    for i in range(5):
        yield i

def generator_two():
    for value in generator_one():
        yield value * 2

# for result in generator_two():
#     print(result)

import random
import time

def get_sensor_data() :
    return random.uniform(0,100)

def sensor_data_stream():
    # Simulate real-time data coming from a sensor
    while True:
        yield get_sensor_data()  # Generate new data in real-time
        time.sleep(1)

threshold = 75.0
# Process the sensor data

# for data in sensor_data_stream():
#     if data > threshold:
#         print(f"Alert! Sensor data is too high: {data}")
#     else:
#         print(f"Sensor data!  {data:.2f}")


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# # Use the generator
# fib = fibonacci()
# for _ in range(10):
#     print(next(fib))  # Outputs the first 10 Fibonacci numbers


import re

def read_logs(file_path):
    """
    Generator to read log lines from a file one at a time.
    """
    with open(file_path) as file:
        for line in file:
            yield line  # Read log lines

def filter_errors(log_lines):
    """
    Generator that filters log lines and yields only those containing 'ERROR'.
    """
    for line in log_lines:
        if "ERROR" in line:
            yield line  # Only yield error lines

def parse_log_line(line):
    """
    Parses a log line to extract useful details like timestamp, log level, and message.

    Args:
    line (str): A single log line.

    Returns:
    dict: A dictionary containing the parsed details (timestamp, log level, message).
    """
    # Regular expression to parse the log line format
    log_pattern = r"\[(?P<timestamp>.*?)\] (?P<log_level>\w+): (?P<message>.*)"
    match = re.match(log_pattern, line)

    if match:
        return match.groupdict()  # Return the matched groups as a dictionary
    else:
        return {
            "timestamp": None,
            "log_level": "UNKNOWN",
            "message": line.strip()  # In case the log line doesn't match the expected format
        }

def parse_error_details(error_lines):
    """
    Generator that parses error log lines into structured details.
    """
    for line in error_lines:
        yield parse_log_line(line)  # Parse each error line into structured details

# Using the pipeline
log_lines = read_logs("system_logs.txt")
error_lines = filter_errors(log_lines)
error_details = parse_error_details(error_lines)

# Process and print parsed error details
# for error in error_details:
#     print(error)

def powers_of_two():
    n = 0
    while True:
        yield 2 ** n
        n += 1

# Fetch only the first few powers of two
# gen = powers_of_two()
# for _ in range(5):
#     print(next(gen))  # Outputs: 1, 2, 4, 8, 16


# import aiohttp
# import asyncio

# async def fetch_url(session, url):
#     async with session.get(url) as response:
#         return await response.text()

# async def url_fetcher(urls):
#     async with aiohttp.ClientSession() as session:
#         for url in urls:
#             content = await fetch_url(session, url)
#             yield content  # Yield fetched content asynchronously

# # Using the async generator
# async def main():
#     urls = ["https://example.com", "https://example2.com"]
#     async for content in url_fetcher(urls):
#         print(content)  # Process the web page content as it arrives

# Running the async code
# asyncio.run(main())



def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_numbers():
    num = 2
    while True:
        if is_prime(num):
            yield num  # Yield prime numbers lazily
        num += 1

# Get the first 10 primes
# primes = prime_numbers()
# for _ in range(10):
#     print(next(primes))

import itertools

def combination_generator(items):
    for combination in itertools.combinations(items, 2):
        yield combination  # Yield combinations lazily

# Using the generator
for combo in combination_generator([1, 2, 3, 4]):
    print(combo)  # Outputs combinations of 2 items

