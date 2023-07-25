from gtts import gTTS
from find_memes import Meme

def say_meme(meme: Meme) -> None:
    tts = gTTS(meme.caption, lang='en')
    tts.save(f'Resources/Audio/{meme.id}.mp3')
