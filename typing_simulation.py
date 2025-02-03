# simulate typing a message.
import time

message = input("Please enter the message you want to simulate typing: ")

while not message:
    message = input("Message cannot be empty. Please enter a message: ")

for letter in message:
    time.sleep(0.2)
    print(letter, end="", flush=True)
