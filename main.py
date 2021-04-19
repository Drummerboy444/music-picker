from state_manager import StateManager
from track import Track


def parse_raw_track(raw_track):
    split = raw_track.split(",")
    return Track(int(split[0]), split[1], split[2:])


tracks_file = open("data/tracks.txt")
tracks = [parse_raw_track(raw_track) for raw_track in tracks_file.read().split("\n")]
tracks_file.close()

state_manager = StateManager(tracks)
should_save = state_manager.await_next_command()

if should_save:
    tracks_file = open("data/tracks.txt", "w")
    tracks_file.write("\n".join(track.serialize() for track in tracks))
    tracks_file.close()
