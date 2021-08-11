import tkinter as tk
import hashlib as hash


def calculation():
    s = string.get()
    ss = sstring.get()
    hs = hash.md5(s.encode()).hexdigest()
    dhs = hash.md5(hs.encode()).hexdigest()

    result = "string = {}\n" \
             "hash = {}\n" \
             "dublehash = {}\n".format(s, hs, dhs)

    labelResults["text"] = result

    shs = hash.md5(ss.encode()).hexdigest()
    sshs = hash.md5(shs.encode()).hexdigest()

    sresult = "string = {}\n" \
             "hash = {}\n" \
             "dublehash = {}\n".format(ss, shs, sshs)
    labelResult["text"] = sresult

    if dhs == sshs:
        re = "{}".format("Matching")
        labelR["text"] = re
    else:
        ren = "{}".format("Not Matching")
        labelR["text"] = ren

win = tk.Tk()
win.title("Calculation")
win.geometry("600x400")

labelfirst = tk.Label(win, text="Password")
labelfirst.pack()

string = tk.Entry(win, width=50)
string.pack()

labelSecond = tk.Label(win, text="Password")
labelSecond.pack()

sstring = tk.Entry(win, width=50)
sstring.pack()

labelResults = tk.Label(win, text="-----")
labelResults.pack()
labelResult = tk.Label(win, text="-----")
labelResult.pack()

labelMatch = tk.Label(win, text="#####Password Match#####")
labelMatch.pack()

labelR = tk.Label(win, text="-----")
labelR.pack()

kmbutton = tk.Button(win, text="Change", repeatdelay=500, repeatinterval=1000)
kmbutton["command"] = calculation
kmbutton.pack()

win.mainloop()

