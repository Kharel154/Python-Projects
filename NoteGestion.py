

student_scores = input("Enter student scores separated by commas : ")
scores = [int(score) for score in student_scores.split(",")]

grades = [
    "A" if score >= 80 else
    "B" if score >= 65 else
    "C" if score >= 50 else
    "D" if score >= 40 else
    "F"
    for score in scores
]

passing_stud = [score for score in scores if score >= 50]
failing_stud = [score for score in scores if score < 50]


print("\n---- Student Grades ----")

#zip is used to combine 2 lists together to form a tuple
for i, (score,grade) in enumerate(zip(scores,grades), start=1):
    print(f"Student {i}: Score = {score}, Grade = {grade}")

print("\n --- Passing and failing Students ---")
print("Passing Students : ", passing_stud)
print("Failing Students : ", failing_stud)
