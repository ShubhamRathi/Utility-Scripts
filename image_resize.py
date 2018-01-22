from PIL import Image
import os

for f in os.listdir("./Images"):
    img = Image.open("./Images/"+f)
    new_img = img.resize((1080,720))
    new_img.save("New/"+f+".jpg", "JPEG", optimize=False)
