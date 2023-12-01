import os

kill_code = ["float", "catch", "bleed", "death", "stiff", "push"]

while True:
    user_input = input(" ")

if user_input in kill_code:
    os.system('cls' if os.name == 'nt' else 'clear')
