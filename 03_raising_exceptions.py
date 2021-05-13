def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("This is not good - Amit ")

a = increment('ad4a0')
print(a)