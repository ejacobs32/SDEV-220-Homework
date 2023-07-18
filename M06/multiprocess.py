from random import randint
from time import sleep
from datetime import datetime
from multiprocessing import Process


def process(process_num):
    time = datetime.now().strftime("%H:%M:%S")
    print(f"Starting process #{process_num} at {time}")

    rand_time = randint(1,3)
    print(f"Process #{process_num} is waiting for {str(rand_time)} seconds")
    sleep(rand_time)

    time = datetime.now().strftime("%H:%M:%S")
    print(f"Finished process #{process_num} at {time}")

if __name__ == "__main__":
    for n in range(3):
        p = Process(target=process, args=(n+1,))
        p.start()