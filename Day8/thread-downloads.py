# Creates one Thread per file. 
# Each thread sleeps random(1,4) seconds to simulate download latency. 
# A threading.Lock protects the shared completed list from race conditions. 
# All threads start first, then all join -- demonstrating true concurrency. 
# Wall-clock time equals the longest single download, not the sum. 
# Foundation for all async I/O in Python.
# Download multiple files concurrently using threads (random sleep simulates network). Track 
# progress safely, compare wall-clock time vs sequential

import threading
import time
import random


completed = []

lock = threading.Lock()

total = 0

def download_file(filename, size_mb):

    delay = random.uniform(1,4)

    global total
    total += delay

    print(
        f"[START] {filename} "
        f"on {threading.current_thread().name}"
    )


    # simulate download
    time.sleep(delay)



    # shared resource
    with lock:

        completed.append(filename)


        print(
            f"[DONE] {filename} "
            f"in {delay:.1f}s"
        )

def main():
    files = [
        ("report.pdf",5),
        ("video.mp4",120),
        ("image.jpg",2),
        ("data.csv",15)
    ]

    # Thread version

    start = time.time()
    threads=[]


    # create threads

    for filename, size in files:

        t = threading.Thread(
            target=download_file,
            args=(filename,size)
        )

        threads.append(t)



    # Start ALL threads first

    for t in threads:
        t.start()



    # Wait for ALL threads
    for t in threads:
        t.join()


    end=time.time()

    print("\nCompleted:")
    print(completed)


    print(f"\nThread time: {end-start:.2f}s")


    # Sequential estimate

    print("\nSequential estimate:")
    print(f"{total:.2f}s")

if __name__ == "__main__":
    main()