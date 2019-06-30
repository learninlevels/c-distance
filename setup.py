import cv2
frame = cv2.imread("im.jpg")
counter = 0
x1 = 0
y1 = 0
def distance(x1,y1,x2,y2):
    d = ( (x1-x2)**2 + (y1-y2)**2 )**0.5
    return d
def draw_circle(event,x,y,flags,param):
    global counter, frame, x1, y1
    if event == cv2.EVENT_LBUTTONDBLCLK:
        counter = counter+1
        
        cv2.circle(frame,(x,y), 5 , (0,0,255), -1 )
        cv2.putText(frame , "x = "+str(x)+" , y = "+str(y), (x , y+20), cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0 , 0 , 0) )
        if (counter == 1 ):
            x1 = x
            y1 = y
        if (counter == 2 ):
            d =  distance(x1,y1,x,y)
            cv2.line(frame,(x1, y1),(x,y),(255,0,0),2)   
            cv2.putText(frame ,format(d , ".2f"),(int((x1 + x) / 2) , int((y1 + y) / 2) ) ,cv2.FONT_HERSHEY_SIMPLEX , 0.5 , (0,0,0))
        if (counter == 3): 
            counter = 0
            frame = cv2.imread("im.jpg")
cv2.namedWindow("im")
cv2.setMouseCallback("im", draw_circle) # param = Noneprint(d)
while(1):
    cv2.imshow("im" , frame)
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
cv2.destroyAllWindows()
