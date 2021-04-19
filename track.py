class Track:
    def __init__(self, id, url, tags):
        self.id = id
        self.url = url
        self.tags = tags

    def print(self):
        print(f"ID: {self.id}")
        print(f"URL: {self.url}")
        print(f"Tags: {' '.join(self.tags)}")

    def get_score(self, tags):
        matching_tag_count = len([tag for tag in tags if tag in self.tags])
        total_tag_count = len(set(tags + self.tags))
        return matching_tag_count / total_tag_count

    def serialize(self):
        return f"{self.id},{self.url},{','.join(self.tags)}"
