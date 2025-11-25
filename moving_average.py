#3) moving_average(signal, window_size)
 #  We want to smooth a 1-D NumPy array using a centered moving average.
  # - signal is a 1-D NumPy array of numbers
   #- window_size is a positive odd integer (1, 3, 5,...).
#   Let k = (window_size - 1) // 2
#   For each index i, consider the indices from max(0, i-k) to min(n-1, i+k),
#   where n is the length of signal, and take the average of those values.
#   Return a new 1-D NumPy array of floats with the same length as signal.



import numpy as np

signal = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
window_size = 3

def moving_average(signal, window_size):
    
    k = (window_size - 1) // 2
    n = len(signal)
    
    new = []
    
    for i in range(n):
        left = max(0, i-k)
        right = min(n-1, i+k)
        
        window = signal[left:right+1]
        new.append(np.mean(window))
        
    new = np.array(new, dtype = float)    
    
    return new
    pass

print(moving_average(signal, window_size))















