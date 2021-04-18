from state_manager import StateManager
from track import Track


def parse_raw_track(raw_track):
    split = raw_track.split(",")
    return Track(int(split[0]), split[1], split[2:])


with open('data/tracks.txt') as raw_tracks, open('data/tags.txt') as raw_tags:
    tracks = [parse_raw_track(raw_track) for raw_track in raw_tracks.read().split("\n")]
    tags = raw_tags.read().split("\n")


state_manager = StateManager(tracks)
state_manager.await_next_command()
