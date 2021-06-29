# questions list
question_prompts = [
    "1. What is the name of Tintin's Dog\n (a) Snowy\n (b) Rado \n (c) Dollar\n (d) Bolt\n\n",
    "2. What is the name of the Obelix's Dog\n (a) Snowy\n (b) Dogmatrix\n (c) Getafix\n (d) Bolt\n\n",
    "3. What is the name of the Superdog\n (a) Snowy\n (b) Dogmatrix\n (c) Kryto\n (d) Bolt\n\n"
]

# the Question class which stores the answer of the questions from the user


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# the questions list stores the questions along with the correct answers


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]

# run_test executes the process and also calculates the score


def run_test(questions):
    score = 0
    ans = []
    corr_ans = ["a", "b", "c"]
    for question in questions:
        answer = input(question.prompt)
        ans.append(answer)
        if answer == question.answer:
            score += 1
    print("You got "+str(score)+"/"+str(len(questions))+" Correct")
    print("Your answers were:", ans, " and actual answers were ", corr_ans)


run_test(questions)
