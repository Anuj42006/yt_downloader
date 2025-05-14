from flask import Flask, render_template, request, send_file, jsonify
import yt_dlp
from pathlib import Path
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = Path("downloads").absolute()
DOWNLOAD_FOLDER.mkdir(exist_ok=True)

def download_video(url):
    """Download video using yt-dlp"""
    ydl_opts = {
        'format': 'best[ext=mp4]/best',  # Simplified format selection
        'outtmpl': str(DOWNLOAD_FOLDER / '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'extract_flat': True,  # Only extract metadata
        'merge_output_format': 'mp4'
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                # Extract video metadata
                meta = ydl.extract_info(url, download=False)
                if not meta:
                    raise Exception("Could not extract video information")
                
                # Extract title from metadata
                title = meta.get('title') if isinstance(meta, dict) else None
                if not title:
                    raise Exception("Could not get video title")
                
                # Create safe filename
                safe_title = "".join(
                    c for c in title 
                    if c.isalnum() or c in (' ','-','_')
                ).rstrip()
                
                # Set output path
                output_path = DOWNLOAD_FOLDER / f'{safe_title}.mp4'
                
                # Configure download options
                download_opts = dict(ydl_opts)
                download_opts['outtmpl'] = str(output_path)
                download_opts['extract_flat'] = False
                
                # Perform download
                print(f"Downloading: {title}")
                with yt_dlp.YoutubeDL(download_opts) as downloader:
                    downloader.download([url])
                
                # Verify download
                if output_path.exists():
                    return output_path
                
                # Look for alternate extensions
                for file in DOWNLOAD_FOLDER.glob(f"{safe_title}.*"):
                    if file.exists():
                        return file
                
                raise Exception(f"Download completed but file not found at {output_path}")
                
            except Exception as extract_error:
                print(f"Error extracting info: {str(extract_error)}")
                raise
                
    except Exception as e:
        print(f"Download error: {str(e)}")
        raise

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        url = request.form['url']
        
        # Download video
        downloaded_file = download_video(url)
        
        # Send file to user
        return send_file(
            str(downloaded_file),
            as_attachment=True,
            download_name=downloaded_file.name,
            mimetype='video/mp4'
        )
        
    except Exception as e:
        error_msg = str(e)
        print(f"Error: {error_msg}")
        return f"Download failed: {error_msg}", 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)