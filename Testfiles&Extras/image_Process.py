from deepface import DeepFace

import cv2 as cv
import threading

model = [
    "VGG-Face",
    "Facenet",
    "Facenet512",
    "OpenFace",
    "DeepFace",
    "DeepID",
    "ArcFace",
    "Dlib",
    "SFace",
]

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

img1_path = "db/img2.jpg"
reference_img = cv.imread(img1_path)


def recog_face(frames):
    global face_match
    try:
        if DeepFace.verify(frames,reference_img,model[2])['verified']:
            face_match = True
        else:
            face_match = False
    except ValueError:
        face_match = False


while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=recog_face, args=(frame,)).start()

            except ValueError:
                pass

        counter += 1

        if face_match:
            
        else:
            cv.putText(frame, "NO MATCH..", (20, 450), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)

        cv.imshow("Video", frame)

    if cv.waitKey(1) == ord('d'):
        break

cap.destroyAllWindows()

