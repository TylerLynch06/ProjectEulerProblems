values = []

for a in range(2,101):
    for b in range(2,101):
        values.append(a**b)
values = set(values)
print(len(values))
