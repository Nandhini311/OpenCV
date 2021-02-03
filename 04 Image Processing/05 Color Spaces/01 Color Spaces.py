import cv2
import matplotlib.pyplot as plt


def show_with_matplotlib(color_img, title, pos):
    # Convert BGR image to RGB:
    img_RGB = color_img[:, :, ::-1]

    ax = plt.subplot(3, 6, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')



image = cv2.imread('color_spaces.png')

plt.figure(figsize=(12, 5))
plt.suptitle("Color spaces in OpenCV", fontsize=14, fontweight='bold')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

(bgr_b, bgr_g, bgr_r) = cv2.split(image)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
(hsv_h, hsv_s, hsv_v) = cv2.split(hsv_image)

hls_image = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
(hls_h, hls_l, hls_s) = cv2.split(hls_image)

ycrcb_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
(ycrcb_y, ycrcb_cr, ycrcb_cb) = cv2.split(ycrcb_image)

lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
(lab_l, lab_a, lab_b) = cv2.split(lab_image)


show_with_matplotlib(image, "BGR - image", 1)

show_with_matplotlib(cv2.cvtColor(gray_image, cv2.COLOR_GRAY2BGR), "gray image", 1 + 6)

show_with_matplotlib(cv2.cvtColor(bgr_b, cv2.COLOR_GRAY2BGR), "BGR - B comp", 2)
show_with_matplotlib(cv2.cvtColor(bgr_g, cv2.COLOR_GRAY2BGR), "BGR - G comp", 2 + 6)
show_with_matplotlib(cv2.cvtColor(bgr_r, cv2.COLOR_GRAY2BGR), "BGR - R comp", 2 + 6 * 2)

show_with_matplotlib(cv2.cvtColor(hsv_h, cv2.COLOR_GRAY2BGR), "HSV - H comp", 3)
show_with_matplotlib(cv2.cvtColor(hsv_s, cv2.COLOR_GRAY2BGR), "HSV - S comp", 3 + 6)
show_with_matplotlib(cv2.cvtColor(hsv_v, cv2.COLOR_GRAY2BGR), "HSV - V comp", 3 + 6 * 2)

show_with_matplotlib(cv2.cvtColor(hls_h, cv2.COLOR_GRAY2BGR), "HLS - H comp", 4)
show_with_matplotlib(cv2.cvtColor(hls_l, cv2.COLOR_GRAY2BGR), "HLS - L comp", 4 + 6)
show_with_matplotlib(cv2.cvtColor(hls_s, cv2.COLOR_GRAY2BGR), "HLS - S comp", 4 + 6 * 2)

show_with_matplotlib(cv2.cvtColor(ycrcb_y, cv2.COLOR_GRAY2BGR), "YCrCb - Y comp", 5)
show_with_matplotlib(cv2.cvtColor(ycrcb_cr, cv2.COLOR_GRAY2BGR), "YCrCb - Cr comp", 5 + 6)
show_with_matplotlib(cv2.cvtColor(ycrcb_cb, cv2.COLOR_GRAY2BGR), "YCrCb - Cb comp", 5 + 6 * 2)

show_with_matplotlib(cv2.cvtColor(lab_l, cv2.COLOR_GRAY2BGR), "L*a*b - L comp", 6)
show_with_matplotlib(cv2.cvtColor(lab_a, cv2.COLOR_GRAY2BGR), "L*a*b - a comp", 6 + 6)
show_with_matplotlib(cv2.cvtColor(lab_b, cv2.COLOR_GRAY2BGR), "L*a*b - b comp", 6 + 6 * 2)

plt.show()
