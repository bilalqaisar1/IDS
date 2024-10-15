def Unique_Users(tuple_data):
    l = []
    for _ in tuple_data:
        if _[1] not in l:
            l.append(_[1])
    return len(l)


def User_IDs(tuple_data):    
    l = []
    for _ in tuple_data:
        l.append(_[1])
    return l


def Tans_IDs(tuple_data):    
    l = []
    for _ in tuple_data:
        l.append(_[0])
    return l


def highest_trans(tuple_data):
    return max(tuple_data, key=lambda t: t[2])


users = [
    (1001, 501, 150.50, '2023-10-01 10:00:00'),
    (1002, 502, 200.75, '2023-10-01 10:05:00'),
    (1003, 503, 120.00, '2023-10-01 10:10:00'),
    (1004, 501, 300.00, '2023-10-01 10:15:00'),
    (1005, 504, 50.25, '2023-10-01 10:20:00'),
]
print()
output = Unique_Users(users)
print("Unique Users: ",output)
out = User_IDs(users)
print("User IDs: ",out)
out = Tans_IDs(users)
print("Transaction IDs: ",out)
out = highest_trans(users)
print("Highest Transaction: ",out) 
print()