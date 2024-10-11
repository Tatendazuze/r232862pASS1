import math
Ys = float(input('enter Y coordinate for S in meters:'))
Yt = float(input('enter Y coordinate for T in meters:'))
Dy = Yt-Ys
print(Dy)
Xs = float(input('enter X coordinate for S in meters:'))
Xt = float(input('enter X coordinate for T in meters:'))
Dx = Xt-Xs
print(Dx)
distance_r = math.sqrt(Dx**2+Dy**2)
print(distance_r)
direction_s=math.degrees(math.atan(Dy/Dx))
print(direction_s)
quadrant_1=direction_s
quadrant_2=180-direction_s
quadrant_3=180+direction_s
quadrant_4=360-direction_s
if Dx>0 and Dy>0:
    print(f"join ST: {distance_r} m, {quadrant_1} degrees")
elif Dx<0 and Dy>0:
    print(f"join ST: {distance_r} m, {quadrant_2} degrees")
if Dx<0 and Dy<0:
    print(f"join ST: {distance_r} m, {quadrant_4} degrees")
elif Dx>0 and Dy<0:
    print(f"join ST: {distance_r} m, {quadrant_3} degress")