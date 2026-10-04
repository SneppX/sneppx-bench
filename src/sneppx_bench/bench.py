"""Micro-benchmark harness."""

import time


def measure(fn, repeats=30, warmup=3):
    for _ in range(warmup):
        fn()
    times = []
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn()
        times.append(time.perf_counter() - t0)
    times.sort()
    return {
        "min": times[0],
        "median": times[len(times) // 2],
        "max": times[-1],
        "repeats": repeats,
    }


def compare(a, b, repeats=30):
    ra = measure(a, repeats=repeats)
    rb = measure(b, repeats=repeats)
    speedup = rb["median"] / ra["median"] if ra["median"] > 0 else float("inf")
    return {"a": ra, "b": rb, "speedup_a_over_b": speedup}
