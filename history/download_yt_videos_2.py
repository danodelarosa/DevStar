import pytube

def download_youtube_video(url):
    # Create a YouTube object from the URL
    youtube = pytube.YouTube(url)

    # Get the highest resolution stream available
    stream = youtube.streams.get_highest_resolution()

    # Download the stream
    stream.download()

# Example usage
download_youtube_video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
