from main import hello_world, fib

import pytest

def test_fib_perf_1(benchmark):
    result = None
    result = benchmark(fib, 500)
    assert result != None

def test_fib_perf_2(benchmark):
    result = None
    fib(400)
    result = benchmark(fib, 500)
    assert result != None

def test_hello_world():
	assert hello_world() == "hello_world"

@pytest.fixture
def string_argument():
	return "this is the string argument"

def test_printer(string_argument):
	assert string_argument == "this is the string argument"


def test_fib():
	xs = range(10)
	ys = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
	for i in range(len(xs)):
		assert fib(xs[i]) == ys[i]
