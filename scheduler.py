from model import Schedule
from random import choice

class Scheduler:
    def __init__(self, schedule):
        self.schedule = schedule

    def optimize_schedule(self, iterations=1000):
        current_schedule = Schedule([])
        current_rank = self.calculate_total_rank(current_schedule)

        for i in range(iterations):
            new_schedule = self.add_or_swap_show(current_schedule)
            if self.is_schedule_valid(new_schedule):
                new_rank = self.calculate_total_rank(new_schedule)
                if new_rank > current_rank:
                    current_schedule, current_rank = new_schedule, new_rank
        
        current_schedule.shows.sort(key=lambda show: show.start_time)

        return current_schedule
    
    def add_or_swap_show(self, schedule):
        current_rank = self.calculate_total_rank(schedule)  # Pass Schedule object

        # Make a deep copy of the schedule to ensure changes don't affect the original
        new_schedule = Schedule(schedule.shows[:])

        # Attempt to add a new show if schedule is not full
        if len(schedule.shows) < len(self.schedule.shows):
            potential_new_shows = [show for show in self.schedule.shows if show not in schedule.shows]
            if potential_new_shows:
                new_show = choice(potential_new_shows)
                new_schedule.shows.append(new_show)
                new_schedule_rank = self.calculate_total_rank(new_schedule)  # Pass Schedule object
                if self.is_schedule_valid(new_schedule) and new_schedule_rank > current_rank:  # Pass Schedule object
                    return new_schedule  # Successfully added a new show
                else:
                    new_schedule.shows.remove(new_show)  # Revert attempted addition if not valid or not improving rank

        # If adding a new show isn't possible or doesn't improve rank, attempt to swap a show with a similar time
        for index, schedule_show in enumerate(schedule.shows):
            similar_time_shows = [
                show for show in self.schedule.shows 
                if show not in new_schedule.shows and abs(self.timedelta_hours(show.start_time - schedule_show.start_time)) <= 3
            ]
            for show_to_swap_in in similar_time_shows:
                # Attempt the swap
                temp_schedule = Schedule(new_schedule.shows[:])
                temp_schedule.shows[index] = show_to_swap_in  # Replace the show at the specific index
                if self.is_schedule_valid(temp_schedule) and self.calculate_total_rank(temp_schedule) > current_rank:  # Pass Schedule object
                    return temp_schedule  # Successfully swapped

        # Return the original schedule if no valid addition or swap is made that improves the rank
        return schedule

    @staticmethod
    def calculate_total_rank(schedule):
        return sum(show.rank for show in schedule.shows)

    @staticmethod
    def is_schedule_valid(schedule):
        sorted_shows = sorted(schedule.shows, key=lambda show: show.start_time)
        for i in range(1, len(sorted_shows)):
            if sorted_shows[i].start_time < sorted_shows[i-1].end_time:
                return False
        return True

    @staticmethod
    def timedelta_hours(td):
        return td.total_seconds() / 3600
