import cv2

def display_cctv_feed():
    # Camera details
    ip = "192.168.18.88"
    username = "admin"
    password = "admin123"
    
    # RTSP URL for Hikvision
    rtsp_url = f"rtsp://{username}:{password}@{ip}/ISAPI/Streaming/Channels/101"
    
    # Create video capture object
    cap = cv2.VideoCapture(rtsp_url)
    
    if not cap.isOpened():
        print("Error: Could not open video stream")
        print("Possible issues:")
        print("1. Incorrect credentials")
        print("2. RTSP not enabled on camera")
        print("3. Network connectivity problem")
        return
    
    print("Successfully connected to CCTV. Press 'q' to quit.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame")
            break
            
        # Display the frame
        cv2.imshow('Hikvision CCTV Feed', frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release resources
    cap.release()
    cv2.destroyAllWindows()

# Run the function
display_cctv_feed()