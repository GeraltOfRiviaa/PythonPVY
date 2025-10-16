import tkinter as tk
import random
from tkinter import simpledialog
from tkinter import colorchooser

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Demo GUI")
        self.root.geometry("650x450")
        self.random = random.Random()

        self.canvas = tk.Canvas(self.root, width=650, height=450, bg="white")
        self.canvas.pack(fill="both",expand=True)
        self.canvas.delete
        width,height = self._get_canvas_size()

        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        m_tasks = tk.Menu(menu_bar, tearoff=False)
        m_tasks.add_command(label="Exit", command=self.root.destroy)
        menu_bar.add_cascade(label="System", menu=m_tasks)

        m_graphics = tk.Menu(menu_bar, tearoff=False)
        m_graphics.add_command(label="Magical lines", command=lambda: self.magic_barcode(2,5))
        m_graphics.add_command(label="Checkerboard", command=lambda: self.checkerboard_dialog())
        m_graphics.add_command(label="Target", command=self.root.destroy)
        menu_bar.add_cascade(label="Graphics", menu=m_graphics)

        m_colors = tk.Menu(menu_bar, tearoff=False)
        m_colors.add_command(label="Red", command=lambda: self.set_bg("red"))
        m_colors.add_command(label="Green",command=lambda: self.set_bg("green"))
        m_colors.add_command(label="Blue",command=lambda: self.set_bg("blue"))
        
        m_colors.add_command(label="Clear",command=lambda: self.clear_bg)
        menu_bar.add_cascade(label="Colors", menu=m_colors)

    def set_bg(self, color:str) -> None:
        self.canvas.config(bg=color)
    def clear_bg(self) -> None:
        self.canvas.delete("all")

    def magic_barcode(self, min:int, max:int) -> None:
        self.clear_bg()
        self.canvas.config(bg="white")
        w,h, = self._get_canvas_size()
        
        x = 0
        while x < w:
            
            width = self.random.randint(min, max)
            color = f"#{random.randint(0,0xffffff):06x}"
            self.canvas.create_line(x,0,x,w, fill=color, width=width)
            x += width
        
    def _get_canvas_size(self) -> tuple:
        w = self.canvas.winfo_width() or self.root.winfo_width or 600
        h = self.canvas.winfo_height() or self.root.winfo_height
        return w,h    
    
    def checkerboard(self, size: int = 8, light: str = "#eee" , dark: str = "#111") -> None:
        self.clear_bg()
        self.canvas.config(bg=light)
        w,h = self._get_canvas_size()
        
        cell_x = w / size
        cell_y = h / size

        for y in range(size):
            for x in range(size):
                if (x + y) % 2 == 0:
                    self.canvas.create_rectangle(x*cell_x,y * cell_y,x*cell_x+cell_x, y * cell_y * cell_y,
                                                  fill=dark,outline="#333", width=5)
    def checkerboard_dialog(self):
        size = simpledialog.askinteger(title="Chessboard", prompt="Enter the size of checker board on x axes",
                                       minvalue=2,maxvalue=20,initialvalue=8,parent=self.root)
        
        light = colorchooser.askcolor(title="Choose a color of background: ")[1]
        self.checkerboard(size=size, light=light)
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    App().run()