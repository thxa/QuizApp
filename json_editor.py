
import tkinter as tk
from tkinter import filedialog, messagebox
import json



class JSONEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Editor")
        
        self.load_button = tk.Button(root, text="Load JSON", command=self.load_json)
        self.load_button.pack()

        self.save_button = tk.Button(root, text="Save JSON", command=self.save_json)
        self.save_button.pack()

        self.id_label = tk.Label(root, text="ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(root)
        self.id_entry.pack()

        self.question_label = tk.Label(root, text="Question:")
        self.question_label.pack()
        self.question_entry = tk.Entry(root, width=100)
        self.question_entry.pack()

        self.options_label = tk.Label(root, text="Options:")
        self.options_label.pack()
        self.options_text = tk.Text(root, height=10, width=100)
        self.options_text.pack()

        self.explain_label = tk.Label(root, text="Explain:")
        self.explain_label.pack()
        self.explain_entry = tk.Entry(root, width=100)
        self.explain_entry.pack()

        self.answers_label = tk.Label(root, text="Answers:")
        self.answers_label.pack()
        self.answers_entry = tk.Entry(root)
        self.answers_entry.pack()

        self.resources_label = tk.Label(root, text="Resources:")
        self.resources_label.pack()
        self.resources_text = tk.Text(root, height=10, width=100)
        self.resources_text.pack()

        self.update_button = tk.Button(root, text="Update", command=self.update_json)
        self.update_button.pack()


        self.prev_button = tk.Button(root, text="Prev", command=self.prev)
        self.prev_button.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next)
        self.next_button.pack()



        self.json_data = None
        self.current_index = None

    def load_json(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if file_path:
            with open(file_path, 'r') as f:
                self.json_data = json.load(f)
            self.current_index = 0
            self.display_json()

    def display_json(self):
        if self.json_data and self.current_index is not None:
            item = self.json_data[self.current_index]
            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(tk.END, item['_id'])

            self.question_entry.delete(0, tk.END)
            self.question_entry.insert(tk.END, item['question'])

            self.options_text.delete('1.0', tk.END)
            self.options_text.insert(tk.END, '\n'.join(item['options']))

            self.explain_entry.delete(0, tk.END)
            self.explain_entry.insert(tk.END, item['explain'])

            self.answers_entry.delete(0, tk.END)
            self.answers_entry.insert(tk.END, ','.join(map(str, item['answers'])))

            self.resources_text.delete('1.0', tk.END)
            self.resources_text.insert(tk.END, '\n'.join(item['resources']))

    def update_json(self):
        if self.json_data and self.current_index is not None:
            item = self.json_data[self.current_index]
            item['_id'] = int(self.id_entry.get())
            item['question'] = self.question_entry.get()
            item['options'] = self.options_text.get('1.0', tk.END).strip().split('\n')
            item['explain'] = self.explain_entry.get()
            item['answers'] = list(map(int, self.answers_entry.get().split(',')))
            item['resources'] = self.resources_text.get('1.0', tk.END).strip().split('\n')
            messagebox.showinfo("Info", "JSON updated!")

    def save_json(self):
        if self.json_data:
            file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON Files", "*.json")])
            if file_path:
                with open(file_path, 'w') as f:
                    json.dump(self.json_data, f, indent=4)
                messagebox.showinfo("Info", "JSON saved!")

    def prev(self):
        if(self.current_index > 0):
            self.current_index -= 1 
            self.display_json()
        else:
            self.current_index = len(self.json_data)-1
            self.display_json()

    def next(self):
        if(self.current_index + 1 < len(self.json_data)):
            self.current_index += 1 
            self.display_json()
        else:
            self.current_index = 0


if __name__ == "__main__":
    root = tk.Tk()
    app = JSONEditorApp(root)
    root.mainloop()

