import time

import numpy as np

lista = list(range(1_000_000))
arr = np.arange(1_000_000)

t = time.time()
r1 = [x * 2 for x in lista]
print("Lista:", time.time() - t)

t = time.time()
r2 = arr * 2
print("NumPy:", time.time() - t)
