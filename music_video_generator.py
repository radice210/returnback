
import os
import moviepy.editor as mp
from tkinter import Tk, filedialog, Label, Button, Entry, StringVar

# Function to select a song file
def select_song():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    song_var.set(file_path)

# Function to select a background image
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    image_var.set(file_path)

# Function to generate video with lyrics
def generate_video():
    song_path = song_var.get()
    image_path = image_var.get()
    lyrics = lyrics_var.get()
    
    if not song_path or not image_path or not lyrics:
        status_label.config(text="Please provide all inputs.", fg="red")
        return

    # Load image and audio
    audio_clip = mp.AudioFileClip(song_path)
    image_clip = mp.ImageClip(image_path, duration=audio_clip.duration)

    # Define lyrics with timestamps (example: user can customize)
    lyrics_data = [
        (0, lyrics.split("\n")[0]),
        (5, lyrics.split("\n")[1]),
        (10, lyrics.split("\n")[2]),
    ]

    # Create text clips for lyrics
    text_clips = []
    for timestamp, text in lyrics_data:
        txt_clip = mp.TextClip(text, fontsize=50, color='white', font="Arial", size=(1280, 100), method="caption")
        txt_clip = txt_clip.set_position(("center", "bottom")).set_start(timestamp).set_duration(5)
        text_clips.append(txt_clip)

    # Overlay text on video
    video = mp.CompositeVideoClip([image_clip] + text_clips).set_audio(audio_clip).set_fps(24)

    # Save the final video
    output_path = "final_music_video.mp4"
    video.write_videofile(output_path, codec="libx264", audio_codec="aac")

    status_label.config(text="Video created successfully!", fg="green")

# GUI Application
app = Tk()
app.title("Music Video Generator")

# Input fields
Label(app, text="Select Song:").pack()
song_var = StringVar()
Entry(app, textvariable=song_var, width=50).pack()
Button(app, text="Browse", command=select_song).pack()

Label(app, text="Select Background Image:").pack()
image_var = StringVar()
Entry(app, textvariable=image_var, width=50).pack()
Button(app, text="Browse", command=select_image).pack()

Label(app, text="Enter Lyrics (Line by Line):").pack()
lyrics_var = StringVar()
Entry(app, textvariable=lyrics_var, width=50).pack()

# Generate Video Button
Button(app, text="Generate Video", command=generate_video).pack()

# Status Label
status_label = Label(app, text="", fg="blue")
status_label.pack()

# Run Application
app.mainloop()
