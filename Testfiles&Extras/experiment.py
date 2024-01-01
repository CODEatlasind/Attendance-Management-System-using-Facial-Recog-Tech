from deepface import DeepFace
import threading
from initial_Bound import *

print("Camera Access Initiated>>")
cap = cv.VideoCapture(0, cv.CAP_DSHOW)
print("Camera is being Accessed>>")

cap.set(cv.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 480)

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

face_database = 'face_database'
face_match = None
face_recon = None
files_List = set()


# files_List = []


def recon(frame, face_dir):
    global face_recon, face_match
    df = DeepFace.find(frame, face_dir, model[2], enforce_detection=False, silent=True)
    face_recon = df[0]['identity']
    face_match = face_verif(frame, face_recon)


def face_verif(frame, observed_img):
    try:
        if DeepFace.verify(frame, observed_img, model[2])['verified']:
            face_v = True
        else:
            face_v = False
    except ValueError:
        face_v = False

    return face_v


def analysis(video_cap, counter=0):
    global face_match, face_recon, files_List
    while True:
        ret, frame = video_cap.read()
        face_found = detect_bounding_box(frame)

        th = threading.Thread(target=recon, args=(frame, face_database,))

        if ret:
            if face_found:
                cv.putText(frame, "Face Detected!!", (20, 450), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
                if counter % 30 == 0:
                    try:
                        th.start()
                        th.join()
                    except KeyError or ValueError:
                        face_found = None

                    if face_recon is not None and face_match:
                        files_List.add(face_recon[14:-4])

            else:
                cv.putText(frame, "No Faces Found in the Feed", (20, 450), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1)
            counter += 1


            cv.imshow("Frame Output", frame)

        if cv.waitKey(1) == ord(' '):
            break

    cv.destroyWindow("Frame Output")
    print("Face Data Collected>>")
    return files_List


analysis(cap)
print(files_List)
