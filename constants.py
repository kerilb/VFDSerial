""" defines constants for the display """
import serial

# control sequences
CLEAR = "\x1B\x5B\x32\x4A"
CURSOR_LINE_START = "\x0D"
CURSOR_LINEFEED = "\x0A"
CURSOR_BACK = "\x08"
CURSOR_CLEAR_TO_LINE_END = "\x1B\x5B\x30\x4B"
CURSOR_POSITION = "\x1B\x5B%s\x3B%s\x48"
COUNTRY_CODE = "\x1B\x52\x35" # russian cp-866 codepage

# communication
BAUDRATE = 9600
PARITY = serial.PARITY_NONE

# Dimensions
LINE_LENGTH = 20
LINES = 2
