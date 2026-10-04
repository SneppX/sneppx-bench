from sneppx_bench.bench import compare, measure


def test_measure_runs():
    r = measure(lambda: sum(range(100)), repeats=5, warmup=1)
    assert r["median"] >= 0
    assert r["repeats"] == 5


def test_compare_returns_speedup():
    r = compare(lambda: sum(range(10)), lambda: sum(range(10000)), repeats=3)
    assert r["speedup_a_over_b"] > 0
