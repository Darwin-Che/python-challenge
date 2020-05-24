import cv2
import numpy as np
im = cv2.imread("cave.jpg", 0)

ans = []
for i in range(len(im)):
    if (i % 2 == 1):
        ans = ans + [list(im[i][1::2])]
    else:
        ans = ans + [list(im[i][0::2])]

cv2.imwrite("my.png", np.asarray(ans, dtype=np.float))