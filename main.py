def max_two_power(x):
  a = 0
  while 2**a <= x:
    a+=1
  a-=1
  return a 
  
def josephus_winner(n):
  a = max_two_power(n)
  l = n - 2**a
  win = 2*l + 1
  return win
