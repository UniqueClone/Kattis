num_villagers = int(input())

num_evenings = int(input())

villagers_songs = []

# Add villagers to array
for i in range(1, num_villagers+2):
    villagers_songs.append([i])

# Add a false for each night of music for each villager
for i in range(num_villagers+1):
    for j in range(1, num_evenings+1):
        villagers_songs[i].append(False)

def night():
