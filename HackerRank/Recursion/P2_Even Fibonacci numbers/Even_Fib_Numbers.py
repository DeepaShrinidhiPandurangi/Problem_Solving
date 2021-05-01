t = int(input().strip())
for a0 in range(t):
  n = int(input().strip())
  fib= []
  fib1= []
  a0 = 1
  a1 = 2
  Sum = 0
  fib.append(a0)
  fib.append(a1)
  fib1.append(a1)
  while Sum < n:
    Sum = a0+a1
    if Sum < n: # There was one last extra term coming. So added this.
      fib.append(Sum)
    if Sum%2 == 0 and Sum < n: # There was one last extra term coming. So added this.
      fib1.append(Sum)
    a0 = a1
    a1= Sum
  #print(fib)
  print(sum(fib1))
