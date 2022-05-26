from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image Viewer thing")
root.geometry("500x500")
root.configure(bg="lightblue")

ImageLabel = Label(root, bg="white", highlightthickness=5, borderwidth=2)
ImageLabel.place(relx=0.5, rely =0.1, anchor=CENTER)

ImagePath = " "

def OpenImage():
    global ImagePath
    print("EA")
    ImagePath = filedialog.askopenfilename(title="Open Images", filetypes = (("Images","*.png", "*.jpg")))
    print("ImagePath")
    Img = ImageTk.PhotoImage(Image.open(ImagePath))
    ImageLabel["image"] = Img
    Img.close
    
def RotateImage():
    print("Games")
    
    
    
OpenButton = Button(root, text="Open Image", command=OpenImage)
OpenButton.place(relx = 0.4, rely = 0.4, anchor=CENTER)

RotateButton = Button(root,text="Rotate Image", command=RotateImage)
RotateButton.place(relx = 0.6, rely = 0.4, anchor=CENTER)


root.mainloop()