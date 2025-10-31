import cv2 as cv

# Abrir camara con OpenCV

capture_camara = cv.VideoCapture(0)

while True:
    isTrue, frame = capture_camara.read()
    cv.imshow('Camara', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture_camara.release()
cv.destroyAllWindows()