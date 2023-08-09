def create_student_report(name, age, **subjects):

    student_marks = {"name": name, "age": age, "subjects": [], "scores": []}

    for subject, scores in subjects.items():
        student_marks["subjects"].append(subject)
        student_marks["scores"].append(scores)
    return student_marks


print(create_student_report("prateek", 24, math=100, science=98, english=92))
