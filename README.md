# face-detector
## Face Detector 
- Method 0: Viola-Jones
- Dlib HOG
- Dlib CNN
- OpenCV DNN
> You can see the all required settings in `settings.py` file.

    ```
    pip install -r requirements.txt
    python detect_image.py --image images/messi.png --method 0
    python detect_video.py --video ~/Downloads/future.mp4 --method 0
    ```

## Running face detection on browser
- Install Nginx
- Create Virtual Host
- Copy the `javascript` folder to documentation root
- getUserMedia() can only be called from an HTTPS URL, localhost or a file:// URL.
