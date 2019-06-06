import tkinter
import tkinter.messagebox

def main():
    flag = True

    def change_lable_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'Hello, World') if flag else ('blue', 'Goodbye, World')
        label.config(text=msg, fg=color)

    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('Warning', 'Are you sure to quit'):
            top.quit()

    top = tkinter.Tk()

    top.geometry('240x160')

    top.title('Little Game')

    label = tkinter.Label(top, text='Hell o', font='Arial-32', fg='yellow')
    label.pack(expand=1)

    panel = tkinter.Frame(top)

    button1 = tkinter.Button(panel, text='Edit', command=change_lable_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='Quit', command=confirm_to_quit)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()

if __name__ == "__main__":
    main()
