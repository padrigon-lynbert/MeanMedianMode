from collections import Counter

# data = [10,30,30,30,30,20,20,20,20]
def mode(given_lst):

    # Count repetition
    count = Counter(given_lst)

    max_count = max(count.values())

    # Search multiple modes
    modes = [key for key, value in count.items() if value == max_count]

    print(f"Mode(s): {modes}: {max_count} times")

# mode(data)