import cv2
import webbrowser
import time

try:
    import mediapipe as mp
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils
except ImportError:
    print("❌ Error: MediaPipe library not found. Run the installation command first!")
    exit()

# Start your Webcam feed
cap = cv2.VideoCapture(0)

# Anti-spam protection setup
last_trigger_time = 0
cooldown_seconds = 4  

print("🚀 System Active! Show 1 to 5 fingers to your camera.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("❌ Camera frame could not be read.")
        break

    # Mirror view
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    
    # Process the frame with MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    status_text = "Scanning..."

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Tracking IDs for fingertips
            tip_ids = [4, 8, 12, 16, 20]
            fingers = []

            # Check Thumb (horizontal calculation)
            if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0] - 1].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Check remaining 4 fingers (Vertical check: Tip vs Joint)
            for id in range(1, 5):
                if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
                    fingers.append(1)  
                else:
                    fingers.append(0)  

            total_fingers = fingers.count(1)
            current_time = time.time()

            # Execute automation commands based on finger counts
            if current_time - last_trigger_time > cooldown_seconds:
                if total_fingers == 1:
                    status_text = "Opening Google..."
                    webbrowser.open("https://google.com")
                    last_trigger_time = current_time
                elif total_fingers == 2:
                    status_text = "Opening ChatGPT..."
                    webbrowser.open("https://chatgpt.com")
                    last_trigger_time = current_time
                elif total_fingers == 3:
                    status_text = "Opening Gemini..."
                    webbrowser.open("https://google.com")
                    last_trigger_time = current_time
                elif total_fingers == 4:
                    status_text = "Opening Gmail..."
                    webbrowser.open("https://gmail.com")
                    last_trigger_time = current_time
                elif total_fingers == 5:
                    status_text = "Opening New Tab..."
                    # Opens a clean blank browser tab orientation
                    webbrowser.open("about:blank") 
                    last_trigger_time = current_time
            else:
                status_text = "Cooldown active. Lower your hand."

    cv2.putText(frame, f"System: {status_text}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    
    cv2.imshow("AI Gesture Web Launcher", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import cv2
import webbrowser
import time

try:
    import mediapipe as mp
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils
except ImportError:
    print("❌ Error: MediaPipe library not found. Run the installation command first!")
    exit()

# Start your Webcam feed
cap = cv2.VideoCapture(0)

# Anti-spam protection setup
last_trigger_time = 0
cooldown_seconds = 4  

print("🚀 System Active! Show 1 to 5 fingers to your camera.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("❌ Camera frame could not be read.")
        break

    # Mirror view
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    
    # Process the frame with MediaPipe
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    status_text = "Scanning..."

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Tracking IDs for fingertips
            tip_ids = [4, 8, 12, 16, 20]
            fingers = []

            # Check Thumb (horizontal calculation)
            if hand_landmarks.landmark[tip_ids[0]].x > hand_landmarks.landmark[tip_ids[0] - 1].x:
                fingers.append(1)
            else:
                fingers.append(0)

            # Check remaining 4 fingers (Vertical check: Tip vs Joint)
            for id in range(1, 5):
                if hand_landmarks.landmark[tip_ids[id]].y < hand_landmarks.landmark[tip_ids[id] - 2].y:
                    fingers.append(1)  
                else:
                    fingers.append(0)  

            total_fingers = fingers.count(1)
            current_time = time.time()

            # Execute automation commands based on finger counts
            if current_time - last_trigger_time > cooldown_seconds:
                if total_fingers == 1:
                    status_text = "Opening Google..."
                    webbrowser.open("https://google.com")
                    last_trigger_time = current_time
                elif total_fingers == 2:
                    status_text = "Opening ChatGPT..."
                    webbrowser.open("https://chatgpt.com")
                    last_trigger_time = current_time
                elif total_fingers == 3:
                    status_text = "Opening Gemini..."
                    webbrowser.open("https://google.com")
                    last_trigger_time = current_time
                elif total_fingers == 4:
                    status_text = "Opening Gmail..."
                    webbrowser.open("https://gmail.com")
                    last_trigger_time = current_time
                elif total_fingers == 5:
                    status_text = "Opening New Tab..."
                    # Opens a clean blank browser tab orientation
                    webbrowser.open("about:blank") 
                    last_trigger_time = current_time
            else:
                status_text = "Cooldown active. Lower your hand."

    cv2.putText(frame, f"System: {status_text}", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    
    cv2.imshow("AI Gesture Web Launcher", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()