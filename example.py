text = "Дамы и господа, началась посадка на рейс Alex-69. Пожалуйста пройдите на гейт 69."

from TeraTTS import TTS

# Optional: Text preprocessing (improves quality)
from ruaccent import RUAccent
accentizer = RUAccent()

# Loading accentuation models and dictionaries
accentizer.load(omograph_model_size='turbo', use_dictionary=True)

# Processing text with stress marks and the letter ё
text = accentizer.process_all(text)
print(f"Text with stress marks and ё: {text}")

# Note: You can find all models at https://huggingface.co/TeraTTS, including the GLADOS model
tts = TTS("TeraTTS/natasha-g2p-vits", add_time_to_end=1.0, tokenizer_load_dict=True) 
# You can adjust 'add_time_to_end' for audio duration, 'tokenizer_load_dict' can be disabled if using RUAccent

# 'length_scale' can be used to slow down the audio for better sound (default 1.1, specified here for example)
audio = tts(text)  
# Create audio. You can add stress marks using '+'
tts.play_audio(audio)  
# Play the created audio
tts.save_wav(audio, "./test.wav")  
# Save the audio to a file

# Create audio and play it immediately
tts(text, play=True)