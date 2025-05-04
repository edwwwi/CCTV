import cv2

# RTSP camera details
username = "rk11vb"
password = "Joymathew2004"
ip_address = "192.168.18.88"
port = 554
channel = "101"  # You can change to 102, 103, etc., for other channels

# Construct the RTSP URL
rtsp_url = f"rtsp://{username}:{password}@{ip_address}:{port}/Streaming/Channels/{channel}"

# Open the video stream
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

print("Camera stream started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    cv2.imshow("Home Camera", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
