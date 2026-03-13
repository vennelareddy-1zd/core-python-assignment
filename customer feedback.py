def positive_feedback_percentage(ratings):
    if len(ratings) == 0:
        return "No ratings available"

    positive = 0

    for r in ratings:
        if r >= 4:
            positive += 1

    percentage = (positive / len(ratings)) * 100

    return percentage


ratings = [5, 4, 3, 5, 2, 4, 1, 5]

result = positive_feedback_percentage(ratings)

print("Positive Feedback:", result, "%")
