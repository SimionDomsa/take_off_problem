from pathlib import Path
from collections import defaultdict
from datetime import datetime

families = defaultdict(list)

with open(Path('nume.txt'), 'r') as fd:
    file_lines = fd.readlines()
if not (number_of_entries := file_lines.pop(0)):
    raise ValueError("Incorrect file format")

for person in file_lines:
    try:
        name, surname, date = person.split()
    except ValueError:
        raise ValueError("Entries should be in the order of surname name date")

    dob = datetime.strptime(date, '%Y-%m-%d')
    families[surname].append((name, dob))
for surname, members in sorted(families.items(), key=lambda x: len(x[1]), reverse=True):
    print(f'{surname}: ', end='')
    for name, dob in sorted(members, key=lambda x: x[1]):
        print(f'{name} ', end='')
    print()
