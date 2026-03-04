# Tyler's Security+ Quiz App
# Built by Tyler Haddock - for GitHub portfolio

score = 0
total_questions = 0
print("=============================")
print("   TYLER'S SECURITY+ APP    ")
print("=============================")
print("Let's see what you know!\n")

def ask_question(question, options, correct_answer, explanation):
    print("\n" + question)
    for option in options:
        print(option)

    answer = input("\nYour answer (A/B/C/D): ").upper()
    return answer, correct_answer, explanation

def check_answer(user_answer, correct_answer, explanation):
    global score, total_questions
    total_questions += 1

    if user_answer == correct_answer:
        print("\nCORRECT!")
        score += 1
    else:
        print(f"\nWRONG! The correct answer was {correct_answer}")

    print(f"Explanation:{explanation}")

# Question 1
q1 = "Q1: What does CIA stand for in cybersecurity?"
q1_options = [
    "A) Central Intelligence Agency",
    "B) Confidentiality, Integrity, Availability",
    "C) Cyber Intelligence Architecture",
    "D) Control, Identify, Authenticate"
]
q1_answer = "B"
q1_explanation = "The CIA Triad is the foundation of cybersecurity. Confidentiality means keeping data private, Integrity means data has NOT been  tampered with, Availability means systems are accessible when needed"

user_ans, correct, explain = ask_question(q1, q1_options, q1_answer, q1_explanation)
check_answer(user_ans, correct, explain)
# Question 2
q2 = "Q2: Which type of attack tricks users into revealing sensitive information?"
q2_options = [
    "A) DDos Attack",
    "B) SQL Injection",
    "C) Phishing",
    "D) Man in the Middle"
]
q2_answer = "C"
q2_explanation = "Phishing is a social engineering attack where attackers impersonate trusted entities to steal credentials or personal information. It is one of the most common attack vectors."

user_ans, correct, explain = ask_question(q2, q2_options, q2_answer, q2_explanation)
check_answer(user_ans, correct, explain)
# Question 3
q3 = "Q3: What is the purpose of a firewall?"
q3_options = [
    "A) Speed up network traffic",
    "B) Monitor and filter incoming and outgoing network traffic",
    "C) Encrypt data on a hard drive",
    "D) Backup data automatically"
]
q3_answer = "B"
q3_explanation = "A fire wall monitors and controls netowrk traffic based on predetermined security rules. It creates a barrier between trusted internal networks and untrustred external networks."

user_ans, correct, explain = ask_question(q3, q3_options, q3_answer, q3_explanation)
check_answer(user_ans, correct, explain)
# Question 4
q4 = "Q4: What does MFA stand for?"
q4_options = [
    "A) Multiple Firewall Authentication",
    "B) Managed Firewall Access",
    "C) Multi Factor Authentication",
    "D) Malware Filtering Architecture"
]
q4_answer = "C"
q4_explanation = "Multi Factor Authentication requires users to provide two or more verification factors to gain access. This makes accounts significantly harder to compromise even if passwords are stolen."

user_ans, correct, explain = ask_question(q4, q4_options, q4_answer, q4_explanation)
check_answer(user_ans, correct, explain)
# Question 5
q5 = "Q5: Which of the following is an example of something you HAVE in MFA?"
q5_options = [
    "A) Password",
    "B) Fingerprint",
    "C) Phone with authenticator app",
    "D) Security question answer"
]
q5_answer = "C"
q5_explanation = "MFA factors are catagorized as something you KNOW (password), something you HAVE (phone/token), or something you are (biometrics). A phone with an authenticator app is something you physically have."

user_ans, correct, explain = ask_question(q5, q5_options, q5_answer, q5_explanation)
check_answer(user_ans, correct, explain)

print("\n================================")
print("n\        QUIZ COMPLETE!      ")
print("==============================")
print(f"Your Score: {score} out of {total_questions}")

percentage = (score / total_questions) * 100

if percentage == 100:
    print("PERFECT SCORE! You're ready!")
elif percentage >=  80:
    print("Great Job! Almost there!")
elif percentage >= 60:
    print("Not bad, keep studying!")
else:
    print("I mean really? That bad huh. Keep grinding, you'll get there eventually kid.")

print(f"\nPercentage: {percentage: .1f}%")
print("====================================================")
