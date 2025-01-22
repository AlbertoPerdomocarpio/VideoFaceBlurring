import cv2
import os


def extract_frames(video_path, output_folder):
    """Estrae i frame dal video e li salva nella cartella output_folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    cap = cv2.VideoCapture(video_path)
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_path, frame)
        frame_count += 1

    cap.release()
    return frame_count


def process_frames(input_folder, output_folder):
    """Applica la censura a tutti i frame nella cartella input_folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    for frame_file in sorted(os.listdir(input_folder)):
        input_path = os.path.join(input_folder, frame_file)
        output_path = os.path.join(output_folder, frame_file)

        frame = cv2.imread(input_path)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            face = frame[y:y+h, x:x+w]
            face = cv2.GaussianBlur(face, (99, 99), 30)
            frame[y:y+h, x:x+w] = face

        cv2.imwrite(output_path, frame)


def combine_frames(input_folder, output_video_path, fps, width, height):
    """Combina i frame processati in un video finale."""
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    for frame_file in sorted(os.listdir(input_folder)):
        frame_path = os.path.join(input_folder, frame_file)
        frame = cv2.imread(frame_path)
        out.write(frame)

    out.release()


def censor_faces(input_path, output_path):
    temp_frames_input = "app/temp_frames/input"
    temp_frames_output = "app/temp_frames/output"

    frame_count = extract_frames(input_path, temp_frames_input)

    cap = cv2.VideoCapture(input_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()

    process_frames(temp_frames_input, temp_frames_output)


    combine_frames(temp_frames_output, output_path, fps, width, height)

    for folder in [temp_frames_input, temp_frames_output]:
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))
        os.rmdir(folder)

