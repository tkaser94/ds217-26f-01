from itertools import count


measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# Replace this scaffold output with your calculation, loop, decision, and summary.

# Part 1
review_threshold = int(review_threshold_text)
#print(type(review_threshold))

# Part 2
total = 0
review_count = 0

# Part 3-7
for measurement in measurements:
    total += measurement
    if measurement >= review_threshold:
        measure_label = "review"
    else:
        measure_label = "within range"
    if measure_label == "within range":
        review_count += 1
    else: review_count += 0
    print("Measurement:", measurement, measure_label)

# Part 8
mean = total / len(measurements)

# Part 9
print("Count:", len(measurements))
print("Total:", total)
print("Mean:", mean)
print("Review count:", review_count)
