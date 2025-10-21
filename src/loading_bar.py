from tqdm import tqdm
import random
import time

status_messages = [
    "Injecting memes...",
    "Calibrating dank levels...",
    "Converting caffeine to code...",
    "Generating random excuses...",
    "Loading virtual motivation...",
    "Downloading more RAM...",
    "Compressing funny cats...",
    "Reticulating splines...",
    "Mining digital cookies...",
    "Buffering procrastination..."
]
total = 10000

with tqdm(total=total, desc=random.choice(status_messages)) as pbar:
    for i in range(total):
        time.sleep(0.001)  # simulating some work
        if i % (total / 5) == 0:  # update every 20%
            pbar.set_description(random.choice(status_messages))
        pbar.update(1)

print(random.choice(status_messages), "completed.")