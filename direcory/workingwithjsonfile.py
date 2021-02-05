import json
from pathlib import Path

'''movies = [
    {"id": 1, "title": 'terminator', 'year': 1233},
    {"id": 2, "title": 'maladorian', 'year': 5233},
    {"id": 1, "title": 'warhero', 'year': 1231}
]

data = json.dumps(movies)
Path('movies.json').write_text(data)
'''

data = Path('movies.json').read_text()
movies = json.loads(data)
# print(movies[0])

for movie in movies:
    print(movie)
