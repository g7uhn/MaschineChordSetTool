# A simple utility to show Native Instruments Maschine Chord Sets, useful for users of Maschine Mikro
# who don't have the benefit of the awesome screens on the Maschine Mk3... 
#
# Find a way to set this window to "Always On Top" so that it floats over Maschine software while you work in Maschine
# - Windows 11: Install "Windows PowerToys", then Ctrl+Win+T shortcut will set a selected window to "Always On Top"
# - Mac: no idea..!  :-)
#
# Hacky python code pasted together by Andy Webster, 19 Nov 2022
# Additonal credit to Michael Sansom for debugging on Mac. 

from tkinter import *
from tkinter.ttk import *

keyValues = ["C", "C#", "D", "Eb ", "E", "F", "F#", "G", "Ab ", "A", "Bb ", "B", ""]
chordsetValues = ["Maj 1", "Maj 2", "Maj 3", "Maj 4", "Maj 5", "Maj 6", "Maj 7", "Maj 8", "Min 1", "Min 2", "Min 3", "Min 4", "Min 5", "Min 6", "Min 7", "Min 8"]

## Chordset data
# Row 0 is the root of the chord, indexed from keyValues (starts at C)
# Row 1 is the modifier
# Row 2 is the note of any 'slash' chord, indexed from keyValues, value of 12 just pulls a blank from the end of that tuple
maj1data = [[0, 4, 5, 7, 9, 4, 7, 2, 5, 5, 7, 7],["", "mi", "", "", "mi", "sus4", "add9", "mi", "add9", "6", "sus4", ""],[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]]
maj2data = [[0, 0, 0, 0, 5, 5, 0, 9, 4, 5, 7, 7],["", "/", "/", "/", "add9", "mi", "sus4", "mi7", "mi", "", "sus4", "6"],[12, 11, 9, 7, 12, 12, 12, 12, 12, 12, 12, 12]]
maj3data = [[0, 9, 5, 7, 9, 5, 0, 7, 2, 10, 7, 5],["", "mi", "ma7", "sus4", "mi add9", "6", "sus2", "", "sus2", "add9", "sus4", "add9"],[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]]
maj4data = [[0, 7, 9, 5, 5, 9, 2, 9, 7, 9, 7, 2],["", "", "mi", "6", "", "mi/", "mi7", "mi/", "add9", "mi7", "/", "mi/"],[12, 12, 12, 12, 12, 4, 12, 0, 12, 12, 11, 7]]
maj5data = [[0, 2, 5, 0, 8, 3, 10, 5, 7, 10, 5, 0],["", "", "", "", "", "", "", "", "7 sus4", "add9", "6", "add9"],[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]]
maj6data = [[0, 7, 2, 9, 5, 7, 0, 9, 2, 4, 0, 7],["", "", "mi", "mi", "", "/", "/", "mi7", "mi7", "mi7", "/", "sus4"],[12, 12, 12, 12, 12, 5, 4, 12, 12, 12, 5, 12]]
maj7data = [[0, 7, 9, 4, 5, 0, 2, 2, 7, 7, 5, 7],["", "", "mi", "mi", "", "/", "mi", "mi/", "7/", "", "/", "7/"],[12, 12, 12, 12, 12, 4, 12, 0, 11, 12, 9, 11]]
maj8data = [[0, 1, 2, 3, 4, 0, 5, 10, 4, 9, 2, 7],["ma9", "dim", "mi9", "dim7", "mi9", "9#5", "ma7 add13", "9", "mi7", "9", "mi11", "7 (b9, b13)"],[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]]
min1data = [[0, 0, 5, 7, 8, 3, 7, 10, 5, 5, 0, 7],["mi", "mi/", "mi", "", "ma7", "", "mi", "", "", "mi/", "mi/", ""],[12, 3, 12, 12, 12, 12, 12, 12, 12, 8, 7, 12]]
min2data = [[0, 7, 0, 0, 8, 3, 5, 10, 0, 10, 8, 7],["mi", "+/", "mi/", "mi/", "ma7", "ma7", "mi", "7", "mi", "add9", "add9", "7 sus4"],[12, 11, 10, 9, 12, 12, 12, 12, 12, 12, 12, 12]]
min3data = [[0, 8, 3, 10, 5, 5, 0, 7, 0, 0, 0, 0],["mi", "", "", "", "", "mi", "mi/", "sus4", "mi", "mi#5", "mi6", "mi7"],[12, 12, 12, 12, 12, 12, 7, 12, 12, 12, 12, 12]]
min4data = [[0, 3, 10, 5, 8, 8, 8, 3, 2, 2, 5, 7],["mi", "", "", "", "", "ma7", "mi7", "ma7", "sus4", "", "mi/", "+"],[12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 7, 12]]
min5data = [[0, 10, 8, 10, 0, 2, 0, 5, 7, 8, 11, 0],["mi", "", "6", "add9", "mi", "mi7", "mi/", "mi", "", "ma7", "6/9", "sus4"],[12, 12, 12, 12, 12, 12, 3, 12, 12, 12, 12, 12]]
min6data = [[0, 5, 10, 3, 8, 2, 7, 7, 8, 7, 0, 7],["mi", "mi", "", "", "", "mi7 b5", "add9 b9", "", "/", "7", "mi/", "7 b9"],[12, 12, 12, 12, 12, 12, 12, 12, 7, 12, 7, 12]]
min7data = [[0, 8, 0, 0, 5, 3, 0, 9, 8, 7, 0, 7],["mi9", "9", "mi11", "7 (#9,b13)", "mi9", "ma7/", "11", "mi11", "7#11", "7#9", "mi add9", "7 (b9,b13)"],[12, 12, 12, 12, 12, 5, 12, 12, 12, 12, 12, 12]]
min8data = [[0, 2, 0, 0, 5, 8, 3, 10, 9, 8, 7, 0],["mi6/9", "mi7 b5", "mi11/", "mi9", "mi9", "mi7", "mi7", "mi7 b5", "mi11", "ma7#5", "7 (b9,b13)", "mi9 ma7"],[12, 12, 7, 12, 12, 12, 12, 12, 12, 12, 12, 12]]

#...pulling the chordset data together into one array...
chordData = [maj1data, maj2data, maj3data, maj4data, maj5data, maj6data, maj7data, maj8data, min1data, min2data, min3data, min4data, min5data, min6data, min7data, min8data]

window = Tk()

window.title("Maschine Chord Sets")
window.config(bg='#525252')

# Initialize style
s = Style()
# Create style used by default for all Frames
s.configure('TFrame', background='#525252')
s.configure('TLabel', background='#232323', foreground='#d9d9d9', font = ('Sans','10','bold'), padding=5)
s.configure('TCombobox', border=5)

s.configure('top_frame.TFrame', background='red')
s.configure('middle_frame.TFrame') #, background='#232323'
s.configure('bottom_frame.TFrame') #, background='red'

s.configure('chord_frame.TFrame', background='black')

#top_frame = Frame(window, style='top_frame.TFrame', padding=5)
middle_frame = Frame(window, style='middle_frame.TFrame', padding=5)
bottom_frame = Frame(window, style='bottom_frame.TFrame', padding=5)

chord1_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord1_frame.grid(column=0, row=2)
chord2_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord2_frame.grid(column=1, row=2)
chord3_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord3_frame.grid(column=2, row=2)
chord4_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord4_frame.grid(column=3, row=2)
chord5_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord5_frame.grid(column=0, row=1)
chord6_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord6_frame.grid(column=1, row=1)
chord7_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord7_frame.grid(column=2, row=1)
chord8_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord8_frame.grid(column=3, row=1)
chord9_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord9_frame.grid(column=0, row=0)
chord10_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord10_frame.grid(column=1, row=0)
chord11_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord11_frame.grid(column=2, row=0)
chord12_frame = Frame(middle_frame, style='chord_frame.TFrame', padding=2)
chord12_frame.grid(column=3, row=0)

def handler(event):
    print('handler triggered')
    
    generateChords()
    displayChords()
    window.update()

# Initialise the string array 'chords'
chords = ['none'] * 12

keyCombo = Combobox(bottom_frame, values=keyValues)
keyCombo.bind('<<ComboboxSelected>>', handler)
keyCombo.current(0) #set the selected item
currentKey = IntVar() # keyCombo.current()
keyCombo.grid(column=0, row=0, padx=5)
#print ('currentKey = ', currentKey)

chordsetCombo = Combobox(bottom_frame, values=chordsetValues)
chordsetCombo.bind('<<ComboboxSelected>>', handler)
chordsetCombo.current(0) #set the selected item
chordsetCombo.grid(column=1, row=0, padx=5)


def generateChords():
    currentKey = keyCombo.current()
    currentChordset = chordsetCombo.current()
    print ('currentKey = ', currentKey, ' currentChordset = ', currentChordset)

    for i in range(12):
        keyIndex = (i + currentKey) % 12
        print ('keyIndex = ', keyIndex)

        # Main part of chord (e.g. "A" for Asus4)
        chordpartAindex = (currentKey + chordData[currentChordset][0][i]) % 12
        print ('chordpartAindex = ', chordpartAindex)
        chordpartA = keyValues[chordpartAindex]

        # Modifier (e.g. "sus4", "mi add9", "ma7#5", whatever...)
        chordpartB = chordData[currentChordset][1][i]

        # Secondary chord (e.g. slash chords)
        if chordData[currentChordset][2][i] == 12:
            chordpartCindex = 12
        else:
            chordpartCindex = (currentKey + chordData[currentChordset][2][i]) % 12
        print ('chordpartCindex = ', chordpartCindex)
        chordpartC = keyValues[chordpartCindex]
        
        chords[i] = chordpartA + chordpartB + chordpartC
        print ('chord = ', chords[i])

    print ('Chords generated: ', chords)


def displayChords():
    chord1Label = Label(chord1_frame, text= chords[0], width=12, anchor="w")
    chord1Label.grid(column=0, row=0)
    chord2Label = Label(chord2_frame, text= chords[1], width=12, anchor="w")
    chord2Label.grid(column=0, row=0)
    chord3Label = Label(chord3_frame, text= chords[2], width=12, anchor="w")
    chord3Label.grid(column=0, row=0)
    chord4Label = Label(chord4_frame, text= chords[3], width=12, anchor="w")
    chord4Label.grid(column=0, row=0)
    chord5Label = Label(chord5_frame, text= chords[4], width=12, anchor="w")
    chord5Label.grid(column=0, row=0)
    chord6Label = Label(chord6_frame, text= chords[5], width=12, anchor="w")
    chord6Label.grid(column=0, row=0)
    chord7Label = Label(chord7_frame, text= chords[6], width=12, anchor="w")
    chord7Label.grid(column=0, row=0)
    chord8Label = Label(chord8_frame, text= chords[7], width=12, anchor="w")
    chord8Label.grid(column=0, row=0)
    chord9Label = Label(chord9_frame, text= chords[8], width=12, anchor="w")
    chord9Label.grid(column=0, row=0)
    chord10Label = Label(chord10_frame, text= chords[9], width=12, anchor="w")
    chord10Label.grid(column=0, row=0)
    chord11Label = Label(chord11_frame, text= chords[10], width=12, anchor="w")
    chord11Label.grid(column=0, row=0)
    chord12Label = Label(chord12_frame, text= chords[11], width=12, anchor="w")
    chord12Label.grid(column=0, row=0)

generateChords()
displayChords()

#top_frame.grid(column=0, row=0)
middle_frame.grid(column=0, row=1)
bottom_frame.grid(column=0, row=2)
window.mainloop()