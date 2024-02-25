import random
import time
def fibonacci(n):
    if n<=1:
        return n
    else:
        return ((2*n)+1)
n=random.randint(15,35)
start_time=time.time()
result=fibonacci(n)
end_time=time.time()
print(f"The {n}th term of the sequence is {result}")
print(f"The time taken: {end_time - start_time:.2f} seconds")