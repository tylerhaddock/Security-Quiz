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
# Question 6
q6 = "Q6: Which of the following BEST describes the principle of least privilege?"
q6_options = [
    "A) Users should have access to all resources they might need",
    "B) Users should only have the minimum access required to perform their job",
    "C) Admins should approve all user access requests",
    "D) Access should be revoked after 90 days"
]
q6_answer = "B"
q6_explanation = "Least privilege limits access to only what is necessary, reducing the overall attack surface of a system."

user_ans, correct, explain = ask_question(q6, q6_options, q6_answer, q6_explanation)
check_answer(user_ans, correct, explain)

# Question 7
q7 = "Q7: Which protocol provides secure, encrypted remote access to a command-line interface?"
q7_options = [
    "A) Telnet",
    "B) RDP",
    "C) SSH",
    "D) FTP"
]
q7_answer = "C"
q7_explanation = "SSH (port 22) encrypts remote sessions. Telnet sends data in plaintext and is insecure."

user_ans, correct, explain = ask_question(q7, q7_options, q7_answer, q7_explanation)
check_answer(user_ans, correct, explain)

# Question 8
q8 = "Q8: Which type of malware encrypts a victim's files and demands payment for the decryption key?"
q8_options = [
    "A) Trojan",
    "B) Worm",
    "C) Ransomware",
    "D) Rootkit"
]
q8_answer = "C"
q8_explanation = "Ransomware encrypts files and extorts victims. Trojans disguise themselves as legitimate software but do not encrypt files."

user_ans, correct, explain = ask_question(q8, q8_options, q8_answer, q8_explanation)
check_answer(user_ans, correct, explain)

# Question 9
q9 = "Q9: A company wants to ensure captured network traffic cannot be read. Which concept addresses this?"
q9_options = [
    "A) Hashing",
    "B) Digital signatures",
    "C) Encryption",
    "D) Steganography"
]
q9_answer = "C"
q9_explanation = "Encryption scrambles data so it is unreadable without the correct key, protecting data in transit."

user_ans, correct, explain = ask_question(q9, q9_options, q9_answer, q9_explanation)
check_answer(user_ans, correct, explain)

# Question 10
q10 = "Q10: An organization stores passwords using a fixed-length output that cannot be reversed. What is this?"
q10_options = [
    "A) Symmetric encryption",
    "B) Asymmetric encryption",
    "C) Hashing",
    "D) Tokenization"
]
q10_answer = "C"
q10_explanation = "Hashing is one-way and deterministic. Unlike encryption, it cannot be reversed to retrieve the original value."

user_ans, correct, explain = ask_question(q10, q10_options, q10_answer, q10_explanation)
check_answer(user_ans, correct, explain)

# Question 11
q11 = "Q11: Which of the following is used to verify a website's identity and enable HTTPS encryption?"
q11_options = [
    "A) SSH key",
    "B) Digital certificate (PKI)",
    "C) Kerberos token",
    "D) LDAP record"
]
q11_answer = "B"
q11_explanation = "PKI-based digital certificates are issued by a Certificate Authority (CA) to authenticate websites and enable TLS encryption."

user_ans, correct, explain = ask_question(q11, q11_options, q11_answer, q11_explanation)
check_answer(user_ans, correct, explain)

# Question 12
q12 = "Q12: Which type of attack positions an attacker between two communicating parties without their knowledge?"
q12_options = [
    "A) Replay attack",
    "B) Man-in-the-Middle (MitM)",
    "C) SQL Injection",
    "D) Phishing"
]
q12_answer = "B"
q12_explanation = "MitM attacks allow an attacker to intercept or alter communications between two parties secretly."

user_ans, correct, explain = ask_question(q12, q12_options, q12_answer, q12_explanation)
check_answer(user_ans, correct, explain)

# Question 13
q13 = "Q13: Which of the following BEST describes multi-factor authentication (MFA)?"
q13_options = [
    "A) Using a long complex password",
    "B) Using two or more factors from different categories",
    "C) Requiring a PIN and a second PIN",
    "D) Using biometrics only"
]
q13_answer = "B"
q13_explanation = "MFA requires factors from different categories: something you know, have, or are. Two PINs are both the same category."

user_ans, correct, explain = ask_question(q13, q13_options, q13_answer, q13_explanation)
check_answer(user_ans, correct, explain)

# Question 14
q14 = "Q14: A pen tester has zero knowledge of the target before starting. What type of test is this?"
q14_options = [
    "A) White box",
    "B) Gray box",
    "C) Black box",
    "D) Red team"
]
q14_answer = "C"
q14_explanation = "Black box = zero prior knowledge, simulating an outside attacker. White box = full knowledge. Gray box = partial."

user_ans, correct, explain = ask_question(q14, q14_options, q14_answer, q14_explanation)
check_answer(user_ans, correct, explain)

# Question 15
q15 = "Q15: A user gets an email from their bank asking them to click a link and enter credentials. What attack is this?"
q15_options = [
    "A) Vishing",
    "B) Smishing",
    "C) Phishing",
    "D) Whaling"
]
q15_answer = "C"
q15_explanation = "Phishing uses fraudulent emails to steal credentials. Vishing = voice calls, Smishing = SMS, Whaling = targets executives."

user_ans, correct, explain = ask_question(q15, q15_options, q15_answer, q15_explanation)
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
