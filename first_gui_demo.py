from msilib.schema import RadioButton
import tkinter as tk
import tkinter.ttk as ttk

class Window:
    def __init__(self,master):
        
        style=ttk.Style()
        # print(style.theme_names()) # to check the available themes
        style.theme_use("vista")

        style.theme_settings("vista",{
            "TButton" : {
                "configure" : {"padding" :20 },
                "map": {
                    "background" : [("active","red5"),
                                    ("!disabled","red5")],
                    "foreground" : [("focus","black"),
                                    ("active","black"),
                                    ("!disabled","black")] # text
                }
            }
        })

        Button=ttk.Button(master, text="Click Me!")
        Button.pack(padx=5,pady=5)

        label=ttk.Label(master, text="This is a label!")
        label.pack(padx=5,pady=15)

        checkbox=ttk.Combobox(master, values=["Option 1","Option 2"])
        checkbox.set("Option 1")
        checkbox.pack(padx=5,pady=5)


        radiobutton=ttk.Radiobutton(master,text="Radio Button")
        radiobutton.pack(padx=5, pady=5)

        checkbutton=ttk.Checkbutton(master, text="Check Button")
        checkbutton.pack(padx=5, pady=5)

        scale=ttk.Scale(master, from_=0,to=10)
        scale.pack(padx=5,pady=5)

        entry=ttk.Entry(master)
        entry.pack(padx=5,pady=5)



root=tk.Tk()
root.geometry('480x480')
window=Window(root)
root.mainloop()