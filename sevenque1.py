import tkinter as tk
from tkinter import ttk
from sevenque import VisionProcessor 

class UpsMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Мониторинг ИБП")
        self.root.geometry("400x250")

        self.notebook = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab1, text="Управление")
        self.notebook.add(self.tab2, text="Инфо")
        self.notebook.pack(expand=True, fill="both")

        self.btn_start = tk.Button(self.tab1, text="Работа от батареи", command=self.run_visuals, bg="lightblue")
        self.btn_start.pack(pady=20)

        self.lbl_slider = tk.Label(self.tab1, text="Установите начальную емкость (%):")
        self.lbl_slider.pack()
        
        self.slider = tk.Scale(self.tab1, from_=0, to=100, orient="horizontal", length=200)
        self.slider.set(100)
        self.slider.pack(pady=10)

        lbl_info = tk.Label(self.tab2, text="Вариант 21.\nПрограммный индикатор уровня заряда ИБП.")
        lbl_info.pack(pady=40)

    def run_visuals(self):
        start_charge = self.slider.get()
        processor = VisionProcessor(start_charge)
        processor.start_animation()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app =UpsMonitor()
    app.run()
