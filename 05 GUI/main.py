import tkinter as tk

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Demo GUI")
        self.root.geometry("650x450")
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        m_tasks = tk.Menu(menu_bar, tearoff=False)
        m_tasks.add_command(label="Exit", command=self.root.destroy)
        menu_bar.add_cascade(label="System", menu=m_tasks)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    App().run()