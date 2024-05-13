# Video Volume Standardization
This Python script automates the process of adjusting video audio levels to a target standard volume. It utilizes the `moviepy.editor` library to manipulate video files.

## Features
- Adjusts video audio volume to a user-defined standard level.
- Reads video files from a specified directory.
- Provides feedback on original and adjusted volume levels.
- Supports single file processing or batch processing from a directory.
- Allows setting a custom volume adjustment factor (optional).

## Process Flow
1. Initialization:
    - Standard volume level is set to 0.1 (adjustable).
    - Script reads command-line arguments to determine processing mode.
2. File Processing:
    - Script iterates through video files (single file or directory).
    - For each video:
        - Original file name is extracted with extension.
        - New file name is created with adjusted volume indicator.
        - Original video volume is calculated and reported.
        - Audio volume is adjusted to the standard level.
        - Adjusted video is saved with a temporary audio file for efficiency.
        - New video volume is calculated and reported.
        - Processing progress is displayed.

## Success/Failure Reports
The script provides feedback on the success of each video processing step:
- Original and adjusted video volume levels are reported.
- Any errors encountered during processing would be printed to the console.

## Logs
The script doesn't generate separate log files by default. However, the console output provides a record of processed videos and their original/adjusted volume levels.

## Requirements
- Python 3.x
- `moviepy` library (pip install moviepy)
- `ffmpeg` (for video processing) - Installation instructions can be found online for your specific operating system.

## Instructions
1. Install `moviepy` and ensure `ffmpeg` is available in your system path.
2. Save the script as `video_volume_standardization.py`.
3. Single File Processing:
    - Open a terminal/command prompt and navigate to the directory containing the script and the video file.
    - Run the script with the video file name as an argument:
        ```Bash
        python video_volume_standardization.py my_video.mp4     # Adjust my_video.mp4 with standard volume x 1.5.
        python video_volume_standardization.py my_video.mp4 1.5 # Adjust my_video.mp4 with standard volume x 1.5.
        ```
4. Batch Processing:
    - Open a terminal/command prompt and navigate to the directory containing the script and the video files.
    - Run the script with the directory path containing the videos as an argument (optional volume adjustment can be added as a third argument):
        ```Bash
        python video_volume_standardization.py # Adjust all videos in "queue" directory.
        ```

## Disclaimer
This script is provided as-is without warranty. Ensure compatibility with your video files and desired volume levels. Back up your original videos before processing.
