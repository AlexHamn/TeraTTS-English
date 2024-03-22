# Russian TTS inference
# Installation
You can install the package using pip:
```
pip install TeraTTS
```
Alternatively, you can install it using Git:
```
pip install -e git+https://github.com/Tera2Space/RUTTS#egg=TeraTTS
```
# Errors
1) If you encounter an **installation error** on Windows, simply **download Visual Studio [here](https://visualstudio.microsoft.com/ru/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&cid=2030&passive=false)** and during installation, select the checkbox next to **C++ Desktop development**.

2) If **something doesn't work after installation**, **make sure the module is downloaded in the latest version** (delete and download again) and **also make sure that the model names are available at** https://huggingface.co/TeraTTS.

3) If nothing helps, **seek assistance at https://t.me/teraspace_chat**.
# Usage

```python  
text = "Hello, world!"

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
tts = TTS("TeraTTS/natasha-g2p-vits", add_time_to_end=1.0, tokenizer_load_dict=True) # You can adjust 'add_time_to_end' for audio duration, 'tokenizer_load_dict' can be disabled if using RUAccent


# 'length_scale' can be used to slow down the audio for better sound (default 1.1, specified here for example)
audio = tts(text, length_scale=1.1)  # Create audio. You can add stress marks using '+'
tts.play_audio(audio)  # Play the created audio
tts.save_wav(audio, "./test.wav")  # Save the audio to a file


# Create audio and play it immediately
tts(text, play=True, length_scale=1.1)

```