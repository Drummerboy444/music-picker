import random

from track import Track


class StateManager:
    def __init__(self, tracks):
        self.tracks = tracks

    def await_next_command(self):
        raw_input = input(":")
        split = raw_input.split()
        command = split[0]
        args = split[1:]
        if command == "help":
            self.help()
        elif command == "print":
            self.print()
        elif command == "add-track":
            self.add_track(args)
        elif command == "remove-track":
            self.remove_track(args)
        elif command == "find-track":
            self.find_track(args)
        elif command == "quit":
            return True
        elif command == "!quit":
            return False
        else:
            print("unknown command")
            print()
        return self.await_next_command()

    def help(self):
        print("Available commands:")
        print("  help                   : help")
        print("  print                  : prints all tracks")
        print("  add-track <url> <tags> : adds a new track with the given url and tags")
        print("  remove-track <id>      : removes the track with the given id")
        print("  find-track <tags>      : finds a track which best matches the given tags")
        print("  quit                   : save and quit the application")
        print("  !quit                  : quit the application without saving")
        print()

    def print(self):
        for track in self.tracks:
            track.print()
            print()

    def add_track(self, args):
        if len(args) <= 1:
            print("not enough args to add a track")
            print()
            return

        id = max(track.id for track in self.tracks) + 1
        url = args[0]
        tags = args[1:]
        self.tracks.append(Track(id, url, tags))
        print()

    def remove_track(self, args):
        if len(args) != 1:
            print("need exactly 1 arg to remove a track")
            print()
            return

        try:
            id = int(args[0])
        except ValueError:
            print("need an integer to remove a track")
            print()
            return

        for track in self.tracks:
            if track.id == id:
                self.tracks.remove(track)
                print()
                return

        print("found no track to remove for the given ID")
        print()

    def find_track(self, tags):
        if (len(tags)) <= 0:
            print("not enough args to find a track")
            print()
            return

        tracks_to_scores = {track: track.get_score(tags) for track in self.tracks}

        max_score = 0
        for track in tracks_to_scores:
            if tracks_to_scores[track] > max_score:
                max_score = tracks_to_scores[track]

        tracks_with_max_score = [track for track in self.tracks if tracks_to_scores[track] == max_score]
        print(random.choice(tracks_with_max_score).url)
        print()
