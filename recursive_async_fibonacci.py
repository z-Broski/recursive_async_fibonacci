# Python 3.11.6 was used
import random
import asyncio

'''
Fibonaccier: Read positive (>0) number n (from stdin or cmdline).

Make 2 asynchronous/concurrent calls to a function fib(...) which
- a) includes a random delay of up to 1 second
- b) calculates and returns the fibonacci number calculated
using the following recursive formula:
    Fib(0) = 0
    Fib(1) = 1
    Fib(n) = Fib(n-1) + Fib(n-2)
Wait until both of the asynchronous calls finish.

Print out the resulting Fibonacci number Fib(n), and which one of
the two calls finished out first.

If you are unsure how to go about it, consider implementing
the solution incrementally e.g. as follows:
  1. Implement a synchronous Fibonacci function without
     the random delay. Verify it produces the correct result.
  2. Change it into an async function. Verify it still works.
  3. Add the random delay into the function.
  4. Implement the 2 concurrent async calls to this function
'''

def enter_fibanacci_number():
    while True:
        user_input = input("Which Fibonacci number would you like to know (positive integer): ")
        if is_positive_integer(user_input):
            return int(user_input)

def is_positive_integer(input_str):
    return input_str.isdigit() and int(input_str) >= 0


def recursive_fibonacci(num):
   if num <= 1:
       return num
   else:
       return recursive_fibonacci(num - 1) + recursive_fibonacci(num - 2)
   
async def sleep_and_recursive_fibonacci(num, call_number):
    # Sleep between 0 and 1 sec
    await asyncio.sleep(random.random())
    result = recursive_fibonacci(num)
    # print(f"Call number {call_number} finished. Fibonacci num {num} is {result}!")

    # Returns the time of execution and the fibonacci number
    return [asyncio.get_event_loop().time(), result]


async def main():
    user_input = enter_fibanacci_number()
    result1, result2 = await asyncio.gather(sleep_and_recursive_fibonacci(user_input, 1), sleep_and_recursive_fibonacci(user_input, 2))

    # compare the times of finished executions of the functions
    if result1[0] < result2[0]:
        print(f"Task 1 finished first. Fibonacci num is {result1[1]}")
    elif result1[0] > result2[0]:
        print(f"Task 2 finished first. Fibonacci num is {result2[1]}")
    else:
        print(f"Both tasks finished at the same time. Fibonacci num is {result1[1]}")

if __name__ == "__main__":
    asyncio.run(main())
