def random_num(min_value, max_value):
  import time
  seed = time.time()

  a = 110351524512
  c = 12345
  m = 2**31

  random_number = ((seed * a + c) % m) / (m - 1)

  return int(random_number * (max_value - min_value + 1)) + min_value