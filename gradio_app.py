# Voicebot UI with Gradio
import os
import gradio as gr

from brain_of_doctor import encode_image, analyze_image_with_query 
from voice_of_patient import transcribe_with_groq
from voice_of_doctor import text_to_speech_with_elevenlabs

system_prompt = """You are to roleplay as a professional doctor. This is only for learning purposes.
When analyzing an image or a description, identify if there is anything medically abnormal.
If you suggest a differential diagnosis, also mention possible remedies or treatments in a concise way.
Do not use any special characters, numbers, or markdown formatting in your response.
Your reply must be written in long paragraph form, but limited to no more than 2 sentences.
Never say things like 'In the image I see...' or 'As an AI model...'. Instead, speak directly as a doctor would to a patient, for example 'With what I see, you have...'.
Begin your answer immediately without preamble."""

def process_inputs(audio_filepath, image_filepath):
    # Speech-to-text
    speech_to_text_output = None
    if audio_filepath:
        speech_to_text_output = transcribe_with_groq(
            GROQ_API_KEY=os.environ.get("GROQ_API_KEY"),
            stt_model="whisper-large-v3",
            audio_filepath=audio_filepath
        )
    else:
        speech_to_text_output = "No voice input provided."

    # Image analysis
    if image_filepath:
        doctor_response = analyze_image_with_query(
            query=system_prompt + speech_to_text_output,
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            encode_image=encode_image(image_filepath)
        )
    else:
        doctor_response = "No image provided for analysis."

    # Text-to-speech
    voice_of_doctor = text_to_speech_with_elevenlabs(doctor_response, "final.mp3")

    return speech_to_text_output, doctor_response, voice_of_doctor

# Gradio interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone", "upload"], type="filepath", label="Speak or Upload Audio"),
        gr.Image(type="filepath", label="Upload an Image"),
    ],
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio(label="Doctor's Voice", type="filepath")
    ],
    title="AI Doctor with Vision and Voice",
    description="Interact with an AI Doctor using voice and images. The AI can analyze images and respond with synthesized speech.",
)

iface.launch(debug=True)
