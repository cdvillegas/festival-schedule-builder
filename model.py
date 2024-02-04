class Artist:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

    def __repr__(self):
        return f"Artist(name={self.name}, rank={self.rank})"


class Show:
    def __init__(self, artist, start_time, end_time):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return f"Show(artist={self.artist}, start_time={self.start_time}, end_time={self.end_time})"


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


