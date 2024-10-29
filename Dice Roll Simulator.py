import tkinter as tk
import random
from PIL import Image, ImageTk

class DiceRollSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Dice Roll Simulator")

        self.dice_images = [
            ImageTk.PhotoImage(Image.open(f"dice{i}.png")) for i in range(1, 7)
        ]

        self.dice_label = tk.Label(root, image=self.dice_images[0])
        self.dice_label.pack(pady=20)

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.start_rolling, font=("Helvetica", 16))
        self.roll_button.pack(pady=20)

        self.rolling = False

    def start_rolling(self):
        if not self.rolling:
            self.rolling = True
            self.roll_dice_animation()

            self.root.after(1000, self.stop_rolling)

    def roll_dice_animation(self):
        if self.rolling:
            random_index = random.randint(0, 5)
            self.dice_label.config(image=self.dice_images[random_index])
            self.root.after(100, self.roll_dice_animation)

    def stop_rolling(self):
        self.rolling = False
        final_result = random.randint(0, 5)
        self.dice_label.config(image=self.dice_images[final_result])

root = tk.Tk()
simulator = DiceRollSimulator(root)

root.mainloop()
