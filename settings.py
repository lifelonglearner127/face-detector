DETECTION = {
    "VIOLA_JONES": {
        "METHOD": 0,
        "CASCADE_FILE": "models/haarcascade_frontalface_default.xml"
    },
    "DLIB_HOG": {
        "METHOD": 1,
    },
    "DLIB_CNN": {
        "METHOD": 2,
        "MODE_FILE": "models/mmod_human_face_detector.dat"
    },
    "CAFFE": {
        "METHOD": 3,
        "MODEL_FILE": "models/res10_300x300_ssd_iter_140000.caffemodel",
        "CONFIG_FILE": "models/deploy.prototxt.txt",
        "CONFIDENCE": 0.4,
        "R_MEAN": 104.0,
        "G_MEAN": 117.0,
        "B_MEAN": 123.0
    }
}
