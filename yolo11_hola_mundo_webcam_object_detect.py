from ultralytics import YOLO
import cv2

# Cargar webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # ancho
cap.set(4, 720)   # alto

# Cargar modelo YOLO
model = YOLO('yolo11n.pt')

while True:
    success, img = cap.read()
    if not success:
        print("No se pudo acceder a la cámara")
        break

    # Procesar la imagen con YOLO
    results = model(img, stream=True)

    # Iterar sobre las detecciones
    for r in results:
        annotated_frame = r.plot()
        cv2.imshow("YOLOv8 Webcam", annotated_frame)

    # Salir con la tecla Enter (código 13)
    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()
