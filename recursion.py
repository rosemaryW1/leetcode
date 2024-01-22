def countdown(i):
    print(i)
    # base case
    if i <= 0:
        return
    else:
        # recursive case
        countdown(i-1)

countdown(22)