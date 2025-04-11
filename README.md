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
