# Billboard to Spotify Playlist Creator

This Python script allows you to create a Spotify playlist based on Billboard's top songs for a specific year. It uses Beautiful to Scrap Billboard music data and makes spotify search request based on the data collected

## Prerequisites

Before running the script, make sure you have the following installed:

- Python 3
- `requests` library (`pip install requests`)
- `BeautifulSoup` library (`pip install beautifulsoup4`)
- `spotipy` library (`pip install spotipy`)

You also need to set up a Spotify Developer account and obtain your client ID and client secret.

## Technology Used

- Python: The script is written in Python, a versatile programming language.
- `requests` library: Used for making HTTP requests to scrape data from the Billboard website.
- `BeautifulSoup` library: Used for parsing HTML content scraped from the Billboard website.
- `spotipy` library: Used for interacting with the Spotify API to create playlists and add tracks.

## Usage

1. Clone this repository to your local machine.
2. Set up a virtual environment and install the required dependencies.
3. Obtain your Spotify client ID and client secret and set them as environment variables (`SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`).
4. Run the script and follow the prompts to select the year you want to create a playlist for.
5. If it's your first time running the script or your access token has expired, the script will prompt you to visit a URL to authorize the application and obtain an access token. Follow the instructions in the terminal to complete this step.

## Functionality

- The script prompts the user to input the year they want to create a playlist for.
- It scrapes Billboard's Hot 100 chart for the specified year.
- It creates a private Spotify playlist named "<Year> Top 100" and adds the top 100 songs from Billboard for that year to the playlist.
