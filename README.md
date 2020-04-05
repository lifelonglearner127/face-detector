# face-detector

## Running face detection
    ```
    pip install -r requirements.txt
    python detect_image.py --image images/messi.png --method 0
    python detect_video.py --video video/future.mp4 --method 2
    ```


## Running face detection on browser
- Install Nginx
- Create Virtual Host
- Set `javascript` folder to documentation root
- getUserMedia() can only be called from an HTTPS URL, localhost or a file:// URL.
