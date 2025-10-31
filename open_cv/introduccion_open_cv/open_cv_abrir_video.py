import cv2 as cv

# Abrir vídeo con ruta relativa

capture_video = cv.VideoCapture('seccion_2/video/video1.mp4')

while True:
    isTrue, frame = capture_video.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture_video.release()
cv.destroyAllWindows()


