from random import randint, sample, choice

class Artist:
    def __init__(self, name, start, end, rank):
        self.name = name
        self.start = start
        self.end = end
        self.rank = rank

    def __repr__(self):
        return f"{self.name} (Start: {self.start}, End: {self.end}, Rank: {self.rank})"

def create_artists(n=140):
    artists = []
    # The top 10% good artists you really want to see
    for i in range(int(n * 0.1)):
        start = randint(0, 22)
        end = start + 2 # Ensure T2 - T1 < 10
        artists.append(Artist(f"Artist {i+1}", start, end, randint(4, 5)))

    # The other 90% of artists you are less excited about
    for i in range(int(n * 0.9)):
        start = randint(0, 22)
        end = start + 2 # Ensure T2 - T1 < 10
        artists.append(Artist(f"Artist {i+1}", start, end, randint(1, 3)))
    return artists

def calculate_total_rank(schedule):
    return sum(artist.rank for artist in schedule)

def is_schedule_valid(schedule):
    schedule.sort(key=lambda x: x.start)  # Sort by start time for easier validation
    for i in range(1, len(schedule)):
        if schedule[i].start < schedule[i-1].end:  # Check for overlap
            return False
    return True

def add_or_swap_artist(schedule, artists):
    new_schedule = schedule[:]
    
    # First, try to add a new artist if the schedule is not full
    if len(schedule) < len(artists):
        potential_new_artists = [artist for artist in artists if artist not in schedule]
        if potential_new_artists:
            new_artist = choice(potential_new_artists)
            new_schedule.append(new_artist)  # Attempt to add a new artist
            new_schedule.sort(key=lambda artist: artist.start)  # Sort after adding
            if is_schedule_valid(new_schedule):
                return new_schedule  # Return if valid after adding and sorting

    # If adding a new artist isn't possible, try swapping an artist from the schedule with one from the artists array
    new_schedule = schedule[:]

    # Randomly choose an artist from the current schedule to attempt a swap
    schedule_artist = choice(new_schedule)

    # Find artists not in the schedule with start times within T=2 of the chosen artist
    similar_time_artists = [artist for artist in artists if artist not in new_schedule and abs(artist.start - schedule_artist.start) <= 2]

    if similar_time_artists:
        # If there are any artists with a similar start time, choose one to swap
        artist_to_swap_in = choice(similar_time_artists)
        
        # Perform the swap
        new_schedule.remove(schedule_artist)
        new_schedule.append(artist_to_swap_in)
        new_schedule.sort(key=lambda artist: artist.start)  # Sort after swapping
        
        if is_schedule_valid(new_schedule):
            # Return the new schedule if it's valid after the swap
            return new_schedule
        else:
            # If the swap results in an invalid schedule, revert the changes
            new_schedule.remove(artist_to_swap_in)
            new_schedule.append(schedule_artist)
            new_schedule.sort(key=lambda artist: artist.start)

    return schedule  # Return the original schedule if no valid addition or swap is made


def optimize_schedule(initial_schedule, artists, iterations=100000):
    current_schedule = initial_schedule
    current_rank = calculate_total_rank(current_schedule)

    for _ in range(iterations):
        new_schedule = add_or_swap_artist(current_schedule, artists)
        if is_schedule_valid(new_schedule):
            new_rank = calculate_total_rank(new_schedule)
            if new_rank > current_rank:
                current_schedule, current_rank = new_schedule, new_rank

    return current_schedule

# Create artists
artists = create_artists()

trials = 10
optimized_schedules = []
for trial_index in range(trials):
    optimized_schedule = optimize_schedule([], artists, iterations=100000)
    total_rank = calculate_total_rank(optimized_schedule)
    optimized_schedules.append((total_rank, optimized_schedule))
    print(f'Rank for trial {trial_index+1}: {total_rank}')

best_schedule = max(optimized_schedules, key=lambda t: t[0])[1]
print(f'\nBest Schedule Rank: {calculate_total_rank(best_schedule)}')
print(f'Total Artist Rank: {calculate_total_rank(artists)}')
for artist in best_schedule:
    print(artist)


