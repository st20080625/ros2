import numpy as np
import matplotlib.pyplot as plt

Points = [np.array([-0.990066, -0.502765]), np.array([-0.946230, -0.449131]), np.array([-0.923050, -0.463866]),
    np.array([-0.845967, -0.423427]), np.array([-0.846124, -0.407516]), np.array([-0.794727, -0.360431]),
    np.array([-0.783218, -0.348086]), np.array([-0.727840, -0.319847]), np.array([-0.723345, -0.327545]),
    np.array([-0.664758, -0.271922]), np.array([-0.652772, -0.269313]), np.array([-0.611586, -0.217798]),
    np.array([-0.580298, -0.223027]), np.array([-0.555132, -0.169916]), np.array([-0.507548, -0.171740]),
    np.array([-0.484088, -0.152736]), np.array([-0.450418, -0.120520]), np.array([-0.404360, -0.106692]),
    np.array([-0.374848, -0.072905]), np.array([-0.339986, -0.065370]), np.array([-0.308692, -0.033436]),
    np.array([-0.261322, -0.013986]), np.array([-0.232925, 0.018149]), np.array([-0.197544, 0.033949]),
    np.array([-0.167206, 0.061422]), np.array([-0.127771, 0.087433]), np.array([-0.100848, 0.112879]),
    np.array([-0.058377, 0.126223]), np.array([-0.034330, 0.152678]), np.array([0.009517, 0.172289]),
    np.array([0.037507, 0.194863]), np.array([0.074056, 0.215773]), np.array([0.102762, 0.243694]),
    np.array([0.143857, 0.256642]), np.array([0.179043, 0.279898]), np.array([0.207044, 0.296611]),
    np.array([0.250845, 0.326826]), np.array([0.285383, 0.339882]), np.array([0.313045, 0.368843]),
    np.array([0.353731, 0.377079]), np.array([0.387503, 0.406056]), np.array([0.414120, 0.421939]),
    np.array([0.454254, 0.454354]), np.array([0.489371, 0.464529]), np.array([0.520586, 0.487899]),
    np.array([0.564335, 0.511315]), np.array([0.593220, 0.527446]), np.array([0.627013, 0.556547]),
    np.array([0.665273, 0.565593]), np.array([0.694222, 0.593949]), np.array([0.729257, 0.617268]),
    np.array([0.827804, 0.849781]), np.array([0.881833, 0.799575]), np.array([0.921831, 0.824033]),
    np.array([0.941507, 0.811238]), np.array([1.001164, 0.777141])]

Rotated_Points = []

def MakeAffine(Vec2, Theta, Displacement):
    Affine = np.array([[np.cos(Theta), -np.sin(Theta), Displacement[0]],
                       [np.sin(Theta),  np.cos(Theta), Displacement[1]],
                       [0,              0,             1]])
    Vec3 = np.array([Vec2[0], Vec2[1], 1])
    Rotated_Vec3 = Affine @ Vec3
    return np.array([Rotated_Vec3[0], Rotated_Vec3[1]])

def matching(last_scan, current_scan):
    box_size = 0.01
    min_x, min_y = 0
    max_x, max_y = 0
    grid = []
    for i in range(len(current_scan)):
        if i == 0:
            min_x = current_scan[0][0]
            min_y = current_scan[0][1]
            max_x = current_scan[0][0]
            max_y = current_scan[0][1]
        if min_x > current_scan[i][0]:
            min_x = current_scan[i][0]
        if min_y > current_scan[i][1]:
            min_y = current_scan[i][1]
        if max_x < current_scan[i][0]:
            max_x = current_scan[i][0]
        if max_y < current_scan[i][1]:
            max_y = current_scan[i][1]

    width = max_x - min_x
    height = max_y - min_y

    for i in range(int(width / box_size)):
        grid.append([])
        for j in range(int(height / box_size)):
            grid[i].append(0)


for i in range(len(Points)):
    Rotated_Points.append(MakeAffine(Points[i], np.pi/6, np.array([0, 0])))

#print(Rotated_Points)

xs = [p[0] for p in Points]
ys = [p[1] for p in Points]
rot_xs = [r_p[0] for r_p in Rotated_Points]
rot_ys = [r_p[1] for r_p in Rotated_Points]

plt.plot(xs, ys, 'o')
plt.plot(rot_xs, rot_ys, 'x')
plt.show()
