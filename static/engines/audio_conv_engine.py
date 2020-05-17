import secrets, os
from pydub import AudioSegment
from config import Config


def convert_audio_mp3(file):
    operator = AudioSegment.from_file(file)
    hash_filename = secrets.token_hex(15)
    save_path = f'{Config.AC_CONVERTED}/{hash_filename}.mp3'
    operator.export(save_path, format='mp3')
    os.remove(file)
    return f'{hash_filename}.mp3'