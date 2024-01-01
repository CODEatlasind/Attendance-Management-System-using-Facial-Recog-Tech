from deepface import DeepFace
import threading
from initial_Bound import *

cap = cv.VideoCapture(0, cv.CAP_DSHOW)
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
face_match = False
face_recon = None
files_List = set()
Disp = 0



def recon(frame, face_dir):
    global face_recon, face_match
    df = DeepFace.find(frame, face_dir, model[2], enforce_detection=False, silent=True)
    face_recon = df[0]['identity'][0]
    face_match = face_verif(frame, face_recon)


def face_verif(frame, observed_img):
    try:
        if DeepFace.verify(frame, observed_img, model[2])['verified']:
            cv.putText(frame, "Face Detected!!", (250, 450), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 255, 0), 1)
            face_v = True
        else:
            face_v = False
    except ValueError:
        face_v = False

    return face_v


def analysis(video_cap, counter=0):
    global face_match, face_recon, files_List
    if video_cap.read()[0] is True:
        print("Camera Access Successful!!")
    while True:
        ret, frame = video_cap.read()
        face_found = detect_bounding_box(frame)

        th = threading.Thread(target=recon, args=(frame, face_database,))

        if ret:
            if face_found:
                cv.putText(frame, "Face Found!!", (20, 450), cv.FONT_HERSHEY_TRIPLEX, 0.5, (0, 204, 204), 1)
                if counter % 30 == 0:
                    try:
                        th.start()
                        th.join()
                    except KeyError or ValueError:
                        pass

                    if face_match:
                        files_List.add(face_recon)
                        c = 1
            else:
                cv.putText(frame, "No Feed Detected", (20, 450), cv.FONT_HERSHEY_TRIPLEX, 0.5, (46, 46, 255), 1)
                face_recon = None
                c = 0

            counter += 1
            cv.imshow("Frame Output", frame)

        if cv.waitKey(1) == ord(' '):
            break

    cv.destroyWindow("Frame Output")
    print("Face Data Collected>>")
    return files_List

# test commands for this function
# analysis(cap)
# print(files_List)
