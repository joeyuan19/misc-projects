import timeit


explicit_and_test = "1 == 0 and " + " and ".join(str(i) + " == " + str(i) for i in range(1000))

t = timeit.Timer(explicit_and_test)
print t.timeit()

function_and_test = "all([1 == 0, " + ", ".join(str(i) + " == " + str(i) for i in range(1000)) + "])"

t = timeit.Timer(function_and_test)
print t.timeit()

setup = """def test_gen(n):
    yield 1 == 0
    for i in range(1,n):
        yield i == i"""

generator_and_test = "all(i for i in test_gen(1000))"

t = timeit.Timer(generator_and_test,setup=setup)
print t.timeit()
