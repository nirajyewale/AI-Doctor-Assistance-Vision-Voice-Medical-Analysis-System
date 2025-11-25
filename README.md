# AI-Doctor-Assistance-Vision-Voice-Medical-Analysis-System
AI-powered doctor assistant with voice and vision. Users can speak or upload audio, submit medical images, and receive professional 2-sentence diagnoses. Uses Groq Whisper for speech-to-text, LLaMA Vision for image analysis, and ElevenLabs for doctor voice responses via Gradio UI.
The AI Doctor Assistance project is an intelligent medical interaction system that combines image analysis, speech-to-text, and AI-generated doctor responses to simulate a realistic medical consultation experience.
Users can speak, upload audio, and submit medical images, and the system responds like a professional doctor—both in text and synthetic voice.

🚀 Features
🔍 1. Medical Image Analysis (Vision AI)

Using the Groq LLaMA Vision model, the system analyzes medical images (such as face skin conditions) and generates concise diagnostic responses.
🎤 2. Voice-to-Text (Patient Speech Input)

The project supports patient audio input via microphone or upload.
Speech is converted to text using Groq Whisper Large V3.

🗣️ 3. Doctor's Voice Output (Text-to-Speech)

The AI doctor’s message is converted into natural speech using ElevenLabs TTS.
Secrets managed via .env file.
🧠 4. Doctor Roleplay System Prompt

You designed a realistic doctor speaking style:

No disclaimers

No special characters or markdown

Only 2 sentences

Direct explanation like a real doctor
(Defined inside gradio_app.py)

🖼 5. Full Voice + Image Gradio UI

The entire interaction—speech input, image upload, diagnosis, and synthesized doctor audio—runs inside a clean Gradio interface:

Implemented in gradio_app.py
📌 Project Workflow

1.User speaks or uploads an audio file

2.System converts speech → text

3.User uploads a medical image

4.LLM analyzes image + patient query

5.AI doctor generates a medically relevant 2-sentence response

6.ElevenLabs converts text → doctor’s voice

7.Output displayed in UI as:

   Text transcription

   Doctor’s written diagnosis

   Audio playback
