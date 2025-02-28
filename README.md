# Joint_Kinematics_angle_calculation
This script is designed to analyze videos by detecting white points, calculating angles between consecutive points, and saving the results for further study. It's particularly helpful for tracking motion in fields like science or engineering.

⏺️Overview

  1️⃣This Python script is designed to process videos from infrared motion capture systems, where retroreflective markers are attached to the body. It provides a simple way to detect these markers, calculate angles between        them, and save the results, avoiding the need for costly software typically used for such tasks.

⏺️What the Script Does

  1️⃣Marker Detection: The script loads a video, converts frames to grayscale, and uses thresholding to identify white points, which are the markers. 
  
  2️⃣Angle Calculation: It finds up to five markers per frame, calculates the angle at the middle point for every set of three consecutive markers, and stores this data.
  
  3️⃣Output: Results are saved in an Excel file ('detected_angles.xlsx') and a processed video ('processed_video.avi') with visual annotations like circles and angle labels.
  

⏺️How to Use

Ensure you have Python with OpenCV, NumPy, and Pandas installed. Place your video (named 'V1.mp4') in the same folder, then run the script. Change the filename in the code if using a different video.
Unexpected Detail
An interesting aspect is that the script labels markers based on their order in each frame, which might lead to inconsistent angle calculations if markers move and their order changes, potentially affecting accuracy for dynamic motions.

⭐Output:

LEVEL WALKING:


https://github.com/user-attachments/assets/a4ccc897-81dc-4652-b79c-02469214d1af


SLOPE WALKING:


https://github.com/user-attachments/assets/81902c87-69cb-4dd5-9034-e2ee0dea4995


STARICASE ASCEND:



https://github.com/user-attachments/assets/598accd7-691e-4c03-b79e-f7754c443cff








〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️

1️⃣Video Loading and Processing:

Loads the video using cv2.VideoCapture with the filename 'Descend-without-trajectories.mp4'.
Sets up a VideoWriter to save the processed output as 'processed_video.avi' with the XVID codec at 20 frames per second.
Converts each frame to grayscale using cv2.cvtColor and applies a threshold at 200 to isolate white points, assuming these are the retroreflective markers.


2️⃣Point Detection:

Uses cv2.findContours with RETR_EXTERNAL and CHAIN_APPROX_SIMPLE to find outer contours, limiting to the first five contours per frame.
For each contour, finds the centroid using cv2.minEnclosingCircle, draws a circle around it, and labels it (e.g., 'Point 1', 'Point 2').
This assumes markers are bright, circular spots, typical in infrared systems, and uses the center of the enclosing circle as the marker's position.


3️⃣Angle Calculation and Storage:

If there are at least three contours, calculates angles for every set of three consecutive points, drawing lines between them and an ellipse to visualize the angle.
Stores the angle data in a Pandas DataFrame with columns for frame number, set number, coordinates of the three points, and the calculated angle.
Saves the DataFrame to 'detected_angles.xlsx' for further analysis.


4️⃣Visualization and Output:

Writes the processed frame to the output video, displaying it with a 0.09-second delay, and allows quitting with 'q'.
Includes visual annotations like circles, labels, and angle text, enhancing interpretability in 'processed_video.avi'.



