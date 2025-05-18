import time
attempts = 0
retries = 5
wait_time = 1
while attempts < retries:
    print(f"Attempt {attempts} {time.ctime()} {wait_time}")
    attempts += 1
    time.sleep(wait_time)
    wait_time *= 2