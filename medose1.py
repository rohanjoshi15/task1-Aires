import math


# in this code ive taken camera as the point of reference 

def offsetting(x, y, z):
    # We have to move extra in the y direction to add the offset
    # x and z should remain the same only add offset to y after the base of the camera reaches the marker
    x_final = x
    y_final = y + 55  
    z_final = z    

    return (x_final, y_final, z_final)

def compute_distance(x1, y1, z1, x2, y2, z2):
    # need to get the distance between two points cause we need it
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

# marker position as detected by the camera relative to the camera's base
x, y, z = 30, 40, -60  

x_final, y_final, z_final = offsetting(x, y, z)

# Dist. for computations
distance_before = compute_distance(0, 0, 0, x, y, z)  
distance_after = compute_distance(0, 0, 0, x_final, y_final, z_final)  

# Output
print(f"Original marker position from camera : ({x}, {y}, {z})")
print(f"Corrected position with the offset: ({x_final}, {y_final}, {z_final})")
print(f"Distance Before Adjustment: {distance_before:.2f} m")
print(f"Distance After Adjustment: {distance_after:.2f} m")

