# Python Spotify Controller - Desktop Application

## Overview
This is a Python-based desktop application that displays the currently playing song on Spotify. It also allows users to control playback (play, pause, skip, previous) and search for songs to play. The application uses the Spotify API to fetch real-time track information and is built using the Tkinter GUI library.

## Disclaimer
This is an **unofficial** application and is **not affiliated with, endorsed, or sponsored by Spotify**. It simply uses the Spotify Web API to provide playback control and track information.

## Features
- Displays the currently playing song, artist, and album information.
- Shows the album cover of the currently playing track.
- Provides playback controls: play/pause, next track, previous track.
- Displays the song progress and allows seeking within the song.
- Allows users to search for and play songs directly from the application.

## Prerequisites
To use this application, you will need:
1. **Spotify API Credentials:** You must have a Spotify Developer account and create an application to get the required credentials.
2. **Python 3.x** installed on your system.
3. The following Python libraries installed:
   - `tkinter` (comes with Python)
   - `spotipy`
   - `pillow`
   - `requests`

## How to Get Spotify API Credentials
1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2. Log in with your Spotify account.
3. Click on "Create an App" and fill in the required details.
4. Once the app is created, navigate to **Settings** and add `http://localhost:7777/callback` as a Redirect URI.
5. Copy the **Client ID** and **Client Secret** from the dashboard.

## Installation
1. Clone or download this repository.
2. Install the required dependencies using pip:
   ```sh
   pip install spotipy pillow requests
   ```
3. Replace `your client ID` and `your client secret` in the script with your Spotify API credentials.

## Usage
1. Run the application:
   ```sh
   python app.py
   ```
2. Log in with your Spotify account when prompted.
3. The GUI will display the currently playing song and allow you to control playback.

## Controls
- **Play/Pause Button:** Toggle playback.
- **Next Track Button:** Skip to the next song.
- **Previous Track Button:** Go back to the previous song.
- **Search Bar:** Enter a song name and press the search button to play it.
- **Progress Bar:** Click on it to seek within the current song.

## Notes
- Ensure you have an active Spotify Premium account for full playback control.
- The application only works when Spotify is actively playing music on a connected device.
- Make sure your redirect URI in the Spotify Developer Dashboard matches the one in the script.

## License
This project is licensed under the **MIT License**. See the LICENSE file for details.

**Note:** This project is not affiliated with or endorsed by Spotify.

