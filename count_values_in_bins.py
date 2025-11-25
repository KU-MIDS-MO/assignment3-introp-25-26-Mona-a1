#2) count_values_in_bins(data, bin_edges)
#   We want to count how many values fall into each numeric bin.
#   - data is a 1-D NumPy array of numbers.
#   - bin_edges is a 1-D NumPy array of length B+1, strictly increasing.
#   These edges define B bins:
#      Bin 0: [bin_edges[0], bin_edges[1])
#      Bin 1: [bin_edges[1], bin_edges[2])
#      ...
#      Bin B-2: [bin_edges[B-2], bin_edges[B-1])
#      Bin B-1: [bin_edges[B-1], bin_edges[B]]   (last bin is inclusive on the right)
#   Values outside [bin_edges[0], bin_edges[-1]] are ignored.
#   Return a 1-D NumPy array of length B with the counts per bin.




import numpy as np


data = np.array([-1.0, 0.0, 0.9, 5.0, 6.0])
bin_edges = np.array([0.0, 1.0, 2.0, 5.0])

def count_values_in_bins(data, bin_edges):
    B = len(bin_edges)-1
    
    y = 0
    
    new = []
    
    for i in range(B):
        left = bin_edges[i]
        right = bin_edges[i+1]
        
        if i == B-1:
            for value in data:
                if left <= value <= right:
                    y = y+1
        
        else:
            for value in data:
                if left <= value < right:
                    y = y+1
        
        
        
        
        new.append(y)
        y=0
    
    
    return np.array(new, dtype = int)
    
    pass
    ### Replace with your own code (end)   ###

print(count_values_in_bins(data, bin_edges))