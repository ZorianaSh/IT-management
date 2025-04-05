import tkinter as tk
from tkinter import messagebox
from collections import Counter
import re

class TextAnalyzerModel:
    def __init__(self, text=""):
        self.text = text

    def analyze(self):
        words = re.findall(r'\b\w+\b', self.text.lower())
        return Counter(words)

class TextAnalyzerView:
    def __init__(self, root):
        self.root = root
        self.root.title("Частотний аналіз тексту")

        self.text_label = tk.Label(root, text="Введіть текст:")
        self.text_label.pack()

        self.text_input = tk.Text(root, height=10, width=50)
        self.text_input.pack()

        self.analyze_button = tk.Button(root, text="Аналізувати", command=self.analyze_text)
        self.analyze_button.pack()

        self.result_label = tk.Label(root, text="Результати:")
        self.result_label.pack()

        self.result_output = tk.Text(root, height=10, width=50)
        self.result_output.pack()
        self.result_output.config(state=tk.DISABLED)

    def get_input_text(self):
        return self.text_input.get("1.0", tk.END).strip()

    def display_results(self, results):
        self.result_output.config(state=tk.NORMAL)
        self.result_output.delete("1.0", tk.END) 
        for word, count in results.items():
            self.result_output.insert(tk.END, f"{word}: {count}\n")
        self.result_output.config(state=tk.DISABLED)

    def show_error(self, message):
        messagebox.showerror("Помилка", message)
 з виглядом
class TextAnalyzerController:
    def __init__(self, root):
        self.view = TextAnalyzerView(root)
        self.model = TextAnalyzerModel()  

    def analyze_text(self):
        input_text = self.view.get_input_text()
        if not input_text:
            self.view.show_error("Будь ласка, введіть текст для аналізу.")
            return

        self.model.text = input_text

        result = self.model.analyze()

        self.view.display_results(result)

def main():
    root = tk.Tk()
    controller = TextAnalyzerController(root)
    root.mainloop()

if __name__ == "__main__":
    main()
