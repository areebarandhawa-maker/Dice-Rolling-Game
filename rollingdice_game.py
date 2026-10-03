import random
import tkinter as tk
from tkinter import messagebox


class DiceRollingGame:

    def __init__(self, root):
        self.root = root

        # Window settings
        self.root.title(" Dice Rolling Game")
        self.root.geometry("520x600")
        self.root.resizable(False, False)
        self.root.configure(bg="black")

        self.create_interface()

    def create_interface(self):
        # ---------------- TITLE ----------------
        title = tk.Label(
            self.root,
            text="Dice Rolling Game",
            font=("Times new roman", 24),
            bg="black",
            fg="red",
        )
        title.pack(pady=(25, 5))

        # ---------------- SUBTITLE ----------------
        instruction = tk.Label(
            self.root,
            text="Roll the dice and see your luck",
            font=("Times new roman", 13, "italic"),
            bg="black",
            fg="white",
        )
        instruction.pack(pady=5)

        # ---------------- DICE FRAME ----------------
        dice_frame = tk.Frame(self.root, bg="black")
        dice_frame.pack(pady=20)

        # Canvas elements for rounded square dice
        self.die1_canvas = tk.Canvas(
            dice_frame, width=110, height=110, bg="black", highlightthickness=0
        )
        self.die1_canvas.grid(row=0, column=0, padx=20)

        self.die2_canvas = tk.Canvas(
            dice_frame, width=110, height=110, bg="black", highlightthickness=0
        )
        self.die2_canvas.grid(row=0, column=1, padx=20)

        # Draw initial dice (value 1 on both)
        self.draw_rounded_die(self.die1_canvas, 1)
        self.draw_rounded_die(self.die2_canvas, 1)

        # ---------------- RESULT ----------------
        self.result_label = tk.Label(
            self.root,
            text="Ready to roll?",
            font=("Times new roman", 16),
            bg="black",
            fg="white",
        )
        self.result_label.pack(pady=15)

        # ---------------- ROLL BUTTON ----------------
        roll_button = tk.Button(
            self.root,
            text="🎲 Roll Dice 🎲",
            font=("Times new roman", 14),
            bg="white",
            fg="red",
            activebackground="#F0F0F0",
            activeforeground="red",
            relief="raised",
            bd=3,
            cursor="hand2",
            padx=15,
            pady=6,
            command=self.roll_dice,
        )
        roll_button.pack(pady=10)

        # ---------------- EXIT BUTTON ----------------
        exit_button = tk.Button(
            self.root,
            text="Exit",
            font=("Times new roman", 13),
            bg="black",
            fg="red",
            activebackground="black",
            activeforeground="#FF6666",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.exit_game,
        )
        exit_button.pack(pady=15)

    def draw_rounded_die(self, canvas, value):
        """Draws a white square die with soft (rounded) corners and red dots."""
        canvas.delete("all")

        # Soft/Rounded Square Coordinates & Radius
        x1, y1, x2, y2 = 10, 10, 100, 100
        radius = 18

        # Smooth rounded rectangle construction
        points = [
            x1 + radius,
            y1,
            x1 + radius,
            y1,
            x2 - radius,
            y1,
            x2 - radius,
            y1,
            x2,
            y1,
            x2,
            y1 + radius,
            x2,
            y1 + radius,
            x2,
            y2 - radius,
            x2,
            y2 - radius,
            x2,
            y2,
            x2 - radius,
            y2,
            x2 - radius,
            y2,
            x1 + radius,
            y2,
            x1 + radius,
            y2,
            x1,
            y2,
            x1,
            y2 - radius,
            x1,
            y2 - radius,
            x1,
            y1 + radius,
            x1,
            y1 + radius,
            x1,
            y1,
        ]

        canvas.create_polygon(
            points, fill="white", smooth=True, outline="#A1A0A0", width=2
        )

        # Dot mapping on the 90x90 square
        dot_positions = {
            "center": (55, 55),
            "top_left": (32, 32),
            "top_right": (78, 32),
            "bottom_left": (32, 78),
            "bottom_right": (78, 78),
            "mid_left": (32, 55),
            "mid_right": (78, 55),
        }

        layout = {
            1: ["center"],
            2: ["top_left", "bottom_right"],
            3: ["top_left", "center", "bottom_right"],
            4: ["top_left", "top_right", "bottom_left", "bottom_right"],
            5: [
                "top_left",
                "top_right",
                "center",
                "bottom_left",
                "bottom_right",
            ],
            6: [
                "top_left",
                "top_right",
                "mid_left",
                "mid_right",
                "bottom_left",
                "bottom_right",
            ],
        }

        r = 6  # Radius of red dots
        for pos in layout[value]:
            cx, cy = dot_positions[pos]
            canvas.create_oval(
                cx - r, cy - r, cx + r, cy + r, fill="red", outline="red"
            )

    def roll_dice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)

        # Redraw rounded square dice
        self.draw_rounded_die(self.die1_canvas, die1)
        self.draw_rounded_die(self.die2_canvas, die2)

        total = die1 + die2
        self.result_label.config(
            text=f"Die 1: {die1}   |   Die 2: {die2}\nTotal: {total}"
        )

    def exit_game(self):
        answer = messagebox.askyesno(
            "Exit Game", "Are you sure you want to exit?"
        )
        if answer:
            self.root.destroy()


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    root = tk.Tk()
    game = DiceRollingGame(root)
    root.mainloop()