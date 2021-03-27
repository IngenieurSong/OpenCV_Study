import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# set the size of video
# cap.set(3, 320)
# cap.set(4, 240)

def harrisCorner():
    while True:
        ret, frame = cap.read()
        if ret == True:
            # BGR->HSV로 변환
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # red 영역의 from ~ to (RGB)
            # 일부 얼굴까지 인식함. RGB 값 수정 필요
            lower_red = np.array([0, 100, 100])
            upper_red = np.array([10, 255, 255])

            # 이미지에서 blue영역
            mask = cv2.inRange(hsv, lower_red, upper_red) # range 범위 안에 들어오면 흰색으로 바꿈(ret)에서 1로 바꿔줌
            res = cv2.bitwise_and(frame, frame, mask=mask)
            cv2.imshow('Original', frame)
            cv2.imshow('res', res)

            gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
            # I don't know what exactly this function works
            # gray = np.float32(gray)

            # Find out all corner (Parameters mean?)
            dst = cv2.cornerHarris(gray, 5, 3, 0.04)

            res[dst > 0.4 * dst.max()] = [0, 255, 0]

            # Background removed and Harris Corner involved video
            cv2.imshow("res", res)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    harrisCorner()