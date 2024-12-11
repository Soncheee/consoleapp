from tkinter import *
from tkinter import font

root = Tk()

root['bg'] = "#fafafa"
root.title("Поиск книг по жанру")
root.wm_attributes('-alpha', 1.0)
root.geometry('800x500')

root.resizable(width=True, height=True)

canvas = Canvas(root, height=800, width=500)
canvas.pack()

frame = Frame(root, bg='darkseagreen')
frame.place(relwidth=1, relheight=1)

courier_font = font.Font(family="Courier", size=25, weight="bold")
search_input = Label(frame, text="Введите жанр книги", bg='hotpink', font=courier_font)
search_input.pack()


root.mainloop()



