import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

class MarketSpyApp:
    def __init__(self, root):
        self.root = root
        self.root.title('MarketSpy: Visual Competitor Price & Product Intelligence Dashboard')
        self.root.geometry('1200x800')
        self.root.configure(bg='#2e2e2e')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#2e2e2e')
        self.style.configure('TLabel', background='#2e2e2e', foreground='white')
        self.style.configure('TButton', background='#4e4e4e', foreground='white')

        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.create_input_section()
        self.create_chart_section()

    def create_input_section(self):
        input_frame = ttk.Frame(self.main_frame)
        input_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Label(input_frame, text='Enter Competitor URL:').pack(side=tk.LEFT, padx=(0, 10))
        self.url_entry = ttk.Entry(input_frame, width=50)
        self.url_entry.pack(side=tk.LEFT, padx=(0, 10))

        self.scrape_button = ttk.Button(input_frame, text='Scrape Data', command=self.scrape_data)
        self.scrape_button.pack(side=tk.LEFT, padx=(0, 10))

        self.status_label = ttk.Label(input_frame, text='Status: Idle')
        self.status_label.pack(side=tk.LEFT)

    def create_chart_section(self):
        self.chart_frame = ttk.Frame(self.main_frame)
        self.chart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.canvas = FigureCanvasTkAgg(self.fig, self.chart_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.update_chart()

    def scrape_data(self):
        self.status_label.config(text='Status: Scraping...')
        self.root.update()

        # Simulate scraping
        data = {'Product': ['Product A', 'Product B', 'Product C'], 'Price': [100, 150, 200]}
        self.df = pd.DataFrame(data)

        self.status_label.config(text='Status: Data Scraped')
        self.update_chart()

    def update_chart(self):
        self.ax.clear()

        if hasattr(self, 'df'):
            self.ax.bar(self.df['Product'], self.df['Price'], color='#4e4e4e')
            self.ax.set_title('Competitor Price Comparison', color='white')
            self.ax.set_ylabel('Price', color='white')
            self.ax.set_xlabel('Product', color='white')
            self.ax.tick_params(colors='white')
            self.fig.patch.set_facecolor('#2e2e2e')
            self.ax.set_facecolor('#2e2e2e')

        self.canvas.draw()

if __name__ == '__main__':
    root = tk.Tk()
    app = MarketSpyApp(root)
    root.mainloop()