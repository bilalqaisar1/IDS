from collections import Counter

def filter_users(tuple_data):

    filtered_data = []
    for t in tuple_data:
        if t[2] > 30:
            if t[3] == "USA" or t[3] == "Canada":
                filtered_data.append(t)
    return filtered_data


def top_10_oldest(tuple_data):

    sorted_users = sorted(tuple_data, key=lambda x: x[2], reverse=True)
    nsorted = []
    counter = 1
    for i in sorted_users:
        nsorted.append(i)
        counter += 1
        if counter == 10:
            break
    return nsorted

def find_repeated_names(tuple_data):
    
    names = [t[1] for t in tuple_data]
    name_counts = Counter(names)
    repeated_names = [name for name, count in name_counts.items() if count > 1]
    return repeated_names
