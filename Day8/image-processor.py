# Uses multiprocessing.Pool.map() to distribute CPU-bound work across all CPU cores. 
# apply_filter() computes sum(i^2 for i in range(500,000)) to simulate real image processing. 
# Benchmarked against single-process to show speedup. 
# Code comments explain why the GIL blocks threading for CPU bound work -- the most important Python performance concept.
# CPU-bound processing using multiprocessing.Pool. 
# Compare single vs multi-process time. 


import multiprocessing
import time

def apply_filter(img):

    result = sum(
        i*i
        for i in range(20_000_000)
    )

    return f"Processed {img} checksum:{result % 9999}"



def main():

    images = [
        f"photo_{i:03d}.jpg"
        for i in range(1,13)
    ]

    # Single process

    start = time.time()


    single_result = [
        apply_filter(img)
        for img in images
    ]

    end = time.time()

    single_time = end - start

    # Multiprocessing

    start = time.time()

    with multiprocessing.Pool(
        multiprocessing.cpu_count()
    ) as pool:

        print(multiprocessing.cpu_count())

        multi_result = pool.map(
            apply_filter,
            images
        )

    end = time.time()

    multi_time = end - start

    print("\nSingle Process:")
    print(single_result)

    print("\nMultiprocessing:")
    print(multi_result)


    print(f"""

        Single : {single_time:.2f} seconds
        Multi  : {multi_time:.2f} seconds
        Speedup: {single_time/multi_time:.2f}x
        """
    )

if __name__ == "__main__":
    main()