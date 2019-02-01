import cv2, time

video=cv2.VideoCapture("Sample.mp4")
# video=cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    print(check)
    print(frame)

    # time.sleep(3)
    cv2.imshow("capturing", frame)

    stop_key=cv2.waitKey(10)
    if stop_key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()