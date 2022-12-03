import matplotlib.pyplot as plt
import numpy as np
import math

# global variables
points_count = 10000
earth_area = 510.1  # unit: km^2

# estimate antarctica as a circle
def inAntarctica(x_index, y_index, z_index):
    if z_index < -0.945:
        return True
    else:
        return False

# estimate africa as a triangle
def inAfrica(x_index, y_index, z_index):
    z0 = 0.6
    theta0 = 1.257      # 2/5 * pi
    
    # if point out of latitude
    if z_index < -z0 or z_index > z0:
        return False
    
    # maximum angle points can be away from
    maxTheta = (theta0 / (2 * z0)) * (z_index + z0)
    
    theta = math.atan(y_index / x_index)

    # if point in wrong hemisphere
    if x_index < 0 and y_index > 0:
        return False

    # determine if point in maximum angle
    if theta < -1 * maxTheta or theta > 0:
        return False
    else:
        return True
            

ax = plt.axes(projection="3d")


## generate 1000 points on the surface of unit sphere (radius=1)
# three random normal variables
x_data = np.random.normal(0, 1, points_count)
y_data = np.random.normal(0, 1, points_count)
z_data = np.random.normal(0, 1, points_count)

lamda = np.sqrt(x_data**2 + y_data**2 + z_data**2)

# (x, y, z) coordinate of 1000 points
x = x_data/lamda
y = y_data/lamda
z = z_data/lamda


## calculate number of points within certain region
antarctic_x = []
africa_x = []
antarctic_y = []
africa_y = []
antarctic_z = []
africa_z = []

antarctica_count = 0
africa_count = 0
for i in range(0, points_count):
    if inAntarctica(x[i], y[i], z[i]):
        antarctica_count += 1
        antarctic_x.append(x[i])
        antarctic_y.append(y[i])
        antarctic_z.append(z[i])

    if inAfrica(x[i], y[i], z[i]):
        africa_count += 1
        africa_x.append(x[i])
        africa_y.append(y[i])
        africa_z.append(z[i])

antarctica_prob = antarctica_count / points_count
africa_prob = africa_count / points_count

antarctica_area = earth_area * antarctica_prob
africa_area = earth_area * africa_prob


## print results
print("P(Points in Antarctic) =", antarctica_prob)
print("P(Points in Africa) =", africa_prob)

print("Estimated area of antarctica:", antarctica_area, "km^2")
print("Estimated area of africa:", africa_area, "km^2")


## plot the points
# ax.scatter(x, y, z)
# ax.scatter(antarctic_x, antarctic_y, antarctic_z, marker='p')
# ax.scatter(africa_x, africa_y, africa_z, marker='o')

# plt.show()
