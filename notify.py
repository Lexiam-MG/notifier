# install tkinter, PIL, ImageTk(sudo apt-get install python3-pil.imagetk)

import tkinter as tk
from PIL import Image, ImageTk


class notify(tk.Tk):

    def __init__(self, title="notify", description="description", image=None,
                 color="#000000", show_time=2000, place="right-top"):
        super().__init__()
        self.title = title
        self.description = description
        self.image = image
        self.color = color
        self.show_time = show_time
        self.place = place

        self.get_screen_window_size()
        self.set_place()
        self.render()

    def render(self):
        self.after(2000, self.destroy)
        self.overrideredirect(1)
        self.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.place_x, self.place_y))
        self.configure(background=self.color)

        self.canvas = tk.Canvas(self, width = self.window_width, height = self.window_height,
                                highlightthickness=0)
        self.canvas.configure(background=self.color)
        self.canvas.pack()

        self.img = Image.open(self.image)
        self.img = self.img.resize((self.window_height, self.window_height), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.img)


        # if(self.image == None):
        #     pass
        # else:
        #     img = Image.open(self.image)
        #     img = img.resize((50,50), Image.ANTIALIAS)
        #     img = ImageTk.PhotoImage(img)
        #
        #     self.canvas.create_image(20, 20, anchor=tk.NW, image=img)


    def set_place(self):
        x = self.place.split("-")[0]
        y = self.place.split("-")[1]

        if(x=="left"):
            self.place_x = int(self.screen_width/50)
        elif(x=="center"):
            self.place_x = int(self.screen_width/2 - self.window_width/2)
        else:
            self.place_x = self.screen_width - (self.window_width + int(self.screen_width/50))

        if(y=="bottom"):
            self.place_y = self.screen_height - (self.window_height + int(self.screen_height/20))
        elif(y=="center"):
            self.place_y = int(self.screen_height/2 - self.window_height/2)
        else:
            self.place_y = int(self.screen_height/20)

    def get_screen_window_size(self):
        self.screen_height = self.winfo_screenheight()
        self.screen_width = self.winfo_screenwidth()
        self.window_height = int(self.screen_height/10)
        self.window_width = int(self.window_height*3)

    def show(self):

        self.mainloop()



s = notify(place="center-center", image="gg.png")
s.show()
