# Autonomy-Interview-Challenge

<img width="452" height="498" alt="IMG_9739" src="https://github.com/user-attachments/assets/f3697e42-2863-41f2-9ee2-bec0d298a63d" />

---
If you don't have UV follow instructions: https://docs.astral.sh/uv/getting-started/installation/

If you are on windows you may also need to turn off smart app control


To run code do:

``` bash
uv run main.py
```
---

**Write all code in main.py**

### Challenge 0 (required):
Open interview_video.mp4 in openCV.

---

### Challenge 1 (required):
Identify red LEDs in the video. Draw rotated bounding boxes around the red LEDs.

Tutorial - https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

Hint - https://www.geeksforgeeks.org/python/splitting-and-merging-channels-with-python-opencv/

Suggested Steps:
- Show a video of extracted red channel
- Threshold red channel for the lights
- Contour binarized image
- Apply rotated rectangle to contours

There are a couple of ways to remove small bits of noise, I'll let you figure that out 😃

---

### Challenge 2 (required):
Use the bounding boxes from the previous challenge to find a position to the center of panel. Use the PnP.py sample file for the camera intrinsics. Panel dimensions are included in the file. Print the position.

---
### Challenge 3 (bonus):
Print which icon is being shown using the provided icon PNGs.