from cProfile import label
from tkinter import *
from PIL import Image, ImageTk
import imutils
import cv2
import numpy as np
from torch.distributed.elastic.timer import configure
from ultralytics import YOLO
import math

#scaning Function
def Scanning():

    if cap is not None:
        ret, frame = cap.read()
        #frame_show = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        if ret == True:

            #results = model(frame, stream=True, verbose=False)
            #for res in results:
                #boxes = res.boxes
                #for box in boxes:
                    #x1, y1, x2, y2 = box.xyxy[0]
                    #x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

                    #error
                    #if x1 < 0: x1 = 0
                    #if y1 < 0: y1 = 0
                    #if x2 < 0: x2 = 0
                    #if y2 < 0: y2 = 0

                    #clase
                    #cls = int(box.cls[0])

                    # Confidence
                    #conf = math.ceil(box.conf[0])

                    #if conf > 0.5:
                        #if cls == 0:
                            # Draw Rectamgle
                            #cv2.rectangle(frame_show, (x1,y1), (x2,y2), (255, 255, 0), 2)



            # resize
            frame = imutils.resize(frame, width = 640)
            # Convertir video
            im = Image.fromarray(frame)
            img= ImageTk.PhotoImage(image=im)

            #show
            lblvideo.image = img
            lblvideo.configure(image=img)
            lblvideo.after(10, Scanning)



        else:
            cap.release()



#ventana principal
def ventana_principal():
    global model, clsName, img_metal,  img_glass,  img_plastic,  img_carton, img_medical, lblvideo
    global  img_metaltxt, img_glasstxt, img_plastictxt, img_cartontxt, img_medical, cap

    pantalla = Tk()
    pantalla.title("RECICLAJE INTELIGENTE")
    pantalla.geometry("1280x720")

    #Backgraund

    imagenf = PhotoImage(file="setUp/Canva.png")
    background = Label(image=imagenf)
    background.place(x=0, y=0, relwidth =1, relheight =1)

    # Model
    model = YOLO ('Modelo/best.pt')

    clsName = ['Metal', 'Glass', 'Plastic', 'Carton', 'Medical']

    #img
    img_metal = cv2.imread("setUp/metal.png")
    img_glass = cv2.imread("setUp/vidrio.png")
    img_plastic = cv2.imread("setUp/plastico.png")
    img_carton = cv2.imread("setUp/carton.png")
    img_medical = cv2.imread("setUp/medical.png")
    img_metaltxt = cv2.imread("setUp/metaltxt.png")
    img_glasstxt = cv2.imread("setUp/vidriotxt.png")
    img_plastictxt = cv2.imread("setUp/plasticotxt.png")
    img_cartontxt = cv2.imread("setUp/cartontxt.png")
    img_medicaltxt = cv2.imread("setUp/medicaltxt.png")

    #label video
    lblvideo = Label(pantalla)
    lblvideo.place(x=319, y=118)

    #cam
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(3, 640)
    cap.set(4, 480)

    #escaner
    Scanning()

    # loop
    pantalla.mainloop()

if __name__ == '__main__':
    ventana_principal()

