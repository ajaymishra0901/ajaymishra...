from tkinter import*
root = Tk()
v = IntVar()
v.set(0)
lang_list = [("Python", 0), ("java", 1), ("C", 2), ("DOTnET", 3), ("PHP", 4)]


def ShowChoice():
    print("hey, your selected choioce is:", v.get())
l = Label(root, text="Select Your Favourite Programming Language:")
l.pack()
for txt, val in lang_list:
    r = Radiobutton(root, text=txt, variable=v, command=ShowChoice, value=val)
    r.pack()
