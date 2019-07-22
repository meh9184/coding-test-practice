genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]

container = {}

for i, (genre, play) in enumerate(zip(genres, plays)):

    if container.get(genre) is None:
        container[genre] = list()
        container[genre].append([i, play])
    else:
        container[genre].append([i, play])


playList = []

for group in container:
    elements = container[group]
    elements.sort(key=lambda x:x[1], reverse=True)
    total = sum(play for index, play in elements)

    if len(elements) > 1:
        elements = elements[:2]

    playList.append([total, elements])

print(playList)

playList.sort(key=lambda x:x[0], reverse=True)

print(playList)
