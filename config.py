MAX_BYTES = 10
BITS_PER_BYTE = 8
BOUNDARY_WALL = MAX_BYTES * BITS_PER_BYTE
WARNING_THRESHOLD = 0.8  # 80% capacity
WARNING_WALL = int(BOUNDARY_WALL * WARNING_THRESHOLD)

WINDOW_TITLE = "LBA SMS Enforcer Machine"
WINDOW_SIZE = "600x400"
FONT_PRIMARY = ("Helvetica", 11)
FONT_TITLE = ("Helvetica", 16, "bold")
FONT_TAPE = ("Courier", 10)


STATE_THEMES = {
    "START": {
        "text": "STATE: START (WAITING FOR INPUT)",
        "bg": "#f0f0f0",
        "fg": "black"
    },
    "READING": {
        "text": "✅ STATE: [READING] SAFE PAYLOAD ZONE",
        "bg": "#ccffcc",
        "fg": "green"
    },
    "WARNING": {
        "text": "⚠️ STATE: [WARNING] 80% PROTOCOL CAP REACHED!",
        "bg": "#ffe5cc",
        "fg": "orange"
    },
    "REJECT": {
        "text": "❌ STATE: [REJECT] BOUNDARY WALL CRASHED!",
        "bg": "#ffcccc",
        "fg": "red"
    }
}