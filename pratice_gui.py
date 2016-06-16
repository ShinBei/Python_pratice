import tkinter as tk
import time
import webbrowser
from tkinter.filedialog import askopenfilename
import cv2

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        root.title("網路開啟")
        
        self.createWidgets()
        
    def OpenFile(self):
        name = askopenfilename(initialdir="C:/Users",
                               filetypes =(("PNG", "*.png"),("JPEG", "*.jpg"),("All Files","*.*")),
                               title = "Choose a file."
                               )
        print (name)
        #Using try in case user types in unknown file or closes without choosing a file.
        try:
            #with open(name,'r') as UseFile:
                #print(UseFile.read())
            im = cv2.imread('%s'%str(name))
            cv2.imshow('im', im)
            cv2.waitKey(0)
        except:
            print("No file exists")

    def createWidgets(self):
        self.Text_1 = tk.Label(self)
        self.Text_1["text"] = "輸入網址:"
        self.Text_1.grid(row=0, column=0)
        
        self.Text_2 = tk.Label(self)
        self.Text_2["text"] = "輸入菜單:"
        self.Text_2.grid(row=1, column=0)
        
        
        self.writeText_1 = tk.Entry(self)
        self.writeText_1["width"] = "50"
        self.writeText_1.grid(row=0, column=1)
        
        self.writeText_2 = tk.Entry(self)
        self.writeText_2["width"] = "50"
        self.writeText_2.grid(row=1, column=1)
        
        
        self.button_1 = tk.Button(self, text="Go" ,command=self.on_button)
        self.button_1.grid(row=0, column=2)
        
        self.button_2 = tk.Button(self, text="Insert" ,command=self.Insertitem)
        self.button_2.grid(row=2, column=0)
        
        self.button_3 = tk.Button(self, text="Remove" ,command=self.Remove)
        self.button_3.grid(row=2, column=1)
        
        
        self.meau = tk.Menu(self)
        filemenu = tk.Menu(self.meau, tearoff=0)
        self.meau.add_cascade(label="File", menu = filemenu)
        filemenu.add_command(label="Open", command = self.OpenFile)
        filemenu.add_command(label="Reset", command = self.Reset)
        self.meau.add_cascade(label="Exit", command = root.destroy)
        root.config(menu = self.meau)       
        
        
        self.list = tk.Listbox(self)
        self.list.grid(row=1, column=3)
        
        
        
        
        
        #self.QUIT.Append(first,"File")
        #self.QUIT.Append(second,"Edit")
        #self.QUIT = tk.Button(self, text="QUIT", command=root.destroy)
        #self.QUIT.grid(row=1, column=0)

    def on_button(self):
        #print(self.writeText_1.get())
        url = self.writeText_1.get()
        time.sleep(5) 
        webbrowser.open(url)
        
    def Insertitem(self):
        self.list.insert(0, self.writeText_2.get())
        self.writeText_2.delete(0, 'end')
        
    def Reset(self):
        self.writeText_1.delete(0, 'end')
        self.writeText_2.delete(0, 'end')
        self.list.delete(0, 'end')
        
    def Remove(self):
        self.list.delete(self.list.curselection())

root = tk.Tk()
app = Application(master=root)
app.mainloop()