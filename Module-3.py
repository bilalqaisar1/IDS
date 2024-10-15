def common_users(page_a, page_b):
    return page_a.intersection(page_b)

def non_common(page_a, page_c):
    return page_a.symmetric_difference(page_c)

def update_page_a_with_new_users(page_a, new_user_ids):
    page_a.update(new_user_ids)

def remove(page_b, user_ids_to_remove):
    page_b.difference_update(user_ids_to_remove)

page_a = {101, 102, 103, 104,109}
page_b = {103, 104, 105, 106,108}
page_c = {102, 107, 108}
addd = {109, 110}
removee = {103, 106}

print()
output = common_users(page_a, page_b)
print(f"Common Users of Page A and Page B: {output}")

output = non_common(page_a, page_c)
print(f"Users who visited either Page A or Page C, but not both: {output}")

update_page_a_with_new_users(page_a, addd)
print(f"Updated Page A users: {page_a}")

remove(page_b, removee)
print(f"Updated Page B users after removal: {page_b}")
print()