class AudioSystem:
    def start(self):
        print("Audio System Ready")

class VideoSystem:
    def start(self):
        print("Video Ready")

class Decoder:
    def start(self, file_name):
        print(f"Loaded {file_name}")

class Popcorn:
    def start(self):
        print("Throwing Popcorn")

class RemoteFacade:
    def __init__(self):
        self.audio = AudioSystem()
        self.video = VideoSystem()
        self.decode = Decoder()
        self.popcr = Popcorn()

    def play_movie(self, file_name):
        self.audio.start()
        self.video.start()
        self.decode.start("Seven Samurai")
        self.popcr.start()


# ====================================

audio = AudioSystem()
video = VideoSystem()
decode = Decoder()
popcr = Popcorn()

# a lot of work

# audio.start()
# video.start()
# decode.start("w movie")
# popcr.start()

remote = RemoteFacade()
remote.play_movie("Movie")
