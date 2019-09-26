import random

a = list(random.sample([i for i in range(1, 1001) if i % 35 == 0], 5))
print(a)
