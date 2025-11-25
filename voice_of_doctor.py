# Step 1-a: Setup Text to Speech (TTS) model with gTTS 
import os
import subprocess
import platform
from gtts import gTTS
from elevenlabs import ElevenLabs

ELEVEN_LABS_API_KEY = os.environ.get("ELEVEN_LABS_API_KEY")

# ---------------- gTTS ----------------
def text_to_speech_with_gtts(input_text, output_filepath):
    language = 'en'
    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)

    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['start', output_filepath], shell=True)  # Windows Media Player
        elif os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        else:  # Linux and others
            subprocess.run(["xdg-open", output_filepath])       
    except Exception as e:
        print(f"Error playing audio: {e}")


# ---------------- ElevenLabs ----------------
def text_to_speech_with_elevenlabs(input_text, output_filepath):
    client = ElevenLabs(api_key=ELEVEN_LABS_API_KEY)

    # ✅ Use new API method
    response = client.text_to_speech.convert(
        voice_id="EXAVITQu4vr4xnSDxMaL",      # name = "Bella"      
        model_id="eleven_turbo_v2_5",  # correct model id
        text=input_text
    )

    # The response is a stream of audio chunks
    with open(output_filepath, "wb") as f:
        for chunk in response:
            f.write(chunk)

    os_name = platform.system()
    try:
        if os_name == "Windows":
            subprocess.run(['start', output_filepath], shell=True)
        elif os_name == "Darwin":
            subprocess.run(['afplay', output_filepath])
        else:
            subprocess.run(["xdg-open", output_filepath])       
    except Exception as e:
        print(f"Error playing audio: {e}")


# ---------------- Run ----------------
input_text = "Hello, I am your virtual doctor autoplay version!"
#text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_test_autoplay.mp3")
text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_test_autoplay.mp3")
