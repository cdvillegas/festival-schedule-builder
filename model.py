class Artist:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Artist(name={self.name})"


class Show:
    def __init__(self, artist, start_time, end_time, rank):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time
        self.rank = rank

    def __repr__(self):
        return f"Show(artist={self.artist}, start_time={self.start_time}, end_time={self.end_time}, rank={self.rank})"


class Schedule:
    def __init__(self, shows):
        self.shows = shows

    def add_show(self, show):
        self.shows.append(show)

    def __repr__(self):
        return f"Schedule(shows={self.shows})"


class Festival:
    def __init__(self, schedules):
        self.schedules = schedules

    def add_schedule(self, schedule):
        self.schedules.append(schedule)

    def __repr__(self):
        return f"Festival(schedules={self.schedules})"


