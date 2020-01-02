from PIL import Image, ImageTk
import tkinter
import os

base_path = 'NY_corp_test'
suitable_path = 'suitable_dir'#left
unsuitable_path = 'unsuitable_dir'#right
image_list = os.listdir('NY_corp_test')
current = 0
photo_num = 0

def move(Rd):
    global current, image_list,photo_num
    if not (0 <= current + Rd < len(image_list)):
        return
    current += Rd
    photo_num += Rd
    image = Image.open(os.path.join(base_path,image_list[current]))
    photo = ImageTk.PhotoImage(image.resize((720,640)))
def next_img(event):
    global current, image_list,photo_num
    #if not (0 <= current + 1 < len(image_list)):
        #return
    
    current += 1
    photo_num += 1
    
    if (photo_num>=len(image_list)):
        label['text'] = 'This was we last photo'
        return
        
    image = Image.open(os.path.join(base_path,image_list[current]))
    photo = ImageTk.PhotoImage(image.resize((720,640)))
    label['text'] = str(photo_num)
    label['image'] = photo
    label.photo = photo

def leftKey(event):
    global current, image_list,photo_num
    image = Image.open(os.path.join(base_path,image_list[current]))
    image.save(suitable_path+'/'+image_list[current])
    print ("Left key pressed")

def rightKey(event):
    global current, image_list,photo_num
    image = Image.open(os.path.join(base_path,image_list[current]))
    image.save(unsuitable_path+'/'+image_list[current])
    print ("Right key pressed")
    
def main():
    def move(Rd):
        global current, image_list,photo_num
        if not (0 <= current + Rd < len(image_list)):
            return
        current += Rd
        photo_num += Rd
        image = Image.open(os.path.join(base_path,image_list[current]))
        photo = ImageTk.PhotoImage(image.resize((720,640)))

    def next_img(event):
        global current, image_list,photo_num
        #if not (0 <= current + 1 < len(image_list)):
            #return
        
        current += 1
        photo_num += 1
        
        if (photo_num>=len(image_list)):
            label['text'] = 'This was we last photo'
            return
        
        image = Image.open(os.path.join(base_path,image_list[current]))
        photo = ImageTk.PhotoImage(image.resize((720,640)))
        label['text'] = str(photo_num)
        label['image'] = photo
        label.photo = photo

    def leftKey(event):
        global current, image_list,photo_num
        image = Image.open(os.path.join(base_path,image_list[current]))
        image.save(suitable_path+'/'+image_list[current])
        print ("Left key pressed")

    def rightKey(event):
        global current, image_list,photo_num
        image = Image.open(os.path.join(base_path,image_list[current]))
        image.save(unsuitable_path+'/'+image_list[current])
        print ("Right key pressed")
#Importing Photos

##    base_path = 'NY_corp_test'
##    suitable_path = 'suitable_dir'#left
#    unsuitable_path = 'unsuitable_dir'#right

    if (not os.path.exists(suitable_path)):
        os.mkdir(suitable_path)
    if (not os.path.exists(unsuitable_path)):
        os.mkdir(unsuitable_path)

#    image_list = os.listdir('NY_corp_test')

 #   current = 0
 #   photo_num = 0

    root = tkinter.Tk()
    label = tkinter.Label(root, compound=tkinter.TOP)
    label.pack()

    frame = tkinter.Frame(root)
    frame.pack()

    root.bind('<Return>',next_img)
    root.bind('<Left>', leftKey)
    root.bind('<Right>', rightKey)
    tkinter.Button(frame, text='Previous picture', command=lambda: move(-1)).pack(side=tkinter.LEFT)
    tkinter.Button(frame, text='Next picture', command=lambda: move(+1)).pack(side=tkinter.LEFT)
    tkinter.Button(frame, text='Quit', command=root.quit).pack(side=tkinter.LEFT)

    root.mainloop()
    
if __name__== "__main__":
   main()