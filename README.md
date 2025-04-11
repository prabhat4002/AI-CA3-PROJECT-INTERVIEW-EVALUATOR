# AI-CA3-PROJECT-INTERVIEW-EVALUATOR

Intervalyze: Mock Interview Evaluator
Intervalyze is an AI-powered mock interview evaluation system that provides comprehensive feedback through speech analysis, integrating emotion recognition, transcription, and semantic similarity evaluation.
Overview
Intervalyze analyzes audio responses from mock interviews to deliver objective feedback on both emotional delivery and answer relevance. The system employs advanced AI models to detect emotional states, transcribe spoken responses, and assess the semantic similarity between user responses and reference answers.
Key Features

Speech Emotion Recognition: Identifies 7 distinct emotions (happy, sad, angry, fear, disgust, surprise, neutral) with 94.11% accuracy
Speech-to-Text Transcription: Converts spoken responses to text using Wav2Vec2ForCTC
Semantic Similarity Analysis: Evaluates the relevance of responses against reference answers using BERT embeddings
Personalized Feedback: Generates tailored recommendations based on emotional tone and content accuracy
User-Friendly Interface: Flask-based web application for easy interaction and result visualization

Technology Stack

Speech Emotion Recognition: Fine-tuned Wav2Vec2 model (facebook/wav2vec2-xls-r-300m)
Transcription: Wav2Vec2ForCTC model (facebook/wav2vec2-base-960h)
Semantic Analysis: BERT model (sentence-transformers/bert-base-nli-mean-tokens)
Web Interface: Flask framework
Data Processing: Librosa for audio processing, PyTorch for model implementation

Block Diagram

![image](https://github.com/user-attachments/assets/8846c550-95ea-46bb-a7bb-5d07b6e7e483)
•  Audio Input: The system begins with the user providing an audio sample which serves as the core input for further processing.
•  Emotion Detection: The audio path is processed to detect emotional content using a fine-tuned model, which outputs emotion probabilities.
•  Interview Emotion Mapping: These probabilities are mapped to predefined interview-related emotional categories to contextualize the speaker’s sentiments.
•  Transcription: Simultaneously, the same audio input is converted into textual format through an automatic speech recognition system.
•  Similarity Analysis: The transcribed text is compared against a reference answer using semantic similarity techniques, producing a similarity score and emotion context (e.g., from the TESS dataset).
•  Feedback Generation: Based on the interview emotion mapping and similarity analysis results, the system generates personalized feedback.
•  Output Display: The final emotion labels, similarity scores, and generated feedback are presented to the user through a user-friendly interface


Performance Metrics

Emotion Recognition: 94.11% accuracy, 95.46% precision, 93.94% F1 score
Training Efficiency: Converged within 5 epochs with minimal overfitting

Project Structure




![image](https://github.com/user-attachments/assets/1feeed61-51ac-4554-acd4-4dbd490aac5a)





Data Collection
The implementation of Intervalyze utilized the Toronto Emotional Speech Set (TESS) dataset, which includes 2800 WAV audio files, each labeled with one of seven emotions: happy, sad, angry, fear, disgust, surprise, or neutral. With 400 files per emotion, the dataset offers balanced representation, critical for robust model training. Recorded at a 24.414 kHz sampling rate, the files were resampled to 16 kHz during preprocessing to meet model requirements. The dataset was divided into 2240 training and 560 testing instances, supporting the development and evaluation of the speech emotion recognition component. For transcription and semantic similarity, pre-trained models were directly integrated, leveraging their generalized performance without additional data collection.
![image](https://github.com/user-attachments/assets/0a20d368-aaaa-4209-9a5e-af0dd74bcd3d)


Data Preprocessing 
The TESS dataset provides the following attributes:
No.	Feature	Description
1	Audio File Path	Path to WAV file (e.g., YAF_home_fear.wav)
2	Emotion Label	Happy, sad, angry, fear, disgust, surprise, neutral
3	Sampling Rate (Original)	24.414 kHz
Preprocessing focused on preparing audio for model compatibility. Using Librosa, WAV files were loaded at 16 kHz and converted to float32 arrays normalized between -1.0 and 1.0. For emotion recognition, a custom dataset class mapped emotions to integer labels (e.g., happy=0, sad=1), structuring inputs for the Wav2Vec2 model (facebook/wav2vec2-xls-r-300m). The transcription component used the same audio arrays, processed by a pre-trained Wav2Vec2ForCTC model (facebook/wav2vec2-base-960h) without further modification. For semantic similarity, transcriptions were tokenized and embedded via a BERT model (sentence-transformers/bert-base-nli-mean-tokens), compared against a reference string (“Java is a programming language”) using cosine similarity.


![image](https://github.com/user-attachments/assets/316c8bbe-6111-4845-892b-11d9ccf6e793)

Limitations

Currently optimized for WAV audio format
Requires a minimum of 1-second audio input
Primarily designed for English language responses
Single reference answer for similarity comparison

Future Improvements

Multi-language support for global accessibility
Domain-specific reference libraries for various industries
Integration of non-verbal communication analysis
Mobile application development for on-the-go practice
Real-time feedback during live mock interviews

Acknowledgments

Toronto Emotional Speech Set (TESS) for providing the dataset
HuggingFace models and transformers library
