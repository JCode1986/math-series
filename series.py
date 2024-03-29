def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
      return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n = None):
    if n < 0:
        return None
    elif n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n - 1) + lucas(n - 2)

def sum_series(n, a = 0, b = 1):
  for i in range(0, n):
      temp = a
      a = b
      b = temp + b
  return a
    