from tkinter import *
import pandas
import random

# CONSTANTS & VARIABLES
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# COMMANDS
# handling exceptions
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")