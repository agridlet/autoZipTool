from tkinter import *
from tkinter import filedialog
from subprocess import Popen
from autoZip import zip_file

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path_transit
    global folder_path_model_webgl
    filename = filedialog.askdirectory()
    folder_path_transit.set(filename)
    print(filename)

    filename_webgl = filedialog.askdirectory()
    folder_path_model_webgl.set(filename_webgl)
    print(filename_webgl)

def start():
    import os
#    os.system("python test.py")
    global folder_path_transit
    global folder_path_model_webgl
    zip_file(folder_path_transit.get(), folder_path_model_webgl.get())

# ma premiere fenetre
window = Tk()
folder_path_transit = StringVar()
folder_path_model_webgl = StringVar()
print(folder_path_transit)
print(folder_path_model_webgl)

lbl1 = Label(master=window, textvariable=folder_path_transit)
lbl1.grid(row=0, column=1)

lbl12 = Label(master=window, textvariable=folder_path_model_webgl)
lbl12.grid(row=1, column=1)

button2 = Button(text="transit directory", command=browse_button)
button2.grid(row=0, column=3)

button3 = Button(text="webgl directory", command=browse_button)
button3.grid(row=1, column=3)

start = Button(text="ZIP", command=start)
start.grid(row=2, column=3)

# personnaliser cette fenetre
window.title("Auto Export Zip by GerbilDindon")
# window.geometry("512x256")

# ajout de text
label_title_from_max = Label(window, text="Chemin d'accès vers le dossier d'export 3ds")
# label_title_from_max.pack()

label_title_to_webglviewer = Label(window, text="Chemin d'accès vers le dossier model du webgl viewer")
# label_title_to_webglviewer.pack()

label_title_to_save_directory = Label(window, text="Chemin d'accès vers le dossier de sauvegarde du zip")
# label_title_to_save_directory.pack()



# afficher la fenetre
window.mainloop()



