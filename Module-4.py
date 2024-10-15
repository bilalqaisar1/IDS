def h_rating(feedback_dict):
    high_ratings = {}
    for user_id, feedback in feedback_dict.items():
        if feedback['rating'] >= 4:
            high_ratings[user_id] = feedback['rating']
    return high_ratings


def top_5(feedback_dict):
    sorted_feedback = sorted(feedback_dict.items(), key=lambda item: item[1]['rating'], reverse=True)
    return sorted_feedback[:5]


def combine(*feedback_dicts):
    combined_feedback = {}   
    for feedback_dict in feedback_dicts:
        for user_id, feedback in feedback_dict.items():
            if user_id in combined_feedback:
                combined_feedback[user_id]['rating'] = max(combined_feedback[user_id]['rating'], feedback['rating'])
                combined_feedback[user_id]['comments'] += " " + feedback['comments']
            else:
                combined_feedback[user_id] = feedback.copy()  
    return combined_feedback

def users_greater_3(feedback_dict):
    return {user_id: feedback['rating'] for user_id, feedback in feedback_dict.items() if feedback['rating'] > 3}

f1 = {
    101: {'rating': 5, 'comments': 'Great service!'},
    102: {'rating': 3, 'comments': 'Average experience.'},
    103: {'rating': 4, 'comments': 'Good, but room for improvement.'}
}

f2 = {
    104: {'rating': 5, 'comments': 'Excellent support.'},
    101: {'rating': 4, 'comments': 'Returning customer.'},
    105: {'rating': 2, 'comments': 'Not happy with the service.'}
}
f3 = {
    104: {'rating': 5, 'comments': 'Excellent support.'},
    101: {'rating': 4, 'comments': 'Returning customer.'},
    105: {'rating': 2, 'comments': 'Not happy with the service.'}
}


print()
output = h_rating(f1)
print(f"Users with rating 4 or higher: {output}")

output = top_5(f1)
print(f"Top 5 users by rating: {output}")
print()
output = (f1, f2, f3)
print(f"Combined feedback: {output}")

output = users_greater_3(f1)
print(f"Users with rating greater then 3: {output}")
print()