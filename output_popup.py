import tkinter as tk
import json
import os
import time
import threading

# Path to your prediction file
PREDICTION_FILE = os.path.join("output", "prediction_output.json")

def load_prediction():
    try:
        with open(PREDICTION_FILE, "r") as f:
            data = json.load(f)
        formatted = (
            f"🧠 Activity: {data.get('activity')}\n"
            f"🔍 Confidence: {data.get('confidence')}\n"
            f"📝 Description: {data.get('description')}\n"
            f"📄 Details: {data.get('details')}\n"
            f"📡 Sources: {data.get('data_sources')}\n"
            f"🕒 Time: {time.ctime(data.get('timestamp'))}"
        )
        return formatted
    except Exception as e:
        return f"[Error reading JSON: {str(e)}]"

def update_text_periodically(text_widget):
    def loop():
        while True:
            new_text = load_prediction()
            text_widget.after(0, lambda: (
                text_widget.delete("1.0", tk.END),
                text_widget.insert(tk.END, new_text)
            ))
            time.sleep(2)
    threading.Thread(target=loop, daemon=True).start()

def main():
    popup = tk.Tk()
    popup.title("Prediction Monitor")
    popup.geometry("500x250+100+100")
    popup.attributes("-topmost", True)
    popup.configure(bg="#111111")

    text_box = tk.Text(
        popup,
        font=("Courier", 11),
        bg="#111111",
        fg="#00ffcc",
        wrap=tk.WORD,
        insertbackground="white"
    )
    text_box.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    update_text_periodically(text_box)

    popup.mainloop()

if __name__ == "__main__":
    main()