from PIL import Image
import numpy as np

x_len = 101
y_len = 103

file = open("input.txt", "r").readlines()

ans1 = 0
ans2 = 0

# PART 1
quads = [0, 0, 0, 0]
for f in file:
    p, v = f.split(" ")
    p = list(map(int, p[2:].split(",")))
    v = list(map(int, v[2:].split(",")))
    p[1] = (p[1] + v[1] * 100) % y_len
    p[0] = (p[0] + v[0] * 100) % x_len

    if p[0] < (x_len-1)/2 and p[1] < (y_len-1)/2: quads[0] += 1
    elif p[0] < (x_len-1)/2 and p[1] > (y_len-1)/2: quads[1] += 1
    elif p[0] > (x_len-1)/2 and p[1] < (y_len-1)/2: quads[2] += 1
    elif p[0] > (x_len-1)/2 and p[1] > (y_len-1)/2: quads[3] += 1

ans1 = quads[0] * quads[1] * quads[2] * quads[3]


# for a in range(x_len*y_len):
# answer after manually searching through all images because wtf does a christmas tree look like in this context
ans2 = 7672
canvas = np.zeros((x_len, y_len))
for f in file:
    p, v = f.split(" ")
    p = list(map(int, p[2:].split(",")))
    v = list(map(int, v[2:].split(",")))
    p[1] = (p[1] + v[1]*ans2) % y_len
    p[0] = (p[0] + v[0]*ans2) % x_len
    canvas[p[0]][p[1]] = 255
image = Image.fromarray(canvas.transpose())
image = image.convert("L")
image.save(f"{ans2}-seconds.png")

print("PART 1", ans1)
print("PART 2", ans2)

