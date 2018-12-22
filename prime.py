from time import time
import math
#Find all primes up to n (NOT 1!!)
def primes(n):
  arr_print = [2]
  for a in range(3, n+1):
    prime = True
    max = int(math.sqrt(a)) + 1 #only checks primes upto the square root
    for b in arr_print:
      if a % b == 0:
        prime = False
        break #if it's not prime then break out of loop
      elif b > max:
        break
    if prime:
      arr_print.append(a)#add to array
  print(arr_print)

  return primes


start = time()
print(primes(1000)) 
elapsed = time() - start

print(elapsed)

