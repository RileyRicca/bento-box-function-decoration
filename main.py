import os

kill_code = ["float", "catch", "bleed", "death", "stiff", "push"]

for code in kill_code:
    user_input = input(" ")
    if user_input == code:
        os.system('cls' if os.name == 'nt' else 'clear')