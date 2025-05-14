# YouTube Downloader

This project is a simple web application that allows users to download YouTube videos by entering the video URL. It is built using Python for the backend and HTML/CSS for the frontend.

## Project Structure

```
youtube-downloader
├── src
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   ├── templates
│   │   ├── base.html
│   │   └── index.html
│   ├── app.py
│   └── utils
│       └── downloader.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

To run this project, you need to have Python installed on your machine. You also need to install the required packages listed in `requirements.txt`.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd youtube-downloader
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter the YouTube video URL in the input field and click the download button.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.