import cv2

cap = cv2.VideoCapture('/Users/kartiktripathi/PycharmProjects/PoseEstimationProject/PoseVideos/1.mp4')

while True:
    success, img = cap.read()

    cv2.imshow("Image", img)
    cv2.waitKey(1)