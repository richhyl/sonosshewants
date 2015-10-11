from soco import SoCo
import random
import time

if __name__ == '__main__':
    sonos = SoCo('192.168.1.102') # Pass in the IP of your Sonos speaker
    # You could use the discover function instead, if you don't know the IP

    # Pass in a URI to a media file to have it streamed through the Sonos
    # speaker
    sonos.play_uri(
        'http://archive.org/download/TenD2005-07-16.flac16/TenD2005-07-16t10Wonderboy_64kb.mp3')

    track = sonos.get_current_track_info()

    print track['title']

    sonos.pause()

    # Play a stopped or paused track
    sonos.play()