import threading

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

def sum_range(thread_id, start, end, results):
    # end + 1 because Python's range() stops before the upper bound
    results[thread_id] = sum(range(start, end + 1))


def sum_all_ranges(ranges):
    n = len(ranges)
    results = [0] * n
    threads = []

    #launch threads
    for thread_id, (start, end) in enumerate(ranges):
        t = threading.Thread(target=sum_range,args=(thread_id, start, end, results),)
        threads.append(t)
        t.start()

    #join all threads
    for t in threads:
        t.join()

    #print
    total = sum(results)
    print(f"{results}\n{total}")


if __name__ == "__main__":
    sum_all_ranges(ranges)