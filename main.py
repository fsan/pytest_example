from utils.memoize import Memoize
from utils.passwords import hashed_password, authenticate

def hello_world():
	return "hello_world"

def printer(text):
	return "this is text"

@Memoize
def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)

def main():
	print(hello_world())
	print(printer("hello"))
	print(fib(10))
	print(authenticate("root", "banana"))
	print(authenticate("root", "root"))

if __name__ == '__main__':
	main()
