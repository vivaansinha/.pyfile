import webbrowser
from tkinter import *
import webbrowser
def important():
    x = input("username ")
    print(f"hi {x}")
    while True:
        z = input()
        if z == "start":
            aa = input("what link ")
            webbrowser.open_new_tab(aa)
window = Tk()
button = Button(window, text="sign in",command=important)
button.pack()
window.geometry("850x666")




window.mainloop()

print('success')












































