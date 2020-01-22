import os
from google.cloud import texttospeech

# Set authentication creds.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.getcwd(), 'gcp-service-acct-key.json')

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
text = input("Please enter string to be digitised: ")
synthesis_input = texttospeech.types.SynthesisInput(text=text)

# Build the voice request, select the language code and the ssml voice gender
# Reference: https://cloud.google.com/text-to-speech/docs/voices
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-AU',
    name='en-AU-Wavenet-B',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE
)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# The response's audio_content is binary.
with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')
