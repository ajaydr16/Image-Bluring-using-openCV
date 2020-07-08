import cv2
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

fc = cv2.CascadeClassifier('train.xml')

img = cv2.imread(file_path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

f = fc.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in f:
    img[y:(y + h), x:(x + w)] = cv2.blur(img[y:(y + h), x:(x + w)], (25, 25))

cv2.imshow('img', img)
cv2.waitKey()