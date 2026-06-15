import config
from states import LbaState

class LbaEngine:
    def __init__(self):
        # Configuration parameters loaded dynamically from config file
        self.boundary = config.BOUNDARY_WALL
        self.warning_wall = config.WARNING_WALL

    def process_payload(self, text_input):
        """Processes text input through the computational limits of the LBA."""
        # Convert text stream to binary string representation
        binary_tape = ''.join(format(ord(char), '08b') for char in text_input)
        bit_count = len(binary_tape)
        byte_count = bit_count // config.BITS_PER_BYTE

        if bit_count == 0:
            current_state = LbaState.START
            visible_tape = "[ Empty Tape ]"
        elif bit_count > self.boundary:
            current_state = LbaState.REJECT
            visible_tape = binary_tape[:self.boundary] + " [OVERFLOW BITS DROPPED!]"
        elif bit_count >= self.warning_wall:
            current_state = LbaState.WARNING
            visible_tape = binary_tape
        else:
            current_state = LbaState.READING
            visible_tape = binary_tape

        return {
            "state": current_state,
            "visible_tape": visible_tape,
            "bit_count": bit_count,
            "byte_count": byte_count
        }