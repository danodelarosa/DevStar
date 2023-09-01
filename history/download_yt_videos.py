import pytube

# Get the YouTube video URL
video_url = "https://www.youtube.com/watch?v=I3xa2y1fWOk&ab_channel=CASAPARLANTE"

# Create a YouTube object and login
youtube = pytube.YouTube(video_url)

# Get the video information
#video_info = youtube.getInfo()

# Get the video title
#video_title = video_info["title"]
video_title = youtube.title
print(video_title)
# Get the video format
video_format = "mp4"
file_ext = youtube.streams.filter(file_extension='mp4')

for ext in file_ext:
    print(ext)

tag = 18

stream = youtube.streams.get_by_itag(tag)
stream.download()

# Download the video
#youtube.streams.get_by_itag(video_format).download()

# Print the success message
print("Successfully downloaded the video: {} in {} format.".format(video_title, video_format))
