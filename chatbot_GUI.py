import tkinter as tk
from tkinter import scrolledtext
from nltk.chat.util import Chat, reflections
import random
import re

# Define pairs of patterns and responses
pairs = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you\?", ["I'm doing well, thank you!", "I'm great, thanks for asking."]),
    (r"what is your name\?", ["You can call me ChatBot.", "I'm just a simple ChatBot."]),
    (r"quit|exit", ["Bye!", "Goodbye!", "See you later!"]),
    (r"what are you doing\?|what's up\?", ["I am searching answers for you!", "Nothing much is UP!!"]),
    (r"tell me something", ["YES, what do you need?"]),
    (r"OK|thank you", ["Glad, it's Helping!", "Welcome"]),
    (r"How can you help me\?|what can you do\?", ["I Can search answers for your Questions", "I am here to help you"]),
    (r"What Tablet can we take for fever?|fever tablet?",["The Tablet you can use for fever is Montek LC"]),
    (r"I have a fever and I'm taking ibuprofen for it. Can you suggest foods that can help me feel better and won't interfere with my medication?",['''Fluids:Stay hydrated by drinking plenty of water, herbal teas, clear broths, or electrolyte-rich drinks like coconut water to replenish fluids lost due to fever and sweating.
Take ibuprofen as directed by your healthcare provider to reduce fever and alleviate discomfort. Follow the recommended dosage and frequency specified on the medication label or by your healthcare provider.
Avoid consuming alcohol while taking ibuprofen, as it can increase the risk of stomach irritation and may interfere with the medication's effectiveness.'''])
]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Default response for unmatched patterns
default_responses = ["I'm still learning. Could you ask me something else?"]

# Function to handle sending and receiving messages
def send_message():
    user_input = input_entry.get()
    input_entry.delete(0, tk.END)
    chat_area.insert(tk.END, "You: " + user_input.lower() + "\n")
    
    response = None
    for pattern, responses in pairs:
        if re.search(pattern, user_input, re.IGNORECASE):
            response = random.choice(responses)
            break
    
    if response is None:
        response = random.choice(default_responses)
    
    chat_area.insert(tk.END, "ChatBot: " + response + "\n")
    chat_area.see(tk.END)  # Scroll to the end of the chat area

# Create the main Tkinter window
root = tk.Tk()
root.title("ChatBot")

# Create a scrolled text widget for displaying the chat
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
chat_area.pack(expand=True, fill="both")

# Create an entry widget for user input
input_entry = tk.Entry(root, width=10)
input_entry.pack(side=tk.LEFT, fill=tk.X, padx=7, pady=5, expand=True)

# Create a button to send messages
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=15, pady=5)

# Start the Tkinter event loop
root.mainloop()
