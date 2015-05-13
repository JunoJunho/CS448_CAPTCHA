from Tkinter import *
from tkFileDialog import askopenfilenames
from PIL import ImageTk, Image
from CaptchaLibrary.CHARACTERIZER.INITIALIZATION import INITIALIZATION
from CaptchaLibrary.CHARACTERIZER.CHARACTERIZER import CHARACTERIZER as Guesser
import sys

sys.path.append('./CaptchaLibrary')


class TkFileDialog(Frame):

    init_theta1, init_theta2 = INITIALIZATION('./CaptchaLibrary/nn_params.txt')
    target_captcha = []
    index = -1
    total_try = 0
    num_success = 0

    def __init__(self, root):
        Frame.__init__(self, root)

        self.parent = root
        self.parent.title("Captcha Breaker")

        self.file_opt = options = {}
        options['filetypes'] = [('all files', '.*'), ('text files', '.txt')]
        options['parent'] = root

        Button(self, text='Open File', command=self.askopenfile).grid(row=0, column=0, padx=5, pady=5)
        Button(self, text='Break Captcha', command=self.handle_captcha_file).grid(row=1, column=0, padx=5, pady=5)
        Button(self, text="next", command=self.next).grid(row=2, column=0, padx=5, pady=5)
        self.captcha_image = Image.new("RGB", (200, 56), "white")
        self.image_viewer = ImageTk.PhotoImage(self.captcha_image)
        label1 = Label(self, image=self.image_viewer)
        label1.grid(row=0, column=1, padx=5, pady=5)

        self.predict_str = StringVar()
        label2 = Label(self, textvariable=self.predict_str)
        label2.grid(row=1, column=1, padx=5, pady=5)

        Label(self, text="Accuracy").grid(row=0, column=2, padx=5, pady=5)
        self.accuracy_of_file = StringVar()
        self.percentage_label = Label(self, textvariable=self.accuracy_of_file, width=7)
        self.percentage_label.grid(row=1, column=2, padx=5, pady=5)

    def askopenfile(self):
        if self.index == len(self.target_captcha):
            return
        filename = askopenfilenames(**self.file_opt)
        for each in filename:
            self.target_captcha.append(each)

    def handle_captcha_file(self):
        guess_string = Guesser(self.init_theta1, self.init_theta2, self.target_captcha[self.index])
        self.predict_str.set(guess_string)
        self.total_try += 1
        if guess_string == self.target_captcha[self.index].split('/')[-1].split('.')[0]:
            self.num_success += 1
        self.accuracy_of_file.set(
            str(round((float(self.num_success) / float(self.total_try)), 3) * 100))

    def next(self):
        self.index += 1
        self.predict_str.set("")
        self.captcha_image = Image.open(self.target_captcha[self.index])
        self.image_viewer.paste(self.captcha_image)

if __name__ == '__main__':
    root = Tk()
    TkFileDialog(root).pack()
    root.mainloop()