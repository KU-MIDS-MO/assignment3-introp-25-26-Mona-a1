## 1) clean_and_scale_scores(scores, min_score, max_score)
#   We have exam scores stored in a NumPy array (1D or 2D).
#   - First, replace all values smaler than min_score by min_score,
#     and all values larger than max_score by max_score.
    
#   - Then linearly scale all values to the range [0, 1] using:
#       scaled = (value - min_score) / (max_score - min_score)
 ##  Return a new NumPy array of floats with the same shape as scores




import numpy as np

scores = np.array([
            [-10, 0],
            [50, 200]
        ])
min_score = 0
max_score = 100


def clean_and_scale_scores(scores, min_score, max_score):
  
    scores1 = scores.reshape(scores.size)
  
    for i in range(scores1.size):
                if scores1[i] < min_score:
                    scores1[i] = min_score
                if scores1[i] > max_score:
                    scores1[i] = max_score
    
    print(scores1)
    
    for i in range(scores1.size):
        value = scores1
        scaled = (value - min_score) / (max_score - min_score)
   
    
    
    
    
    new = np.array([scaled], dtype=float).reshape(scores.shape)
  
    return new

  
  
    
  
    
    pass

print(clean_and_scale_scores(scores, min_score, max_score))