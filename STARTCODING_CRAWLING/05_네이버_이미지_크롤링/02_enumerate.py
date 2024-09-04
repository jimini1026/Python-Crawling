animals = ["목도리도마뱀", "개코원숭이", "알파카"]

i = 1
for animal in animals:
    print(i, animal)
    i += 1

for i, animal in enumerate(animals, 1):
    print(i, animal)