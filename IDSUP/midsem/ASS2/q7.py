import math

def ncdf(x):
    return (1 + math.erf(x / math.sqrt(2))) / 2

def inv_ncdf(p:float, mu:float=0, sigma:float=1, tolerance:float=0.00001):
    if mu != 0 or sigma != 1:
        return mu + sigma * inv_ncdf(p, tolerance=tolerance)
    
    low_z = -10
    high_z = 10
    while high_z - low_z > tolerance:
        mid_z = (low_z + high_z) / 2
        mid_p = ncdf(mid_z)
        if mid_p < p:
            low_z = mid_z
        else:
            high_z = mid_z
    return mid_z

# Example usage
p = 0.3
result = inv_ncdf(p)
print(f"The value of z for p={p} is approximately {result}")
