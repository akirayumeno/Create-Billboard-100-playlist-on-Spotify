# 🎧 Create Billboard Hot 100 Playlist on Spotify
Automatically generate a Spotify playlist based on the Billboard Hot 100 chart for a given date 🎶

# 📌 Overview
This Python project allows you to create a Spotify playlist populated with the songs from the Billboard Hot 100 chart on any specific date (e.g., your birthday or a nostalgic moment). It fetches the chart data from Billboard and uses the Spotify Web API to search and add tracks to your Spotify account.

# 🚀 Features
- 🔍 Scrape Billboard Hot 100 chart for any historical date
- 🎼 Search and match each track on Spotify
- 📻 Automatically create a playlist on your Spotify account
- 💾 Save matched and unmatched songs for review

# 🛠️ Tech Stack
- Python
- BeautifulSoup – Web scraping
- Spotipy – Spotify Web API wrapper
- Spotify Developer Account & API

# 🔧 How to Use
1. Clone the repo:
```bash
git clone https://github.com/akirayumeno/Create-Billboard-100-playlist-on-Spotify.git
cd Create-Billboard-100-playlist-on-Spotify
```
2. Set up your Spotify Developer credentials:
```bash
client_id=your_client_id
client_secret=your_client_secret
username=your username
```
ps: you should add the same username to the spotify developer dashboard.

3. Run the script and input a date:
```bash
python main.py
```
When prompted, enter a date like 2001-08-18.
4. Enjoy your automatically created playlist on Spotify!
