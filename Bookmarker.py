# PYTHON BOOKMARKER APP

from tkinter import *
from webbrowser import *

HEIGHT = 500
WIDTH = 500

URL = "https://www.python.jp/"

# Event Handler Function: Home
def open_home(event):
    open_new_tab(URL)

# Event Handler Function: News & Events
def open_news(event):
    open_new_tab(URL + "/news")

# Event Handler Function: Recruitment
def open_recruit(event):
    open_new_tab(URL + "/jobboard")

# Event Handler Function: Exit
def close_window(event):
    app.destroy()

app = Tk()

app.title("Bookmarker")
app.iconbitmap(r"bookmark_icon.ico")

# SCREEN SIZE SETTING
canvas = Canvas(app, height = HEIGHT, width = WIDTH)

# FRAME CREATION
frame = Frame(app, bg = "#F0F0F0")

# CENTER BOX FRAME
frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
# frame.place(anchor = 'n', relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
# frame.place(relwidth = 1, relheight = 1)

# LABEL SETTING
about_label = Label(frame, text = "Python ブックマークアプリ", bg = "#F0F0F0", font = "Arial 20 bold")
# about_label.pack(side = "right", fill = "both", expand = "True")
about_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)
# about_label.grid(row = 0, column = 1)

# HOME BUTTON SETTING
home_button = Button(frame, text = "Python ホーム", bg = "blue", fg = "#fff")
# home_button.pack(side = "left", fill = 'x', expand = "True")
home_button.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.1)
# button.grid(row = 0, column = 0)

# NEWS BUTTON SETTING
news_button = Button(frame, text = "ニュース・エベント", bg = "blue", fg = "#fff")
news_button.place(relx = 0, rely = 0.4, relwidth = 1, relheight = 0.1)

# RECRUIT BUTTON SETTING
recruit_button = Button(frame, text = "採用情報", bg = "blue", fg = "#fff")
recruit_button.place(relx = 0, rely = 0.6, relwidth = 1, relheight = 0.1)

# EXIT BUTTON SETTING
exit_button = Button(frame, text = "Exit APP", bg = "blue", fg = "#fff")
exit_button.place(relx = 0, rely = 0.8, relwidth = 1, relheight = 0.1)

# TEXT BOX
# entry = Entry(frame)
# entry.pack()

# BUTTON ACTIONS
home_button.bind("<Button-1>", open_home)
news_button.bind("<Button-1>", open_news)
recruit_button.bind("<Button-1>", open_recruit)
exit_button.bind("<Button-1>", close_window)

canvas.pack()

# app.geometry("300x300")

app.mainloop()
