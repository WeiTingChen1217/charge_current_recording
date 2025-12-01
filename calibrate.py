import cv2
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"({x}, {y}),")

img = cv2.imread("2025-12-01_11-02-00.jpg")  # 先放一張你螢幕截圖
cv2.imshow("click to get coord", img)
cv2.setMouseCallback("click to get coord", mouse_callback)
cv2.waitKey(0)