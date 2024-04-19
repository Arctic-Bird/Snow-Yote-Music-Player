from pygame import mixer
from tkinter import *
from tkinter import filedialog
import tkinter.font as font
import os

def addToPlaylist():
    global tracklist,index
    os.chdir(filedialog.askdirectory(title="Open a directory with the songs you'd like to play"))
    tracklist = os.listdir()

    for song in tracklist:
        songs_list.insert(END, song)

def deleteFromPlaylist():
    current_song = songs_list.curselection()
    songs_list.delete(current_song[0])

def playSong():
    song = songs_list.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play()

def pauseSong():
    mixer.music.pause()

def stopSong():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

def resumeSong():
    mixer.music.unpause()

def rewindSong():
    mixer.music.rewind()

def previousSong():
    global index
    index -= 1
    previous_song = tracklist[index]

    mixer.music.load(previous_song)
    mixer.music.play()

    #songs_list.selection_clear(0, END)
    songs_list.activate(previous_song)

def nextSong():
    global index
    index += 1

    next_song = tracklist[index]
    mixer.music.load(next_song)
    mixer.music.play()

    #songs_list.selection_clear(0, END)
    songs_list.activate(next_song)
    #songs_list.selection_set(next_song)
    
# Create the root window via tkinter
root_window = Tk()
root_window.title("Snow Yote Music Player") # RIP Arizona Coyotes :pensive:
mixer.init() # Initialize pygame's mixer functionality

# Create the songs list
songs_list = Listbox(root_window, selectmode=SINGLE, bg="blue", fg="white", font=("arial",15), height=12, width=47,
                     selectbackground="black", selectforeground="gray")
songs_list.grid(columnspan=9)


index = 0

defined_font = font.Font(family = "Helvetica")

# Initialize Play button
playButton = Button(root_window, text="Play", width = 7, command = playSong)
playButton['font'] = defined_font
playButton.grid(row=1, column=0)

# Initialize Pause button
pauseButton = Button(root_window, text="Pause", width = 7, command = pauseSong)
pauseButton['font'] = defined_font
pauseButton.grid(row=1, column=1)

# Initialize Stop button
stopButton = Button(root_window, text="Stop", width = 7, command = stopSong)
stopButton['font'] = defined_font
stopButton.grid(row=1, column=2)

# Initialize Resume button
resumeButton = Button(root_window, text="Resume", width = 7, command = resumeSong)
resumeButton['font'] = defined_font
resumeButton.grid(row=1, column=3)

# Initialize Previous button
previousButton = Button(root_window, text="Previous", width = 7, command = previousSong)
previousButton['font'] = defined_font
previousButton.grid(row=1, column=4)

# Initialize Next button
nextButton = Button(root_window, text="Next", width = 7, command = nextSong)
nextButton['font'] = defined_font
nextButton.grid(row=1, column=5)

# Initialize the music player's menu
main_menu = Menu(root_window)
root_window.config(menu=main_menu)

# Create the menu for adding songs to playlist
add_song_menu = Menu(main_menu)
main_menu.add_cascade(label="Menu", menu= add_song_menu)
add_song_menu.add_command(label="Add Songs", command = addToPlaylist)
add_song_menu.add_command(label="Delete Songs", command = deleteFromPlaylist)

root_window.mainloop()