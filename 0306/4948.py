## 베르트랑 공준: 자연수 n 보다 크고 2n보다 작거나 같은 소수는 적어도 하나 존재한다.

x = int(input())
x_prime = True                
t = []
def isPrime(x):
  for i in range(2,x):
    if x % i == 0:
      t.append(i)

print(t)

def prime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

while True:
    number =int(input())
    count = 0

    if number <= 0:
        break

    else:
        for i in range(number+1, number*2):
            if prime(i):
                count += 1
    
    print(count)
