from collections import Counter

data = input(": ").split()

def mode(given_lst):

    # Count repetition
    count = Counter(given_lst)

    max_count = max(count.values())

    # Search multiple modes
    modes = [key for key, value in count.items() if value == max_count]

    return f"Mode(s): {modes}: {max_count} times"

print(mode(data))


