import time

def random_num(min_value, max_value):
  seed = time.time()

  a = 110351524512
  c = 12345
  m = 2**31

  random_number = ((seed * a + c) % m) / (m - 1)

  return int(random_number * (max_value - min_value + 1)) + min_value

min_num = 5
max_num = 30
random_value = random_num(min_num, max_num)
print(random_value)