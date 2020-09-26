
# Author: itzAamir
# Date: 26th Sept 2020

from tkinter import Label, StringVar, Entry, Button, mainloop, Tk, Menu, HORIZONTAL
from tkinter.ttk import Progressbar
from tkinter import simpledialog, messagebox
import pytube

# Basic Necessities
root = Tk()
root.geometry("750x700")
root.title("YT Downloader")

# Functions

def about():
    messagebox.showinfo("Contact Us", "Contact us on Social Media For any Query.\n\nInstagram: ItzAamir\n\nEmail: amirpc190320@gmail.com")

def help():
    messagebox.showinfo("Information", "For any difficulty, Please refer to readMe document provided with this file.\n\nIn case you didn't got the readMe file Contact Us.")

def popup():
    messagebox.showinfo("Downloaded","Your File has been downloaded.\n\nYou didn't see the progress animation of downloading a video, Obviously because of the laziness of developer.\n\nEnjoy xD")

def download():
    try:
        yt_url = url_var.get()
        youtube = pytube.YouTube(yt_url)
        streams = youtube.streams.all()
        # print(len(streams))
        stream_label1.set(streams[0])
        stream_label_var1.update()
        stream_label2.set(streams[1])
        stream_label_var2.update()
        stream_label3.set(streams[2])
        stream_label_var3.update()
        stream_label4.set(streams[3])
        stream_label_var4.update()
        stream_label5.set(streams[4])
        stream_label_var5.update()
        stream_label6.set(streams[5])
        stream_label_var6.update()
        stream_label7.set(streams[6])
        stream_label_var7.update()
        stream_label8.set(streams[7])
        stream_label_var8.update()
        stream_label9.set(streams[8])
        stream_label_var9.update()
        stream_label10.set(streams[9])
        stream_label_var10.update()
        stream_label11.set(streams[10])
        stream_label_var11.update()
        stream_label12.set(streams[11])
        stream_label_var12.update()
        stream_label13.set(streams[12])
        stream_label_var13.update()
        stream_label14.set(streams[13])
        stream_label_var14.update()
        stream_label15.set(streams[14])
        stream_label_var15.update()
        stream_label16.set(streams[15])
        stream_label_var16.update()

        itag = simpledialog.askinteger("stream", "Enter the itag")
        video = youtube.streams.get_by_itag(itag)
        video.download(r"C:\Users\NC 67\Downloads\Yt Downloads")
        popup()

    except Exception as e:
        messagebox.showwarning("Error",f"Unable to donwload the video because \n{e}")


# Menubar
menubar = Menu(root)  
file = Menu(menubar, tearoff= 0)
file.add_command(label= "Exit", command= root.quit)
menubar.add_cascade(label="File", menu=file) 

info = Menu(menubar, tearoff= 0)
info.add_command(label= "Help", command= help)
info.add_command(label= "About", command= about)
menubar.add_cascade(label= "Information", menu= info)
root.config(menu=menubar)

# Interface
Label(root, text= "Youtube Video/Audio Downloader", font=("comic sans ms", 23, "bold"), fg= "#ff0800").pack(pady= 40)

url_var = StringVar()
urlLabel = Label(root, text= "Paste Url: ").pack()
url = Entry(urlLabel, textvariable=url_var, font=("", 10, ""), width=50)
url.pack(ipady=4)

Button(root, text= "Download", bg= "#ff0800", fg= "white", font=("comic sans ms", 10, ""), command= download).pack(pady= 10)

# unable to use loops, so I hard coded this set of lines
stream_label1 = StringVar()
stream_label2 = StringVar()
stream_label3 = StringVar()
stream_label4 = StringVar()
stream_label5 = StringVar()
stream_label6 = StringVar()
stream_label7 = StringVar()
stream_label8 = StringVar()
stream_label9 = StringVar()
stream_label10 = StringVar()
stream_label11 = StringVar()
stream_label12 = StringVar()
stream_label13 = StringVar()
stream_label14 = StringVar()
stream_label15 = StringVar()
stream_label16 = StringVar()
stream_label17 = StringVar()
stream_label_var1 = Label(root, textvariable= stream_label1,font= ("", 8, "") )
stream_label_var1.pack()
stream_label_var2 = Label(root, textvariable= stream_label2,font= ("", 8, "") )
stream_label_var2.pack()
stream_label_var3 = Label(root, textvariable= stream_label3,font= ("", 8, "") )
stream_label_var3.pack()
stream_label_var4 = Label(root, textvariable= stream_label4,font= ("", 8, "") )
stream_label_var4.pack()
stream_label_var5 = Label(root, textvariable= stream_label5,font= ("", 8, "") )
stream_label_var5.pack()
stream_label_var6 = Label(root, textvariable= stream_label6,font= ("", 8, "") )
stream_label_var6.pack()
stream_label_var7 = Label(root, textvariable= stream_label7,font= ("", 8, "") )
stream_label_var7.pack()
stream_label_var8 = Label(root, textvariable= stream_label8,font= ("", 8, "") )
stream_label_var8.pack()
stream_label_var9 = Label(root, textvariable= stream_label9,font= ("", 8, "") )
stream_label_var9.pack()
stream_label_var10 = Label(root, textvariable= stream_label10,font= ("", 8, "") )
stream_label_var10.pack()
stream_label_var11 = Label(root, textvariable= stream_label11,font= ("", 8, "") )
stream_label_var11.pack()
stream_label_var12 = Label(root, textvariable= stream_label12,font= ("", 8, "") )
stream_label_var12.pack()
stream_label_var13 = Label(root, textvariable= stream_label3,font= ("", 8, "") )
stream_label_var13.pack()
stream_label_var14 = Label(root, textvariable= stream_label4,font= ("", 8, "") )
stream_label_var14.pack()
stream_label_var15 = Label(root, textvariable= stream_label5,font= ("", 8, "") )
stream_label_var15.pack()
stream_label_var16 = Label(root, textvariable= stream_label6,font= ("", 8, "") )
stream_label_var16.pack()
stream_label_var17 = Label(root, textvariable= stream_label7,font= ("", 8, "") )
stream_label_var17.pack()


root.mainloop()
