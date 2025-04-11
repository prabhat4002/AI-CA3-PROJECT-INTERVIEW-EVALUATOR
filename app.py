from flask import Flask, request, render_template
import os
import numpy as np
import librosa  # Add this import

app = Flask(__name__)

from emotion import predict_emotion
from transcribe import transcribe_audio
from similarity import compute_similarity

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'audio' not in request.files:
            return render_template('index.html', error="No file uploaded")
        
        audio_file = request.files['audio']
        if audio_file.filename == '':
            return render_template('index.html', error="No file selected")
        if not audio_file.filename.lower().endswith('.wav'):
            return render_template('index.html', error="Upload .wav format only")
        
        audio_path = "temp_audio.wav"
        audio_file.save(audio_path)

        # Check audio duration
        audio, sr = librosa.load(audio_path, sr=16000)
        duration = librosa.get_duration(y=audio, sr=sr)
        if duration < 1.0:
            if os.path.exists(audio_path):
                os.remove(audio_path)
            return render_template('index.html', error="Audio too short - Please record at least 1 second")

        # Rest of the processing
        predicted_emotion, probabilities = predict_emotion(audio_path)
        transcription = transcribe_audio(audio_path)
        similarity_score = compute_similarity(transcription)
        
        # [Your existing emotion mapping and feedback logic]
        rounded_probs = [round(p, 4) for p in probabilities]
        prob_sum = sum(rounded_probs)
        if prob_sum != 0:
            normalized_probs = [p / prob_sum for p in rounded_probs]
        else:
            normalized_probs = rounded_probs
        
        interview_emotions = {
            'nervous': max(probabilities[0], probabilities[4]),
            'confident': max(probabilities[6], probabilities[5]),
            'hesitant': max(probabilities[3], probabilities[4]),
            'agitated': max(probabilities[1], probabilities[2])
        }
        predicted_interview_emotion = max(interview_emotions, key=interview_emotions.get)
        
        similarity_feedback = ""
        if similarity_score < 0.3:
            similarity_feedback = "Your answer is off-topic. Improve clarity and match the question."
        elif 0.3 <= similarity_score < 0.7:
            similarity_feedback = "Getting closer! Work on aligning your answer with the question."
        else:
            similarity_feedback = "Spot on! Your answer matches the question well."

        emotion_feedback = ""
        if predicted_interview_emotion == 'nervous':
            emotion_feedback = "You sound nervous. Try to relax and speak more confidently."
        elif predicted_interview_emotion == 'confident':
            emotion_feedback = "Great job! You sound confident and in control."
        elif predicted_interview_emotion == 'hesitant':
            emotion_feedback = "You seem hesitant. Practice speaking more decisively."
        elif predicted_interview_emotion == 'agitated':
            emotion_feedback = "You sound agitated. Stay calm and composed for a better impression."
        
        feedback = f"{similarity_feedback} {emotion_feedback}"
        
        if os.path.exists(audio_path):
            os.remove(audio_path)

        return render_template('index.html', emotion=predicted_emotion, probabilities=normalized_probs, 
                             emotion_labels=['fear', 'angry', 'disgust', 'neutral', 'sad', 'ps', 'happy'], 
                             transcription=transcription, similarity_score=similarity_score,
                             interview_emotion=predicted_interview_emotion, interview_probabilities=interview_emotions,
                             feedback=feedback)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)