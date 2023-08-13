#lots of bugs are here
#in future i will do it in OOP and and also adding complex regex and also reverse abjad

import tkinter as tk
root = tk.Tk()
label = tk.Label(root, text="Enter the Arabic word:")
label.pack()
entry = tk.Entry(root)
entry.pack()

def calculate_abjad():
    abjad_value = 0
    word = entry.get()
    for letter in word:
        if letter == 'ا':
        abjad_value += 1
            elif letter == 'ب':
                abjad_value += 2
            elif letter == 'ج':
        abjad_value += 3
# Add more conditions for other Arabic letters
    result_label.config(text=f"The abjad value of {word} is {abjad_value}")
    
button = tk.Button(root, text="Calculate Abjad", command=calculate_abjad)

button.pack()
root.mainloop()
