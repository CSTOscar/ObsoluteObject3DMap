import numpy as np
import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('cv_image/image0.JPG', 0)  # queryImage
img2 = cv2.imread('cv_image/image1.JPG', 0)  # trainImage

orb = cv2.ORB_create()
# find the keypoints and descriptors with ORB
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

for i in range(len(kp1)):
    k1 = kp1[i]
    k2 = kp2[i]
    print(k1.pt, k2.pt)

print(kp1[0].pt)
print(des1.shape)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# Match descriptors.
matches = bf.match(des1, des2)

# Sort them in the order of their distance.
matches = sorted(matches, key=lambda x: x.distance)
print([str(mat) for mat in matches])

# Draw first 10 matches.
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:20], flags=2, outImg=None)
plt.imshow(img3), plt.show()

stereo = cv2.StereoBM_create(numDisparities=32, blockSize=15)
disparity = stereo.compute(img1, img2)
# plt.imshow(disparity, 'gray')
# plt.show()
