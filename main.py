import tkinter as tk
from tkinter import Label, PhotoImage, ttk, Button, Entry
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image, ImageTk
import requests
from io import BytesIO

# Spotify API Credentials
CLIENT_ID = "your client ID"
CLIENT_SECRET = "your client secret"
REDIRECT_URI = "http://localhost:7777/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-read-currently-playing,user-modify-playback-state,user-read-playback-state,user-read-private"
))

def get_current_song():
    """Fetch the currently playing song from Spotify."""
    try:
        current_track = sp.currently_playing()
        if current_track and current_track['is_playing']:
            track_name = current_track['item']['name']
            artist_name = current_track['item']['artists'][0]['name']
            album_name = current_track['item']['album']['name']
            album_cover_url = current_track['item']['album']['images'][0]['url']
            progress_ms = current_track['progress_ms']
            duration_ms = current_track['item']['duration_ms']
            remaining_ms = duration_ms - progress_ms
            return track_name, artist_name, album_name, album_cover_url, progress_ms, duration_ms, remaining_ms
    except:
        return None

def update_song_info():
    """Update song information in the UI."""
    song_info = get_current_song()
    if song_info:
        track_name, artist_name, album_name, album_cover_url, progress_ms, duration_ms, remaining_ms = song_info
        track_label.config(text=track_name)
        artist_label.config(text=artist_name)
        album_label.config(text=album_name)
        progress_bar['value'] = (progress_ms / duration_ms) * 100
        progress_time_label.config(text=f"{progress_ms // 60000}:{(progress_ms // 1000) % 60} / {duration_ms // 60000}:{(duration_ms // 1000) % 60}")
        
        # Load and display album cover
        response = requests.get(album_cover_url)
        img_data = Image.open(BytesIO(response.content))
        img_data = img_data.resize((250, 250))
        img = ImageTk.PhotoImage(img_data)
        album_cover_label.config(image=img)
        album_cover_label.image = img
    else:
        track_label.config(text="Žádná hudba nehraje.")
        progress_bar['value'] = 0
    root.after(1000, update_song_info)

def play_pause():
    current_track = sp.current_playback()
    if current_track and current_track['is_playing']:
        sp.pause_playback()
    else:
        sp.start_playback()

def next_track():
    sp.next_track()

def previous_track():
    sp.previous_track()

def seek_song(event):
    """Seek to a specific position in the song."""
    if progress_bar['value'] > 0:
        duration = sp.current_playback()['item']['duration_ms']
        seek_position = int((event.x / progress_bar.winfo_width()) * duration)
        sp.seek_track(seek_position)

def search_and_play():
    """Search for a song and play it."""
    query = search_entry.get()
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track_uri = results['tracks']['items'][0]['uri']
        sp.start_playback(uris=[track_uri])

# GUI Setup
root = tk.Tk()
root.title("Spotify Now Playing")
root.geometry("400x500")
root.configure(bg="#121212")

track_label = Label(root, text="", font=("Arial", 14, "bold"), fg="white", bg="#121212")
track_label.pack(pady=5)

artist_label = Label(root, text="", font=("Arial", 12), fg="gray", bg="#121212")
artist_label.pack()

album_label = Label(root, text="", font=("Arial", 10), fg="gray", bg="#121212")
album_label.pack()

album_cover_label = Label(root, bg="#121212")
album_cover_label.pack(pady=10)

# Progress bar with time
progress_frame = tk.Frame(root, bg="#121212")
progress_frame.pack(pady=5)
progress_time_label = Label(progress_frame, text="", font=("Arial", 10), fg="white", bg="#121212")
progress_time_label.pack()
progress_bar = ttk.Progressbar(progress_frame, orient="horizontal", length=300, mode="determinate", style="TProgressbar")
progress_bar.pack()
progress_bar.bind("<Button-1>", seek_song)

# Playback Controls
control_frame = tk.Frame(root, bg="#121212")
control_frame.pack(pady=10)

prev_button = Button(control_frame, text="⏮", font=("Arial", 14), fg="black", bg="#1DB954", relief="flat", command=previous_track)
prev_button.pack(side="left", padx=10)

play_pause_button = Button(control_frame, text="⏯", font=("Arial", 14), fg="black", bg="#1DB954", relief="flat", command=play_pause)
play_pause_button.pack(side="left", padx=10)

next_button = Button(control_frame, text="⏭", font=("Arial", 14), fg="black", bg="#1DB954", relief="flat", command=next_track)
next_button.pack(side="left", padx=10)

# Search Bar
search_frame = tk.Frame(root, bg="#121212")
search_frame.pack(pady=10)
search_entry = Entry(search_frame, font=("Arial", 12), width=25)
search_entry.pack(side="left", padx=5)
search_button = Button(search_frame, text="🔍", font=("Arial", 12), fg="black", bg="#1DB954", relief="flat", command=search_and_play)
search_button.pack(side="left", padx=5)

# Style progress bar
style = ttk.Style()
style.configure("TProgressbar", thickness=5, troughcolor="#282828", background="#1DB954", bordercolor="#282828", darkcolor="#1DB954", lightcolor="#1DB954")

# Start updating song info
update_song_info()

root.mainloop()

