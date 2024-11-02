import random
import webbrowser
import tkinter as tk
from tkinter import messagebox

# Sample data for different moods
mood_songs = {
    "Happy": [
        {"title": "Happy - Pharrell Williams", "url": "https://www.youtube.com/watch?v=ZbZSe6N_BXs"},
        {"title": "Can't Stop the Feeling - Justin Timberlake", "url": "https://www.youtube.com/watch?v=ru0K8uYEZWw"},
        {"title": "Uptown Funk - Mark Ronson ft. Bruno Mars", "url": "https://www.youtube.com/watch?v=OPf0YbXqDm0"}
    ],
    "Sad": [
        {"title": "Someone Like You - Adele", "url": "https://www.youtube.com/watch?v=hLQl3WQQoQ0"},
        {"title": "Fix You - Coldplay", "url": "https://www.youtube.com/watch?v=k4V3Mo61fJM"},
        {"title": "Let Her Go - Passenger", "url": "https://www.youtube.com/watch?v=RBumgq5yVrA"}
    ],
    "Relaxed": [
        {"title": "Weightless - Marconi Union", "url": "https://www.youtube.com/watch?v=UfcAVejslrU"},
        {"title": "Sunset Lover - Petit Biscuit", "url": "https://www.youtube.com/watch?v=4YGpS_fy3Fo"},
        {"title": "Ocean Eyes - Billie Eilish", "url": "https://www.youtube.com/watch?v=viimfQi_pUw"}
    ],
    "Energetic": [
        {"title": "Eye of the Tiger - Survivor", "url": "https://www.youtube.com/watch?v=btPJPFnesV4"},
        {"title": "Stronger - Kanye West", "url": "https://www.youtube.com/watch?v=PsO6ZnUZI0g"},
        {"title": "Don't Stop Me Now - Queen", "url": "https://www.youtube.com/watch?v=HgzGwKwLmgM"}
    ]
}

# Function to suggest a song based on selected mood
def suggest_song():
    mood = mood_var.get()
    if mood not in mood_songs:
        messagebox.showerror("Error", "Please select a valid mood!")
        return

    song = random.choice(mood_songs[mood])
    song_title = song["title"]
    song_url = song["url"]

    # Display the song title and open the URL
    messagebox.showinfo("Recommended Song", f"We recommend: {song_title}")
    webbrowser.open(song_url)  # Opens the song in the default web browser

# GUI setup
root = tk.Tk()
root.title("Mood-Based Music Recommender")
root.geometry("400x300")
root.config(bg="#f0f8ff")

# Title label
title_label = tk.Label(root, text="Mood-Based Music Recommender", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333")
title_label.pack(pady=20)

# Mood selection dropdown
mood_var = tk.StringVar()
mood_var.set("Select your mood")  # Default value

mood_dropdown = tk.OptionMenu(root, mood_var, *mood_songs.keys())
mood_dropdown.config(width=20, font=("Arial", 12))
mood_dropdown.pack(pady=10)

# Suggest button
suggest_button = tk.Button(root, text="Get Recommendation", command=suggest_song, font=("Arial", 12), bg="#4CAF50", fg="white", width=20)
suggest_button.pack(pady=20)

# Run the application
root.mainloop()
