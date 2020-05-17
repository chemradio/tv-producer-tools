from pydub import AudioSegment


sound = AudioSegment.from_file("audio/gs-16b-1c-8000hz.amr")
sound.export('converted.mp3', format='mp3')