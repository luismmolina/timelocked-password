#!/usr/bin/env python3



import hashlib
import sys
import time
import getpass


def get_input():
    total_count = 0
    while not total_count:
        try:
            # We do the double conversion thing to allow 10ex notation
            total_count = int(float(input("Enter count: ")))
        except:
            print("Enter a positive integer.")

    seed, seed_check = "a", "b"
    while seed != seed_check:
        seed = getpass.getpass()
        seed_check = getpass.getpass(prompt="Confirm password: ")
        if seed != seed_check:
            print("Passwords must match.")
    return total_count, seed


def print_progress(total_count, passed_time, current_count):
    projected_time = total_count * passed_time / current_count
    progress_time = "[{:.2f} / {:.2f}s".format(passed_time, projected_time)
    progress_percent = current_count / total_count * 100
    progress_percent = "- {:.2f}%]".format(progress_percent)
    print(progress_time, progress_percent, "   ", end='\r')


if __name__ == "__main__":
    total_count, seed = get_input()
    start_time = time.time()
    current_time = start_time
    m = hashlib.sha256()
    m.update(seed.encode())

    for current_count in range(total_count):
        if time.time() - current_time > 1:
            current_time = time.time()
            passed_time = current_time - start_time
            print_progress(total_count, passed_time, current_count)
        m.update(m.digest())

    print("{} hashes done. Final result:".format(total_count))
    print(m.hexdigest())