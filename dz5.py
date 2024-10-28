result = []

def divider(a, b):
    if a < b:
        raise ValueError("a is less than b")
    if b > 100:
        raise IndexError("b is greater than 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except (TypeError, ValueError, IndexError, ZeroDivisionError) as e:
        print(f"Error for {key}/{data[key]}: {e}")

print(result)