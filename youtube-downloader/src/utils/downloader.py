from pytube import YouTube

def clean_url(url):
    if '?' in url:
        url = url.split('?')[0]
    return url

def download_video(url):
    cleaned_url = clean_url(url)
    try:
        yt = YouTube(cleaned_url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        return f"Download completed! Title: {yt.title}, Length: {yt.length} seconds"
    except Exception as e:
        return f"Error occurred: {str(e)}"