import cv2
import time
import random
import dropbox

startTime = time.time()

def takesnapshot():
    videoCaptureObject = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    result = True
    number = random.randint(0, 100)

    while result:
        ret,frame = videoCaptureObject.read()
        imageName = "img"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        global startTime
        startTime = time.time()
        print(startTime)
        result = False
        
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return imageName

def uploadImage(imageName):
    access_token = "sl.A2VrhVjaP5DKX2vfxI0PnR20o5-sCAEuHUFLWB33rdp-DUfbidjBZUG4cYWZIXUL4EDLER5XD4q22Akj5tccqYwgDV1vd92Hd0oajNuX9ISJsAfKiC1VA3rVnV7sgMpo0t-_7x0"
    file_from = imageName
    file_to = "/Security/"+file_from

    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(), file_to, mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while True:
        print(str(time.time())+"current_time")
        print(str(startTime)+"start_time")
        print(str(time.time()-startTime)+"difference in time")

        if (time.time() - startTime >= 5):
            name = takesnapshot()
            uploadImage(name)

main()
