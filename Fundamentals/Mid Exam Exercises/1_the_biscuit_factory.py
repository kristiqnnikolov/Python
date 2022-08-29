from math import floor

buscuits = int(input())
workers = int(input())
others = int(input())
total = 0
daily = buscuits * workers
for day in range(1, 31):
    if day % 3 == 0:
        total += floor(daily * 0.75)
    else:
        total += floor(daily)

diff = total - others
percent = abs(diff / others * 100)
print(f"You have produced {total} biscuits for the past month.")
if total > others:
    print(f"You produce {percent:.2f} percent more biscuits.")
else:
    print(f"You produce {percent:.2f} percent less biscuits.")