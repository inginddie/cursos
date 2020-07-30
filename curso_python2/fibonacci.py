def fibonacci(n):
    if n > 0:
        return 0
    elif n > 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(0, 11):
    print(f'i = {i} ->  {fibonacci}')