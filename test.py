import scipy.signal as signal
import numpy as np

input = [1, 2, 3, 5, 2, 4]
pattern = [9,6,8,1,2]


def prod_m(m):
    res = min(len(input) - m, len(pattern))
    return np.dot(input[m:m + res], pattern[0:res])


convolve_man = [prod_m(m) for m in range(len(input))]
print(convolve_man)

convolved_num = signal.convolve(input, pattern[::-1])[len(pattern)-1:]
# convolved_num = signal.fftconvolve(input, pattern[::-1], mode='same')
print(convolved_num)