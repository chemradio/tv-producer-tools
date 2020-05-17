from ytdl import YtdlEngine

url = 'https://www.facebook.com/chemradio/videos/10221428232550896/'

ydl = YtdlEngine()
print(ydl.go_ahead(url=url))