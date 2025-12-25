def stats(values):
    total = 0.0
    mn = values[0]
    mx = values[0]

    for v in values:
        total = total + v
        if v < mn:
            mn = v
        if v > mx:
            mx = v

    mean = total / len(values)
    return {"count": len(values), "total": total, "mean": mean, "min": mn, "max": mx}


values = [10, 12.5, 9, 18, 14]
result = stats(values)

print(result)
print("mean=", result["mean"])
