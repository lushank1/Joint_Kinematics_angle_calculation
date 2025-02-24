import cv2
import numpy as np
import time
import pandas as pd
import os


def calculate_angle(centroid1, centroid2, centroid3):
    vector1 = np.array([centroid1[0] - centroid2[0], centroid1[1] - centroid2[1]])
    vector2 = np.array([centroid3[0] - centroid2[0], centroid3[1] - centroid2[1]])
    dot_product = np.dot(vector1, vector2)
    magnitude1 = np.linalg.norm(vector1)
    magnitude2 = np.linalg.norm(vector2)
    cosine_angle = dot_product / (magnitude1 * magnitude2)
    angle = np.arccos(cosine_angle)
    angle_degrees = np.degrees(angle)
    return angle_degrees


# Load the video
cap = cv2.VideoCapture('v3.mp4')

# Get the width and height of the frames
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
out = cv2.VideoWriter('processed_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (frame_width, frame_height))

# DataFrame to store angles
angles_df = pd.DataFrame(columns=['Frame', 'Set', 'Point1', 'Point2', 'Point3', 'Angle'])

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold the frame to get white points
    _, thresh = cv2.threshold(gray_frame, 200, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # print(len(contours))

    # Ensure only 5 contours are processed
    contours = contours[:5]

    # Draw circles around white points and label them
    for idx, contour in enumerate(contours):
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(frame, center, 5, (0, 255, 0), 5)
        cv2.putText(frame, f'Point {idx + 1}', (center[0] + 10, center[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (255, 0, 0), 2)
        cv2.putText(frame, 'Lushank Shambharkar', (1000, 600), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Join white points with lines and draw angles
    if len(contours) >= 3:
        for i in range(len(contours) - 2):
            set_label = f'Set {i + 1}'

            # Calculate centroids of neighboring contours
            centroid1 = tuple(contours[i].mean(axis=0, dtype="int")[0])
            centroid2 = tuple(contours[i + 1].mean(axis=0, dtype="int")[0])
            centroid3 = tuple(contours[i + 2].mean(axis=0, dtype="int")[0])

            # Draw line between centroids
            cv2.line(frame, centroid1, centroid2, (0, 0, 255), 2)
            cv2.line(frame, centroid2, centroid3, (0, 0, 255), 2)

            # Calculate angle between lines
            angle = calculate_angle(centroid1, centroid2, centroid3)
            cv2.putText(frame, f'{angle:.2f} degrees', centroid2, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Create a new DataFrame for the current angle
            new_data = pd.DataFrame([{
                'Frame': frame_count,
                'Set': set_label,
                'Point1': f'({centroid1[0]}, {centroid1[1]})',
                'Point2': f'({centroid2[0]}, {centroid2[1]})',
                'Point3': f'({centroid3[0]}, {centroid3[1]})',
                'Angle': angle
            }])

            # Append new data to the existing DataFrame
            angles_df = pd.concat([angles_df, new_data], ignore_index=True)

            # Draw arc for angle
            center_angle = centroid2
            radius_angle = 30
            start_angle = int(np.degrees(np.arctan2(centroid1[1] - centroid2[1], centroid1[0] - centroid2[0])))
            end_angle = int(np.degrees(np.arctan2(centroid3[1] - centroid2[1], centroid3[0] - centroid2[0])))
            if start_angle < 0:
                start_angle += 360
            if end_angle < 0:
                end_angle += 360
            cv2.ellipse(frame, center_angle, (radius_angle, radius_angle), 0, start_angle, end_angle, (255, 255, 0), 2)

            # Draw the set label near the middle point of each set
            mid_point = ((centroid2[0] + centroid3[0]) // 2, (centroid2[1] + centroid3[1]) // 2)
            cv2.putText(frame, set_label, mid_point, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    # Write the processed frame to the video file
    out.write(frame)

    # Display the frame
    cv2.imshow('Processed Video', frame)
    time.sleep(0.09)
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Save all angles to an Excel file
angles_df.to_excel('detected_angles.xlsx', index=False)

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Data saved to detected_angles.xlsx and processed video saved as processed_video.avi")
