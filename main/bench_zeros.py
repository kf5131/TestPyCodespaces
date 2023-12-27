import numpy as np
import time

# PARAMS
REPEAT: int = 1000000
VECTOR_LENGTH: int = 10

def make_zeros(len: int=VECTOR_LENGTH):
    b = np.zeros(len, dtype=np.int8)
    return b

def main():
    time_begin = time.perf_counter()
    
    for i in range(REPEAT):
        c = make_zeros()
    
    time_end = time.perf_counter()
    
    print(f"Total time:  {time_end - time_begin} s \nFor vector length: {VECTOR_LENGTH} \nAnd loop-depth:  {REPEAT}")
    
    ...
    

if __name__ == "__main__":
    main()
    
    
    
