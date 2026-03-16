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
# Question 16
q16 = "Q16: Which of the following is the BEST example of something you ARE in MFA?"
q16_options = [
    "A) Password",
    "B) Smart card",
    "C) Fingerprint",
    "D) PIN"
]
q16_answer = "C"
q16_explanation = "Biometrics like fingerprints are 'something you are.' Passwords and PINs are 'something you know.' Smart cards are 'something you have.'"

user_ans, correct, explain = ask_question(q16, q16_options, q16_answer, q16_explanation)
check_answer(user_ans, correct, explain)

# Question 17
q17 = "Q17: Which of the following BEST describes a zero-day vulnerability?"
q17_options = [
    "A) A vulnerability that has been patched",
    "B) A vulnerability unknown to the vendor with no available fix",
    "C) A vulnerability discovered during a pen test",
    "D) A vulnerability that only affects older systems"
]
q17_answer = "B"
q17_explanation = "A zero-day is a vulnerability unknown to the vendor, meaning no patch exists yet, making it extremely dangerous."

user_ans, correct, explain = ask_question(q17, q17_options, q17_answer, q17_explanation)
check_answer(user_ans, correct, explain)

# Question 18
q18 = "Q18: What type of attack floods a target system with traffic to make it unavailable to users?"
q18_options = [
    "A) Phishing",
    "B) Brute force",
    "C) Denial of Service (DoS)",
    "D) Replay attack"
]
q18_answer = "C"
q18_explanation = "A DoS attack overwhelms a system with traffic, making it unavailable. A DDoS uses multiple sources to do the same thing."

user_ans, correct, explain = ask_question(q18, q18_options, q18_answer, q18_explanation)
check_answer(user_ans, correct, explain)

# Question 19
q19 = "Q19: Which of the following uses asymmetric encryption?"
q19_options = [
    "A) AES",
    "B) RSA",
    "C) DES",
    "D) 3DES"
]
q19_answer = "B"
q19_explanation = "RSA is asymmetric and uses a public/private key pair. AES, DES, and 3DES are all symmetric encryption algorithms."

user_ans, correct, explain = ask_question(q19, q19_options, q19_answer, q19_explanation)
check_answer(user_ans, correct, explain)

# Question 20
q20 = "Q20: What is the purpose of a VPN?"
q20_options = [
    "A) To block malicious websites",
    "B) To create an encrypted tunnel for secure communication over an untrusted network",
    "C) To scan for open ports on a network",
    "D) To assign IP addresses to devices"
]
q20_answer = "B"
q20_explanation = "A VPN creates an encrypted tunnel over an untrusted network like the internet, protecting data in transit."

user_ans, correct, explain = ask_question(q20, q20_options, q20_answer, q20_explanation)
check_answer(user_ans, correct, explain)

# Question 21
q21 = "Q21: Which of the following BEST describes social engineering?"
q21_options = [
    "A) Exploiting software vulnerabilities",
    "B) Manipulating people into revealing confidential information",
    "C) Scanning a network for open ports",
    "D) Injecting malicious code into a database"
]
q21_answer = "B"
q21_explanation = "Social engineering manipulates humans rather than systems. Phishing, vishing, and pretexting are all social engineering attacks."

user_ans, correct, explain = ask_question(q21, q21_options, q21_answer, q21_explanation)
check_answer(user_ans, correct, explain)

# Question 22
q22 = "Q22: An attacker captures a valid authentication token and reuses it later. What type of attack is this?"
q22_options = [
    "A) Pass the hash",
    "B) Replay attack",
    "C) Brute force",
    "D) MitM"
]
q22_answer = "B"
q22_explanation = "A replay attack captures valid credentials or tokens and reuses them later to gain unauthorized access."

user_ans, correct, explain = ask_question(q22, q22_options, q22_answer, q22_explanation)
check_answer(user_ans, correct, explain)

# Question 23
q23 = "Q23: Which of the following BEST describes the CIA triad?"
q23_options = [
    "A) Confidentiality, Integrity, Availability",
    "B) Confidentiality, Identity, Authentication",
    "C) Control, Integrity, Authorization",
    "D) Confidentiality, Intrusion, Availability"
]
q23_answer = "A"
q23_explanation = "The CIA triad stands for Confidentiality, Integrity, and Availability — the three core principles of information security."

user_ans, correct, explain = ask_question(q23, q23_options, q23_answer, q23_explanation)
check_answer(user_ans, correct, explain)

# Question 24
q24 = "Q24: Which tool is commonly used to capture and analyze network packets?"
q24_options = [
    "A) Nmap",
    "B) Metasploit",
    "C) Wireshark",
    "D) Nessus"
]
q24_answer = "C"
q24_explanation = "Wireshark is a packet analyzer used to capture and inspect network traffic. Nmap scans ports, Nessus scans vulnerabilities."

user_ans, correct, explain = ask_question(q24, q24_options, q24_answer, q24_explanation)
check_answer(user_ans, correct, explain)

# Question 25
q25 = "Q25: What does IDS stand for and what does it do?"
q25_options = [
    "A) Internet Defense System — blocks all incoming traffic",
    "B) Intrusion Detection System — monitors and alerts on suspicious activity",
    "C) Internal Data Scanner — scans files for malware",
    "D) Intrusion Denial System — prevents unauthorized logins"
]
q25_answer = "B"
q25_explanation = "An IDS monitors network traffic and alerts administrators to suspicious activity. Unlike an IPS, it detects but does not block."

user_ans, correct, explain = ask_question(q25, q25_options, q25_answer, q25_explanation)
check_answer(user_ans, correct, explain)

# Question 26
q26 = "Q26: Which of the following is a example of a strong password policy?"
q26_options = [
    "A) Minimum 6 characters, letters only",
    "B) Minimum 12 characters with uppercase, lowercase, numbers, and symbols",
    "C) Use the same password across all systems for consistency",
    "D) Change passwords every 5 years"
]
q26_answer = "B"
q26_explanation = "Strong passwords use length and complexity — uppercase, lowercase, numbers, and symbols — making them harder to brute force."

user_ans, correct, explain = ask_question(q26, q26_options, q26_answer, q26_explanation)
check_answer(user_ans, correct, explain)

# Question 27
q27 = "Q27: What is the purpose of network segmentation?"
q27_options = [
    "A) To increase internet speeds",
    "B) To limit the spread of attacks by dividing the network into isolated zones",
    "C) To assign static IP addresses to all devices",
    "D) To block all external traffic"
]
q27_answer = "B"
q27_explanation = "Network segmentation divides a network into zones so that if one segment is compromised, attackers cannot freely move laterally."

user_ans, correct, explain = ask_question(q27, q27_options, q27_answer, q27_explanation)
check_answer(user_ans, correct, explain)

# Question 28
q28 = "Q28: Which of the following BEST describes a rootkit?"
q28_options = [
    "A) Malware that replicates itself across networks",
    "B) Malware that encrypts files and demands ransom",
    "C) Malware that hides its presence and gives attackers privileged access",
    "D) Malware that displays unwanted advertisements"
]
q28_answer = "C"
q28_explanation = "A rootkit conceals itself on a system and provides attackers with persistent, privileged access while avoiding detection."

user_ans, correct, explain = ask_question(q28, q28_options, q28_answer, q28_explanation)
check_answer(user_ans, correct, explain)

# Question 29
q29 = "Q29: What is the difference between authentication and authorization?"
q29_options = [
    "A) Authentication grants access, authorization verifies identity",
    "B) Authentication verifies identity, authorization determines what access is granted",
    "C) They are the same thing",
    "D) Authorization happens before authentication"
]
q29_answer = "B"
q29_explanation = "Authentication = proving who you are. Authorization = determining what you are allowed to do after being authenticated."

user_ans, correct, explain = ask_question(q29, q29_options, q29_answer, q29_explanation)
check_answer(user_ans, correct, explain)

# Question 30
q30 = "Q30: Which of the following is an example of a physical security control?"
q30_options = [
    "A) Firewall",
    "B) Antivirus software",
    "C) Mantrap",
    "D) Encryption"
]
q30_answer = "C"
q30_explanation = "A mantrap is a physical security control using two doors to prevent tailgating. Firewalls and antivirus are technical controls."

user_ans, correct, explain = ask_question(q30, q30_options, q30_answer, q30_explanation)
check_answer(user_ans, correct, explain)

# Question 31
q31 = "Q31: Which port does HTTPS use by default?"
q31_options = [
    "A) 80",
    "B) 443",
    "C) 22",
    "D) 8080"
]
q31_answer = "B"
q31_explanation = "HTTPS uses port 443. HTTP uses port 80. SSH uses port 22. Know your common ports — they show up frequently on the exam."

user_ans, correct, explain = ask_question(q31, q31_options, q31_answer, q31_explanation)
check_answer(user_ans, correct, explain)

# Question 32
q32 = "Q32: What type of malware spreads across a network without user interaction?"
q32_options = [
    "A) Trojan",
    "B) Spyware",
    "C) Worm",
    "D) Adware"
]
q32_answer = "C"
q32_explanation = "Worms self-replicate and spread across networks without user interaction. Trojans require a user to execute them."

user_ans, correct, explain = ask_question(q32, q32_options, q32_answer, q32_explanation)
check_answer(user_ans, correct, explain)

# Question 33
q33 = "Q33: Which of the following BEST describes Defense in Depth?"
q33_options = [
    "A) Using one very strong security control",
    "B) Relying solely on a firewall to protect a network",
    "C) Layering multiple security controls so if one fails others remain",
    "D) Encrypting all data at rest"
]
q33_answer = "C"
q33_explanation = "Defense in Depth uses multiple layers of security controls so that no single point of failure can compromise the entire system."

user_ans, correct, explain = ask_question(q33, q33_options, q33_answer, q33_explanation)
check_answer(user_ans, correct, explain)

# Question 34
q34 = "Q34: What is the purpose of a DMZ in network architecture?"
q34_options = [
    "A) To store encrypted backups",
    "B) To host public-facing services while keeping the internal network protected",
    "C) To block all incoming traffic from the internet",
    "D) To assign IP addresses to internal devices"
]
q34_answer = "B"
q34_explanation = "A DMZ is a buffer zone between the internet and the internal network, hosting public services like web servers while protecting internal systems."

user_ans, correct, explain = ask_question(q34, q34_options, q34_answer, q34_explanation)
check_answer(user_ans, correct, explain)

# Question 35
q35 = "Q35: Which of the following BEST describes the role of a Certificate Authority (CA)?"
q35_options = [
    "A) Assigns IP addresses to devices on a network",
    "B) Issues and manages digital certificates to verify identities",
    "C) Monitors network traffic for intrusions",
    "D) Encrypts data stored on hard drives"
]
q35_answer = "B"
q35_explanation = "A CA is a trusted entity that issues digital certificates used to verify the identity of websites and users in a PKI system."

user_ans, correct, explain = ask_question(q35, q35_options, q35_answer, q35_explanation)
check_answer(user_ans, correct, explain)
# Question 36
q36 = "Q36: Which of the following is used to detect and prevent intrusions in real time?"
q36_options = [
    "A) IDS",
    "B) IPS",
    "C) SIEM",
    "D) Firewall"
]
q36_answer = "B"
q36_explanation = "An IPS (Intrusion Prevention System) actively blocks threats in real time. An IDS only detects and alerts but does not block."

user_ans, correct, explain = ask_question(q36, q36_options, q36_answer, q36_explanation)
check_answer(user_ans, correct, explain)

# Question 37
q37 = "Q37: What type of attack tries every possible password combination until the correct one is found?"
q37_options = [
    "A) Dictionary attack",
    "B) Rainbow table attack",
    "C) Brute force attack",
    "D) Credential stuffing"
]
q37_answer = "C"
q37_explanation = "Brute force tries every possible combination. Dictionary attacks use a wordlist. Rainbow tables use precomputed hashes."

user_ans, correct, explain = ask_question(q37, q37_options, q37_answer, q37_explanation)
check_answer(user_ans, correct, explain)

# Question 38
q38 = "Q38: Which of the following BEST describes a business continuity plan (BCP)?"
q38_options = [
    "A) A plan to recover deleted files after an attack",
    "B) A plan to keep critical business operations running during and after a disaster",
    "C) A plan to patch vulnerabilities across all systems",
    "D) A plan to train employees on security awareness"
]
q38_answer = "B"
q38_explanation = "A BCP ensures critical operations continue during disruptions. A DRP focuses on restoring systems after a disaster occurs."

user_ans, correct, explain = ask_question(q38, q38_options, q38_answer, q38_explanation)
check_answer(user_ans, correct, explain)

# Question 39
q39 = "Q39: What does SIEM stand for and what is its primary function?"
q39_options = [
    "A) Secure Information and Event Management — encrypts log files",
    "B) Security Information and Event Management — aggregates and analyzes security logs",
    "C) System Integrity and Event Monitoring — monitors hardware health",
    "D) Security Incident and Error Management — tracks software bugs"
]
q39_answer = "B"
q39_explanation = "SIEM collects and correlates security logs from across an environment to detect threats and support incident response."

user_ans, correct, explain = ask_question(q39, q39_options, q39_answer, q39_explanation)
check_answer(user_ans, correct, explain)

# Question 40
q40 = "Q40: Which of the following BEST describes tailgating?"
q40_options = [
    "A) An attacker following an authorized person into a secured area without their knowledge",
    "B) An attacker intercepting network traffic behind a firewall",
    "C) An attacker sending phishing emails to executives",
    "D) An attacker reusing captured authentication tokens"
]
q40_answer = "A"
q40_explanation = "Tailgating is a physical security attack where an attacker follows an authorized person through a secured door without credentials."

user_ans, correct, explain = ask_question(q40, q40_options, q40_answer, q40_explanation)
check_answer(user_ans, correct, explain)

# Question 41
q41 = "Q41: Which encryption algorithm is considered the current standard for symmetric encryption?"
q41_options = [
    "A) DES",
    "B) RSA",
    "C) AES",
    "D) MD5"
]
q41_answer = "C"
q41_explanation = "AES (Advanced Encryption Standard) is the current symmetric encryption standard. DES is outdated. RSA is asymmetric. MD5 is a hash function."

user_ans, correct, explain = ask_question(q41, q41_options, q41_answer, q41_explanation)
check_answer(user_ans, correct, explain)

# Question 42
q42 = "Q42: What is the purpose of salting a password before hashing it?"
q42_options = [
    "A) To encrypt the password twice for extra security",
    "B) To add a random value to the password to prevent rainbow table attacks",
    "C) To convert the password into asymmetric format",
    "D) To store the password in plaintext temporarily"
]
q42_answer = "B"
q42_explanation = "A salt is a random value added to a password before hashing, ensuring identical passwords produce different hashes and defeating rainbow tables."

user_ans, correct, explain = ask_question(q42, q42_options, q42_answer, q42_explanation)
check_answer(user_ans, correct, explain)

# Question 43
q43 = "Q43: Which of the following BEST describes a supply chain attack?"
q43_options = [
    "A) An attack targeting a company's shipping and logistics systems",
    "B) An attack that compromises a trusted vendor or software update to reach the target",
    "C) An attack that floods a network with traffic",
    "D) An attack using stolen credentials to access cloud storage"
]
q43_answer = "B"
q43_explanation = "A supply chain attack compromises a trusted third party like a software vendor to gain access to the ultimate target organization."

user_ans, correct, explain = ask_question(q43, q43_options, q43_answer, q43_explanation)
check_answer(user_ans, correct, explain)

# Question 44
q44 = "Q44: What port does DNS use by default?"
q44_options = [
    "A) 25",
    "B) 53",
    "C) 110",
    "D) 443"
]
q44_answer = "B"
q44_explanation = "DNS uses port 53. Port 25 is SMTP, port 110 is POP3, port 443 is HTTPS. Common ports are heavily tested on Security+."

user_ans, correct, explain = ask_question(q44, q44_options, q44_answer, q44_explanation)
check_answer(user_ans, correct, explain)

# Question 45
q45 = "Q45: Which of the following BEST describes a honeypo?"
q45_options = [
    "A) A firewall rule that traps malicious traffic",
    "B) A decoy system designed to attract and monitor attackers",
    "C) A backup server used during disaster recovery",
    "D) A tool used to crack password hashes"
]
q45_answer = "B"
q45_explanation = "A honeypot is a decoy system that lures attackers, allowing defenders to monitor their tactics without risking real systems."

user_ans, correct, explain = ask_question(q45, q45_options, q45_answer, q45_explanation)
check_answer(user_ans, correct, explain)

# Question 46
q46 = "Q46: What is the MAIN difference between a vulnerability scan and a penetration test?"
q46_options = [
    "A) A vulnerability scan is illegal, a penetration test is not",
    "B) A vulnerability scan identifies weaknesses, a penetration test actively exploits them",
    "C) A penetration test is automated, a vulnerability scan is manual",
    "D) They are the same thing"
]
q46_answer = "B"
q46_explanation = "Vulnerability scans identify and report weaknesses. Penetration tests go further by actively exploiting those weaknesses to assess real impact."

user_ans, correct, explain = ask_question(q46, q46_options, q46_answer, q46_explanation)
check_answer(user_ans, correct, explain)

# Question 47
q47 = "Q47: Which of the following BEST describes role-based access control (RBAC)?"
q47_options = [
    "A) Access is granted based on a user's physical location",
    "B) Access is granted based on the user's assigned role within the organization",
    "C) Access is granted based on time of day",
    "D) Access is granted based on the device being used"
]
q47_answer = "B"
q47_explanation = "RBAC assigns permissions based on job roles rather than individual users, making access management easier and more consistent."

user_ans, correct, explain = ask_question(q47, q47_options, q47_answer, q47_explanation)
check_answer(user_ans, correct, explain)

# Question 48
q48 = "Q48: Which of the following is a common use of steganography?"
q48_options = [
    "A) Encrypting hard drive contents",
    "B) Hiding secret data inside an image or audio file",
    "C) Scanning networks for open ports",
    "D) Cracking password hashes"
]
q48_answer = "B"
q48_explanation = "Steganography hides data inside innocent-looking files like images or audio. It is used for covert communication and data exfiltration."

user_ans, correct, explain = ask_question(q48, q48_options, q48_answer, q48_explanation)
check_answer(user_ans, correct, explain)

# Question 49
q49 = "Q49: What does the term non-repudiation mean in cybersecurity?"
q49_options = [
    "A) Ensuring data is encrypted at rest",
    "B) Ensuring a user cannot deny performing an action they took",
    "C) Ensuring systems remain available during an attack",
    "D) Ensuring passwords are never stored in plaintext"
]
q49_answer = "B"
q49_explanation = "Non-repudiation ensures that a user cannot deny an action they performed, typically enforced through digital signatures and audit logs."

user_ans, correct, explain = ask_question(q49, q49_options, q49_answer, q49_explanation)
check_answer(user_ans, correct, explain)

# Question 50
q50 = "Q50: Which of the following BEST describes a watering hole attack?"
q50_options = [
    "A) Flooding a network with traffic to cause an outage",
    "B) Compromising a website frequently visited by the target group",
    "C) Sending phishing emails to a large group of users",
    "D) Physically stealing hardware from a target organization"
]
q50_answer = "B"
q50_explanation = "A watering hole attack compromises a website the target group regularly visits, infecting visitors with malware when they land on the page."

user_ans, correct, explain = ask_question(q50, q50_options, q50_answer, q50_explanation)
check_answer(user_ans, correct, explain)

# Question 51
q51 = "Q51: Which protocol is used to securely transfer files and runs over SSH?"
q51_options = [
    "A) FTP",
    "B) FTPS",
    "C) SFTP",
    "D) TFTP"
]
q51_answer = "C"
q51_explanation = "SFTP (SSH File Transfer Protocol) runs over SSH and is fully encrypted. FTP is plaintext. FTPS adds TLS to FTP. TFTP is lightweight with no authentication."

user_ans, correct, explain = ask_question(q51, q51_options, q51_answer, q51_explanation)
check_answer(user_ans, correct, explain)

# Question 52
q52 = "Q52: An attacker sends an email pretending to be the CEO asking an employee to wire money. What attack is this?"
q52_options = [
    "A) Phishing",
    "B) Whaling",
    "C) Smishing",
    "D) Vishing"
]
q52_answer = "B"
q52_explanation = "Whaling is a targeted phishing attack aimed specifically at high-profile individuals like executives. BEC (Business Email Compromise) is a common whaling tactic."

user_ans, correct, explain = ask_question(q52, q52_options, q52_answer, q52_explanation)
check_answer(user_ans, correct, explain)

# Question 53
q53 = "Q53: Which of the following BEST describes data loss prevention (DLP)?"
q53_options = [
    "A) A tool that encrypts all data stored on a hard drive",
    "B) A system that detects and prevents unauthorized transfer of sensitive data",
    "C) A backup solution that restores lost files after an attack",
    "D) A firewall rule that blocks all outbound traffic"
]
q53_answer = "B"
q53_explanation = "DLP monitors and controls data transfers to prevent sensitive information from leaving the organization without authorization."

user_ans, correct, explain = ask_question(q53, q53_options, q53_answer, q53_explanation)
check_answer(user_ans, correct, explain)

# Question 54
q54 = "Q54: What is the purpose of an access control list (ACL)?"
q54_options = [
    "A) To log all failed login attempts",
    "B) To define which users or systems are permitted or denied access to a resource",
    "C) To encrypt data traveling across a network",
    "D) To assign IP addresses to network devices"
]
q54_answer = "B"
q54_explanation = "An ACL is a set of rules that defines which users or systems are allowed or denied access to specific network resources or files."

user_ans, correct, explain = ask_question(q54, q54_options, q54_answer, q54_explanation)
check_answer(user_ans, correct, explain)

# Question 55
q55 = "Q55: Which of the following BEST describes a botnet?"
q55_options = [
    "A) A network of security cameras monitored by an attacker",
    "B) A collection of compromised devices controlled remotely by an attacker",
    "C) A group of firewalls working together to block attacks",
    "D) A set of honeypots deployed to attract attackers"
]
q55_answer = "B"
q55_explanation = "A botnet is a network of infected devices (bots) controlled by an attacker (botmaster), often used to launch DDoS attacks or send spam."

user_ans, correct, explain = ask_question(q55, q55_options, q55_answer, q55_explanation)
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
