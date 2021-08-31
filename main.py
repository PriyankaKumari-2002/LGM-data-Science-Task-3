import cv2
#img_loc='Image to pencil sketch/'

''' process to convert to pencil image:

img ->pencil_sketch=gray ->inverted->blur->invert_blur->
divide(gray,invert_blur)=pencil_sketch

'''
file_name='Priyanka pic.jpeg'
img=cv2.imread(  file_name)
resize=cv2.resize(img,(500,800))
gray=cv2.cvtColor(resize,cv2.COLOR_BGR2GRAY)
invert_gray=255-gray
blur=cv2.GaussianBlur(invert_gray,(21,21),0)
invert_blur=255-blur
pencil_sketch=cv2.divide(gray, invert_blur,scale=250.0)
cv2.imshow('Original Image',resize)
#resize1=cv2.resize(gray,(400,600))
#cv2.imshow('GrayImage',invert_gray)
#cv2.imshow('GrayImage',invert_blur)
cv2.imshow('Pencil Sketch',pencil_sketch)
cv2.imwrite('Image to pencil sketch/saved/'+file_name,pencil_sketch)

cv2.waitKey(0)
