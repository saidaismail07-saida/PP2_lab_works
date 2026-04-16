import pygame
import os

class Player:
    def __init__(self, music_folder="music"):
        pygame.mixer.init()

        self.music_folder = music_folder
        self.playlist = self.load_tracks()
        self.index = 0

        self.is_playing = False

    def load_tracks(self):
        tracks = []
        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3") or file.endswith(".ogg"):
                tracks.append(os.path.join(self.music_folder, file))
        tracks.sort()
        return tracks

    def load_current(self):
        if self.playlist:
            pygame.mixer.music.load(self.playlist[self.index])

    def play(self):
        if not self.playlist:
            return

        if not self.is_playing:
            self.load_current()
            pygame.mixer.music.play()
            self.is_playing = True
        else:
            pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.playlist:
            return
        self.index = (self.index + 1) % len(self.playlist)
        self.load_current()
        pygame.mixer.music.play()

    def prev_track(self):
        if not self.playlist:
            return
        self.index = (self.index - 1) % len(self.playlist)
        self.load_current()
        pygame.mixer.music.play()

    def get_current_track(self):
        if not self.playlist:
            return "No music found"
        return os.path.basename(self.playlist[self.index])