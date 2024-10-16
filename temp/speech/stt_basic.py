from google.oauth2 import service_account
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
from google.api_core.client_options import ClientOptions
import base64



PROJECT_ID = 'hy-ai-demo'

cred = service_account.Credentials.from_service_account_file(
    '/home/gcpvm/sakey/hy-ai-demo.json')

def quickstart_v2(audio_file: str, sourceLang: str, targetLang: str) -> cloud_speech.RecognizeResponse:
    """Transcribe an audio file.
    Args:
        audio_file (str): Path to the local audio file to be transcribed.
    Returns:
        cloud_speech.RecognizeResponse: The response from the recognize request, containing
        the transcription results
    """
    # Reads a file as bytes
    with open(audio_file, "rb") as f:
        audio_content = f.read()

    # Instantiates a client
    client = SpeechClient(credentials = cred, client_options=ClientOptions(api_endpoint='us-central1-speech.googleapis.com'))

    print(sourceLang, targetLang)

    config = cloud_speech.RecognitionConfig(
        auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
        language_codes=[sourceLang],
        model="chirp_2",
        translation_config=cloud_speech.TranslationConfig(
            target_language=targetLang),
    )

    request = cloud_speech.RecognizeRequest(
        recognizer=f"projects/{PROJECT_ID}/locations/us-central1/recognizers/_",
        config=config,
        content=audio_content,
    )

    # Transcribes the audio into text
    response = client.recognize(request=request)



    for result in response.results:
        print(f"Transcript: {result.alternatives[0].transcript}")

    return response

sourceLangList = ['ar-EG']
targetLangList = ['en-US']

for source in sourceLangList:
    for target in targetLangList:
        try:
            print('----------------')
            quickstart_v2('/home/gcpvm/gcp/ai/demo/i/23102176033911560.mp3', source, target)
        except Exception:
            pass
