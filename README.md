# Autonomy-Interview-Challenge

<img width="452" height="498" alt="IMG_9739" src="https://github.com/user-attachments/assets/f3697e42-2863-41f2-9ee2-bec0d298a63d" />

---
If you don't have UV follow these instructions: https://docs.astral.sh/uv/getting-started/installation/

If you are on windows you may need to turn off smart app control


To run code do:

``` bash
uv run main.py
```
---

**Write all code in main.py**

### Challenge 0 (required):
Open interview_video.mp4 in openCV.
Tutorial - https://learnopencv.com/read-write-and-display-a-video-using-opencv-cpp-python/

---

### Challenge 1 (required):
Identify red LEDs in the video. Draw rotated bounding boxes around the red LEDs.

Hint - https://www.geeksforgeeks.org/python/splitting-and-merging-channels-with-python-opencv/

Suggested Steps:
- Show a video of extracted red channel
- Threshold red channel for the lights
- Contour binarized image
- Apply rotated rectangles to contours - https://www.geeksforgeeks.org/python/finding-minimum-enclosing-rectangle-in-opencv-python/

There are a couple of ways to remove small bits of noise, I'll let you figure that out 😃

---

### Challenge 2 (Required if Autonomy and not embedded):
Use the bounding boxes from the previous challenge to find a position to the center of panel. PnP.py sample file contains an example of how to get the camera intrinsics, **DO NOT EDIT or SUBMIT this file**. Panel dimensions are included in the file. Print the position. A tutorial can be found here https://medium.com/@abdulhaq.ah/what-is-solvepnp-and-how-does-it-work-d9ac70823724

You may see strange values for X and Y positions, that is ok. Keep all of your units in cm.

---
### Submition:
Upload main.py to the google form.