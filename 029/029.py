answers = set()
for a in range(2,101):
    for b in range(2,101):
        x=a**b
        answers.add(x)
print(len(answers))
