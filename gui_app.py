import tkinter as tk
import config
from states import LbaState
from lba_engine import LbaEngine

class LbaGuiApp:
    def __init__(self, root):
        self.root = root
        self.root.title(config.WINDOW_TITLE)
        self.root.geometry(config.WINDOW_SIZE)
        self.root.resizable(False, False)
        
        self.engine = LbaEngine()

        title = tk.Label(root, text="Linear Bounded Automaton Simulator", font=config.FONT_TITLE)
        title.pack(pady=10)
        
        rules_text = f"Limit: {config.MAX_BYTES} Bytes ({config.BOUNDARY_WALL} bits) | Warning at {int(config.WARNING_THRESHOLD*100)}%"
        rules = tk.Label(root, text=rules_text, font=(config.FONT_PRIMARY[0], 10, "italic"))
        rules.pack()

        initial_theme = config.STATE_THEMES["START"]
        self.state_label = tk.Label(
            root, text=initial_theme["text"], font=(config.FONT_PRIMARY[0], 12, "bold"),
            bg=initial_theme["bg"], fg=initial_theme["fg"], width=45, height=2
        )
        self.state_label.pack(pady=15)

        entry_label = tk.Label(root, text="Type your message live below:", font=config.FONT_PRIMARY)
        entry_label.pack(anchor="w", padx=50)

        self.user_input = tk.Entry(root, font=(config.FONT_PRIMARY[0], 12), width=50)
        self.user_input.pack(pady=5)
        self.user_input.bind("<KeyRelease>", self.handle_realtime_typing)

        self.counter_label = tk.Label(
            root, text=f"Bits: 0/{config.BOUNDARY_WALL}  |  Bytes: 0/{config.MAX_BYTES}", 
            font=(config.FONT_PRIMARY[0], 11, "bold")
        )
        self.counter_label.pack(pady=10)

        tape_title = tk.Label(root, text="LBA Tape Contents (Σ = {0, 1}):", font=(config.FONT_PRIMARY[0], 10, "bold"), fg="gray")
        tape_title.pack(anchor="w", padx=50)
        
        self.tape_label = tk.Label(root, text="[ Empty Tape ]", font=config.FONT_TUBE if hasattr(config, 'FONT_TUBE') else config.FONT_TAPE, wraplength=500, justify="left", fg="blue")
        self.tape_label.pack(pady=5, padx=50, fill="x")

    def handle_realtime_typing(self, event):
        """Intercepts keyboard streams and maps state transitions to configuration UI themes."""
        raw_text = self.user_input.get()
        metrics = self.engine.process_payload(raw_text)
        
        state_key = metrics["state"].name  # Converts LbaState.START into string "START"
        theme = config.STATE_THEMES[state_key]

        self.state_label.config(text=theme["text"], bg=theme["bg"], fg=theme["fg"])
        self.tape_label.config(text=metrics["visible_tape"])
        self.counter_label.config(text=f"Bits: {metrics['bit_count']}/{config.BOUNDARY_WALL}  |  Bytes: {metrics['byte_count']}/{config.MAX_BYTES}")