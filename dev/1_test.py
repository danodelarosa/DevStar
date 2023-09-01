import pytube

# Get the YouTube video URL
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Create a YouTube object and login
youtube = pytube.YouTube(video_url)

# Get the video information
video_info = youtube.getInfo()

# Get the video title
video_title = video_info["title"]

# Get the video format
video_format = "mp4"

# Download the video
youtube.streams.get_by_itag(video_format).download()

# Print the success message
print("Successfully downloaded the video: {} in {} format.".format(video_title, video_format))
