# Joint_Kinematics_angle_calculation
This script is designed to analyze videos by detecting white points, calculating angles between consecutive points, and saving the results for further study. It's particularly helpful for tracking motion in fields like science or engineering.
⏺️Overview
  1️⃣This Python script is designed to process videos from infrared motion capture systems, where retroreflective markers are attached to the body. It provides a simple way to detect these markers, calculate angles between        them, and save the results, avoiding the need for costly software typically used for such tasks.

⏺️What the Script Does
  1️⃣Marker Detection: The script loads a video, converts frames to grayscale, and uses thresholding to identify white points, which are the markers.
  2️⃣Angle Calculation: It finds up to five markers per frame, calculates the angle at the middle point for every set of three consecutive markers, and stores this data.
  3️⃣Output: Results are saved in an Excel file ('detected_angles.xlsx') and a processed video ('processed_video.avi') with visual annotations like circles and angle labels.

⏺️How to Use
Ensure you have Python with OpenCV, NumPy, and Pandas installed. Place your video (named 'Descend-without-trajectories.mp4') in the same folder, then run the script. Change the filename in the code if using a different video.
Unexpected Detail
An interesting aspect is that the script labels markers based on their order in each frame, which might lead to inconsistent angle calculations if markers move and their order changes, potentially affecting accuracy for dynamic motions.
