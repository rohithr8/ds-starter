values = [10, 12.5, 9, 18, 14]

mn = values[0]
mx = values[0]

for v in values:
    if v < mn:
        mn = v
    if v > mx:
        mx = v

print("min=", mn)
print("max=", mx)

