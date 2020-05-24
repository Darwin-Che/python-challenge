import cv2
import numpy as np

im = cv2.imread("wire.png", 0)

ans = np.zeros([100,100])

bound = 0
x = 0
y = 0

# apparently it is easier to start aligning from the edges

for i in range(0, 10000):
    ans[x][y] = im[0][i]
    if x == bound:
        if y < 99 - bound:
            y = y + 1
            continue
    if y == 99 - bound:
        if x < 99 - bound:
            x = x + 1
            continue
    if x == 99 - bound:
        if y > bound:
            y = y - 1
            continue
    if y == bound:
        if x > bound + 1:
            x = x - 1
            continue
        if x == bound + 1:
            bound = bound + 1
            y = y + 1
            continue

cv2.imwrite("14.png", np.asarray(ans, dtype=np.float))
        
print(im[0])
print(ans[50][50])