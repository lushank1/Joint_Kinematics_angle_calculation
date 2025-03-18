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


![Untitled video - Made with Clipchamp (2)](https://github.com/user-attachments/assets/7a088d55-61c5-4264-9b77-47902ebf4572)


SLOPE WALKING:


![Untitled video - Made with Clipchamp (3)](https://github.com/user-attachments/assets/1858ba16-a260-43e9-8be7-e541cc041415)



STARICASE ASCEND:



![Untitled video - Made with Clipchamp (4)](https://github.com/user-attachments/assets/fa301ad3-8bd2-46bc-a71e-e98d8d1d000b)









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


🚀 Meet Lushank Shambharkar – A passionate researcher in Production & Industrial Engineering, specializing in biomechanics & gait analysis!
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖


🎓 Education:

📌 PhD (Ongoing) – Visvesvaraya National Institute of Technology

📌 M.Tech  – Indian Institute of Engineering Science and Technology

📌 B.E.  – RTMNU, JD College of Engineering & Management

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

💼 Experience:

🔹 Industrial project on Lean Manufacturing at SABOO PLASTICS PVT. LTD.


🔹 Training as System Engineer at INFOSYS LIMITED

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

🛠 Technical Skills:

✅ AutoCAD, Creo, Catia

✅ MATLAB, Python, Java

✅ OpenSim, Minitab, Technomatix

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

📢 Notable Research & Publications:

📌 Joint trajectory & kinematics on adjustable staircases (PhD)

📌 Accuracy of optical motion capture systems (IEOM Conference)

📌 Biomechanics of joints & orthopaedic implants (NPTEL)

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

🏆 Workshops & Certifications:

🔹 Digital Manufacturing & Design (Coursera)

🔹 AI & Computer Vision Trends (ATAL Academy) 

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

⚽ Extracurriculars:

🏅 Football & Basketball competitions at NIT & VNIT


➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

💡 Passionate about innovation, problem-solving, and research in biomechanics & motion capture accuracy.

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

📧 Connect with Lushank:

🔗 LinkedIn: https://www.linkedin.com/in/lushank-shambharkar-874a64241/

📩 Email: lushank@outlook.com

🤖 Github: https://github.com/lushank1

🧑‍💻 Hackerank: https://www.hackerrank.com/profile/lushank


#Engineering #Biomechanics #MotionCapture #Research #Innovation 🚀
