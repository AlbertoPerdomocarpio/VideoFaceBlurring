
# Video Face Blurring Tool

This is a web application that allows users to upload a video, apply face blurring (censorship) to the video, and download the processed video. The application uses Flask for the backend, OpenCV for face detection, and Bootstrap for the frontend styling.

## Features

- Upload a video file
- Process the video by applying face blurring
- Download the processed video with blurred faces
- User-friendly interface with Bootstrap
- Video playback of the processed video after processing

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (Bootstrap)
- **Face Blurring**: OpenCV (Python)
- **File Handling**: Werkzeug (for file uploads)
- **Video Playback**: HTML5 `<video>` tag

## Requirements

Before running the application, make sure you have Python installed on your system. You also need to install the following Python packages:

- Flask
- OpenCV
- Werkzeug

You can install the necessary dependencies with `pip`:

```bash
pip install -r requirements.txt
```

Make sure you also have `ffmpeg` installed, as OpenCV uses it for video processing.

## Setting Up the Application

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/video-face-blurring-tool.git
```

### 2. Install dependencies

Navigate to the project directory and install the required Python packages:

```bash
cd video-face-blurring-tool
pip install -r requirements.txt
```

### 3. Configure Flask

Make sure Flask is configured to run correctly. You can set the `FLASK_APP` and `FLASK_ENV` environment variables for development purposes:

```bash
export FLASK_APP=app
export FLASK_ENV=development
```

Or set these in your `.bashrc` or `.zshrc` file if you prefer.

### 4. Run the application

Once everything is set up, run the application:

```bash
flask run
```

By default, the application will run on `http://127.0.0.1:5000`.

## Usage

1. **Upload a Video**: Go to the homepage of the app (`localhost:5000`) and upload a video file (e.g., `.mp4`, `.avi`).
   
2. **Face Blurring Process**: The system will process the video to blur the faces in the frames using OpenCV.

3. **Download Processed Video**: Once the video is processed, you will be provided with a download link to the blurred video.

4. **View Processed Video**: You can also play the processed video directly in the browser after the processing is completed.

## File Structure

```
/video-face-blurring-tool
│
├── app
│   ├── __init__.py
│   ├── routes.py           # Handles routes for file upload, processing, and downloading
│   ├── utils.py            # Utility functions for face detection and blurring
│   ├── uploads/            # Directory for uploaded videos
│   ├── processed/          # Directory for processed videos
│   └── templates/          # HTML templates for rendering pages
│       └── index.html      # Main page for uploading and processing videos
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Customization

- **Video Processing**: You can adjust the parameters for face blurring inside the `utils.py` file where OpenCV is used.
- **Frontend Design**: The design is based on Bootstrap, and you can easily customize the look and feel by modifying the `index.html` file inside the `templates` folder.

## Troubleshooting

- **Video not processed correctly**: Make sure that `ffmpeg` is installed and properly configured, as OpenCV uses it for video processing. You can check the installation by running:

```bash
ffmpeg -version
```

- **File upload issue**: Ensure that the file upload size is not too large. If needed, adjust the `MAX_CONTENT_LENGTH` setting in Flask.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
