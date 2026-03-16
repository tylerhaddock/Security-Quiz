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
# Question 56
q56 = "Q56: Which of the following BEST describes threat intelligence?"
q56_options = [
    "A) A tool that automatically patches vulnerabilities",
    "B) Information about current and emerging threats used to make security decisions",
    "C) A log of all failed login attempts on a system",
    "D) A list of approved software applications"
]
q56_answer = "B"
q56_explanation = "Threat intelligence is actionable information about threats and threat actors that helps organizations proactively defend their systems."

user_ans, correct, explain = ask_question(q56, q56_options, q56_answer, q56_explanation)
check_answer(user_ans, correct, explain)

# Question 57
q57 = "Q57: What is the purpose of patch management?"
q57_options = [
    "A) To monitor network traffic for suspicious activity",
    "B) To ensure systems are kept up to date with security fixes",
    "C) To back up critical data on a scheduled basis",
    "D) To assign user roles and permissions"
]
q57_answer = "B"
q57_explanation = "Patch management ensures systems receive security updates promptly, closing vulnerabilities before attackers can exploit them."

user_ans, correct, explain = ask_question(q57, q57_options, q57_answer, q57_explanation)
check_answer(user_ans, correct, explain)

# Question 58
q58 = "Q58: Which of the following BEST describes a logic bomb?"
q58_options = [
    "A) Malware that spreads automatically across a network",
    "B) Malicious code that executes when a specific condition or trigger is met",
    "C) A phishing email targeting executives",
    "D) A tool used to crack encryption keys"
]
q58_answer = "B"
q58_explanation = "A logic bomb is malicious code that remains dormant until a specific trigger occurs, such as a date, time, or user action."

user_ans, correct, explain = ask_question(q58, q58_options, q58_answer, q58_explanation)
check_answer(user_ans, correct, explain)

# Question 59
q59 = "Q59: Which of the following port and protocol pairs is CORRECT?"
q59_options = [
    "A) SSH — Port 23",
    "B) SMTP — Port 25",
    "C) HTTP — Port 443",
    "D) RDP — Port 22"
]
q59_answer = "B"
q59_explanation = "SMTP uses port 25. SSH is port 22, HTTP is port 80, HTTPS is port 443, and RDP is port 3389. Know these cold for the exam."

user_ans, correct, explain = ask_question(q59, q59_options, q59_answer, q59_explanation)
check_answer(user_ans, correct, explain)

# Question 60
q60 = "Q60: What is the purpose of full disk encryption (FDE)?"
q60_options = [
    "A) To speed up disk read and write performance",
    "B) To protect data on a device if it is lost or stolen",
    "C) To compress files to save storage space",
    "D) To back up data to a remote server"
]
q60_answer = "B"
q60_explanation = "Full disk encryption protects all data on a device by encrypting the entire drive, making data unreadable without the correct credentials."

user_ans, correct, explain = ask_question(q60, q60_options, q60_answer, q60_explanation)
check_answer(user_ans, correct, explain)

# Question 61
q61 = "Q61: Which of the following BEST describes a man-in-the-browser attack?"
q61_options = [
    "A) An attacker physically sits between two computers",
    "B) Malware that intercepts and modifies transactions inside a web browser",
    "C) An attacker clones a website to steal credentials",
    "D) An attacker floods a browser with pop-up ads"
]
q61_answer = "B"
q61_explanation = "A man-in-the-browser attack uses malware to intercept and manipulate web transactions in real time inside the victim's browser."

user_ans, correct, explain = ask_question(q61, q61_options, q61_answer, q61_explanation)
check_answer(user_ans, correct, explain)

# Question 62
q62 = "Q62: Which of the following is the BEST way to protect data at rest?"
q62_options = [
    "A) VPN",
    "B) TLS",
    "C) Encryption",
    "D) Firewall"
]
q62_answer = "C"
q62_explanation = "Encryption protects data at rest by making it unreadable without the correct key. VPN and TLS protect data in transit, not at rest."

user_ans, correct, explain = ask_question(q62, q62_options, q62_answer, q62_explanation)
check_answer(user_ans, correct, explain)

# Question 63
q63 = "Q63: What is the purpose of a disaster recovery plan (DRP)?"
q63_options = [
    "A) To train employees on phishing awareness",
    "B) To restore IT systems and operations after a disaster or outage",
    "C) To prevent attackers from accessing the network",
    "D) To assign roles and responsibilities during a security audit"
]
q63_answer = "B"
q63_explanation = "A DRP focuses on restoring IT systems after a disaster. A BCP is broader and covers keeping all business operations running."

user_ans, correct, explain = ask_question(q63, q63_options, q63_answer, q63_explanation)
check_answer(user_ans, correct, explain)

# Question 64
q64 = "Q64: Which of the following BEST describes a cross-site scripting (XSS) attack?"
q64_options = [
    "A) Injecting malicious SQL into a database query",
    "B) Injecting malicious scripts into a trusted website viewed by other users",
    "C) Intercepting traffic between a browser and a web server",
    "D) Flooding a web server with requests to cause an outage"
]
q64_answer = "B"
q64_explanation = "XSS injects malicious scripts into a trusted website, which then execute in the browsers of other users who visit the page."

user_ans, correct, explain = ask_question(q64, q64_options, q64_answer, q64_explanation)
check_answer(user_ans, correct, explain)

# Question 65
q65 = "Q65: Which of the following BEST describes SQL injection?"
q65_options = [
    "A) Injecting malware into a database server through a USB drive",
    "B) Inserting malicious SQL code into an input field to manipulate a database",
    "C) Encrypting a database and demanding ransom",
    "D) Intercepting database traffic across a network"
]
q65_answer = "B"
q65_explanation = "SQL injection inserts malicious SQL code into an input field to manipulate or extract data from a backend database."

user_ans, correct, explain = ask_question(q65, q65_options, q65_answer, q65_explanation)
check_answer(user_ans, correct, explain)

# Question 66
q66 = "Q66: What does the term 'threat actor' refer to?"
q66_options = [
    "A) A security professional performing a penetration test",
    "B) Any individual or group that poses a threat to an organization's security",
    "C) Software used to detect and block malware",
    "D) A vulnerability found during a security audit"
]
q66_answer = "B"
q66_explanation = "A threat actor is any individual or group that intentionally causes harm to systems. Examples include nation-states, hacktivists, and insider threats."

user_ans, correct, explain = ask_question(q66, q66_options, q66_answer, q66_explanation)
check_answer(user_ans, correct, explain)

# Question 67
q67 = "Q67: Which of the following BEST describes separation of duties?"
q67_options = [
    "A) Requiring employees to take mandatory vacation",
    "B) Dividing critical tasks among multiple people to prevent fraud or error",
    "C) Assigning all admin tasks to a single trusted employee",
    "D) Separating wired and wireless network traffic"
]
q67_answer = "B"
q67_explanation = "Separation of duties splits critical tasks across multiple people so no single person has enough access to commit fraud or make a critical error alone."

user_ans, correct, explain = ask_question(q67, q67_options, q67_answer, q67_explanation)
check_answer(user_ans, correct, explain)

# Question 68
q68 = "Q68: Which of the following BEST describes a rainbow table attack?"
q68_options = [
    "A) Trying every possible password combination one by one",
    "B) Using precomputed hash values to crack passwords",
    "C) Intercepting hashed passwords over a network",
    "D) Injecting malicious code into a login form"
]
q68_answer = "B"
q68_explanation = "Rainbow table attacks use precomputed hash values to reverse engineer passwords. Salting passwords defeats this attack."

user_ans, correct, explain = ask_question(q68, q68_options, q68_answer, q68_explanation)
check_answer(user_ans, correct, explain)

# Question 69
q69 = "Q69: Which of the following is an example of a technical security control?"
q69_options = [
    "A) Security awareness training",
    "B) A locked server room door",
    "C) An intrusion prevention system",
    "D) A written acceptable use policy"
]
q69_answer = "C"
q69_explanation = "Technical controls use technology to protect systems, like firewalls and IPS. Physical controls are locks and cameras. Administrative controls are policies."

user_ans, correct, explain = ask_question(q69, q69_options, q69_answer, q69_explanation)
check_answer(user_ans, correct, explain)

# Question 70
q70 = "Q70: What is the purpose of a security baseline?"
q70_options = [
    "A) To document all known vulnerabilities in a system",
    "B) To establish a minimum security standard that all systems must meet",
    "C) To monitor network traffic for anomalies",
    "D) To assign user permissions based on job role"
]
q70_answer = "B"
q70_explanation = "A security baseline defines the minimum security configuration required for systems in an organization, ensuring consistent protection."

user_ans, correct, explain = ask_question(q70, q70_options, q70_answer, q70_explanation)
check_answer(user_ans, correct, explain)

# Question 71
q71 = "Q71: Which of the following BEST describes pretexting?"
q71_options = [
    "A) Sending malicious attachments via email",
    "B) Creating a fabricated scenario to manipulate someone into revealing information",
    "C) Intercepting network traffic to steal credentials",
    "D) Flooding a system with login attempts"
]
q71_answer = "B"
q71_explanation = "Pretexting is a social engineering technique where an attacker invents a believable scenario to trick a victim into revealing sensitive information."

user_ans, correct, explain = ask_question(q71, q71_options, q71_answer, q71_explanation)
check_answer(user_ans, correct, explain)

# Question 72
q72 = "Q72: Which of the following BEST describes a fileless malware attack?"
q72_options = [
    "A) Malware stored on a USB drive",
    "B) Malware that runs entirely in memory without writing files to disk",
    "C) Malware that deletes all files on a hard drive",
    "D) Malware hidden inside an image file"
]
q72_answer = "B"
q72_explanation = "Fileless malware runs in memory and leaves no files on disk, making it much harder for traditional antivirus tools to detect."

user_ans, correct, explain = ask_question(q72, q72_options, q72_answer, q72_explanation)
check_answer(user_ans, correct, explain)

# Question 73
q73 = "Q73: What does RDP stand for and what port does it use?"
q73_options = [
    "A) Remote Desktop Protocol — Port 22",
    "B) Remote Desktop Protocol — Port 3389",
    "C) Remote Data Protocol — Port 443",
    "D) Remote Desktop Protocol — Port 80"
]
q73_answer = "B"
q73_explanation = "RDP (Remote Desktop Protocol) uses port 3389 and allows users to remotely control another computer's desktop. It is a frequent attack target."

user_ans, correct, explain = ask_question(q73, q73_options, q73_answer, q73_explanation)
check_answer(user_ans, correct, explain)

# Question 74
q74 = "Q74: Which of the following BEST describes the concept of data sovereignty?"
q74_options = [
    "A) Encrypting all data before it leaves the network",
    "B) The idea that data is subject to the laws of the country where it is stored",
    "C) Ensuring only authorized users can access sensitive data",
    "D) Backing up data to multiple geographic locations"
]
q74_answer = "B"
q74_explanation = "Data sovereignty means data is governed by the laws of the country where it physically resides, which is critical for cloud storage compliance."

user_ans, correct, explain = ask_question(q74, q74_options, q74_answer, q74_explanation)
check_answer(user_ans, correct, explain)

# Question 75
q75 = "Q75: Which of the following BEST describes an insider threat?"
q75_options = [
    "A) A hacker from another country attacking a network remotely",
    "B) A current or former employee who misuses their access to harm the organization",
    "C) Malware installed on a system through a phishing email",
    "D) An attacker who physically breaks into a server room"
]
q75_answer = "B"
q75_explanation = "Insider threats come from people with legitimate access such as employees or contractors, making them especially dangerous and difficult to detect."

user_ans, correct, explain = ask_question(q75, q75_options, q75_answer, q75_explanation)
check_answer(user_ans, correct, explain)
# Question 76
q76 = "Q76: Which of the following BEST describes a cold site in disaster recovery?"
q76_options = [
    "A) A fully operational backup site ready to take over immediately",
    "B) A site with some equipment but no live data or active systems",
    "C) An empty facility with no equipment that requires full setup after a disaster",
    "D) A cloud-based backup solution"
]
q76_answer = "C"
q76_explanation = "A cold site is an empty facility that requires full setup after a disaster. A warm site has some equipment. A hot site is fully operational and ready immediately."

user_ans, correct, explain = ask_question(q76, q76_options, q76_answer, q76_explanation)
check_answer(user_ans, correct, explain)

# Question 77
q77 = "Q77: Which of the following BEST describes a hot site in disaster recovery?"
q77_options = [
    "A) A site that requires 24-48 hours to become operational",
    "B) A fully operational backup site that can take over immediately after a disaster",
    "C) A site with basic infrastructure but no data",
    "D) A mobile disaster recovery unit"
]
q77_answer = "B"
q77_explanation = "A hot site mirrors the production environment and can take over immediately. It is the most expensive DR option but has the lowest recovery time."

user_ans, correct, explain = ask_question(q77, q77_options, q77_answer, q77_explanation)
check_answer(user_ans, correct, explain)

# Question 78
q78 = "Q78: What does the term 'attack surface' refer to?"
q78_options = [
    "A) The physical area around a server room that must be secured",
    "B) The total number of vulnerabilities found in a system",
    "C) All the points where an attacker could try to enter or extract data from a system",
    "D) The number of users with admin privileges"
]
q78_answer = "C"
q78_explanation = "The attack surface is every possible entry point an attacker could exploit. Reducing attack surface is a core security principle."

user_ans, correct, explain = ask_question(q78, q78_options, q78_answer, q78_explanation)
check_answer(user_ans, correct, explain)

# Question 79
q79 = "Q79: Which of the following BEST describes a dictionary attack?"
q79_options = [
    "A) Trying every possible character combination to crack a password",
    "B) Using a list of common words and passwords to crack credentials",
    "C) Using precomputed hashes to reverse engineer passwords",
    "D) Intercepting credentials as they travel across a network"
]
q79_answer = "B"
q79_explanation = "A dictionary attack uses a wordlist of common passwords. Brute force tries all combinations. Rainbow tables use precomputed hashes."

user_ans, correct, explain = ask_question(q79, q79_options, q79_answer, q79_explanation)
check_answer(user_ans, correct, explain)

# Question 80
q80 = "Q80: Which of the following is the BEST defense against phishing attacks?"
q80_options = [
    "A) Installing a firewall",
    "B) Security awareness training for employees",
    "C) Enabling full disk encryption",
    "D) Disabling unused network ports"
]
q80_answer = "B"
q80_explanation = "Since phishing targets humans, security awareness training is the most effective defense. Technical controls help but cannot replace educated users."

user_ans, correct, explain = ask_question(q80, q80_options, q80_answer, q80_explanation)
check_answer(user_ans, correct, explain)

# Question 81
q81 = "Q81: What is the purpose of a public key in asymmetric encryption?"
q81_options = [
    "A) To decrypt messages sent by others",
    "B) To encrypt messages so only the holder of the private key can decrypt them",
    "C) To sign documents on behalf of an organization",
    "D) To generate a shared symmetric key"
]
q81_answer = "B"
q81_explanation = "In asymmetric encryption the public key encrypts data and the private key decrypts it. The public key is freely shared while the private key is kept secret."

user_ans, correct, explain = ask_question(q81, q81_options, q81_answer, q81_explanation)
check_answer(user_ans, correct, explain)

# Question 82
q82 = "Q82: Which of the following BEST describes a CSRF attack?"
q82_options = [
    "A) Injecting malicious scripts into a trusted website",
    "B) Tricking an authenticated user into unknowingly submitting a malicious request",
    "C) Intercepting traffic between a browser and web server",
    "D) Flooding a web server with requests to cause an outage"
]
q82_answer = "B"
q82_explanation = "Cross-Site Request Forgery tricks an authenticated user's browser into sending unauthorized requests, exploiting the trust a site has in the user."

user_ans, correct, explain = ask_question(q82, q82_options, q82_answer, q82_explanation)
check_answer(user_ans, correct, explain)

# Question 83
q83 = "Q83: What is the MAIN purpose of security awareness training?"
q83_options = [
    "A) To teach employees how to perform penetration tests",
    "B) To reduce human error and make employees the first line of defense",
    "C) To replace technical security controls",
    "D) To train employees on how to use encryption tools"
]
q83_answer = "B"
q83_explanation = "Security awareness training reduces human error by educating employees on threats like phishing, social engineering, and safe computing practices."

user_ans, correct, explain = ask_question(q83, q83_options, q83_answer, q83_explanation)
check_answer(user_ans, correct, explain)

# Question 84
q84 = "Q84: Which of the following BEST describes the concept of zero trust?"
q84_options = [
    "A) Trusting all users inside the corporate network by default",
    "B) Never trusting any user or device by default and always verifying before granting access",
    "C) Blocking all external traffic at the firewall",
    "D) Requiring all employees to use VPNs"
]
q84_answer = "B"
q84_explanation = "Zero trust assumes no user or device should be trusted by default, even inside the network. Every access request must be verified continuously."

user_ans, correct, explain = ask_question(q84, q84_options, q84_answer, q84_explanation)
check_answer(user_ans, correct, explain)

# Question 85
q85 = "Q85: Which hashing algorithm is considered the MOST secure from the options below?"
q85_options = [
    "A) MD5",
    "B) SHA-1",
    "C) SHA-256",
    "D) DES"
]
q85_answer = "C"
q85_explanation = "SHA-256 is currently considered secure. MD5 and SHA-1 are outdated and vulnerable to collision attacks. DES is a symmetric encryption algorithm, not a hash."

user_ans, correct, explain = ask_question(q85, q85_options, q85_answer, q85_explanation)
check_answer(user_ans, correct, explain)

# Question 86
q86 = "Q86: What is the purpose of log management in cybersecurity?"
q86_options = [
    "A) To encrypt all system activity",
    "B) To collect, store, and analyze logs to detect and investigate security events",
    "C) To back up user data on a scheduled basis",
    "D) To assign permissions based on user activity"
]
q86_answer = "B"
q86_explanation = "Log management collects and analyzes logs from systems and devices to detect threats, support investigations, and meet compliance requirements."

user_ans, correct, explain = ask_question(q86, q86_options, q86_answer, q86_explanation)
check_answer(user_ans, correct, explain)

# Question 87
q87 = "Q87: Which of the following BEST describes a spear phishing attack?"
q87_options = [
    "A) A phishing attack sent to thousands of random users",
    "B) A highly targeted phishing attack aimed at a specific individual or organization",
    "C) A phishing attack delivered via SMS",
    "D) A phishing attack that uses voice calls"
]
q87_answer = "B"
q87_explanation = "Spear phishing is targeted at a specific person or organization using personalized information to appear more convincing than generic phishing."

user_ans, correct, explain = ask_question(q87, q87_options, q87_answer, q87_explanation)
check_answer(user_ans, correct, explain)

# Question 88
q88 = "Q88: Which of the following BEST describes the principle of need to know?"
q88_options = [
    "A) Users should know all company security policies",
    "B) Users should only have access to information required to perform their specific job",
    "C) All employees should know who the security team is",
    "D) Managers should know all employee passwords"
]
q88_answer = "B"
q88_explanation = "Need to know restricts access to information based on job necessity. It works alongside least privilege to minimize data exposure."

user_ans, correct, explain = ask_question(q88, q88_options, q88_answer, q88_explanation)
check_answer(user_ans, correct, explain)

# Question 89
q89 = "Q89: What does TPM stand for and what is its purpose?"
q89_options = [
    "A) Trusted Platform Module — a chip that stores encryption keys and protects hardware integrity",
    "B) Threat Protection Manager — software that blocks malware",
    "C) Total Patch Management — a system for deploying security updates",
    "D) Trusted Password Manager — a tool for storing user credentials"
]
q89_answer = "A"
q89_explanation = "A TPM is a hardware chip that stores cryptographic keys and ensures platform integrity. It is commonly used with full disk encryption like BitLocker."

user_ans, correct, explain = ask_question(q89, q89_options, q89_answer, q89_explanation)
check_answer(user_ans, correct, explain)

# Question 90
q90 = "Q90: Which of the following BEST describes an advanced persistent threat (APT)?"
q90_options = [
    "A) A fast moving virus that spreads across a network in minutes",
    "B) A long term targeted attack where an intruder gains and maintains stealthy access",
    "C) A ransomware attack that encrypts files immediately",
    "D) A phishing campaign targeting thousands of users at once"
]
q90_answer = "B"
q90_explanation = "An APT is a prolonged stealthy attack, often state-sponsored, where the attacker maintains persistent access to gather intelligence over a long period."

user_ans, correct, explain = ask_question(q90, q90_options, q90_answer, q90_explanation)
check_answer(user_ans, correct, explain)

# Question 91
q91 = "Q91: Which of the following BEST describes tokenization?"
q91_options = [
    "A) Converting plaintext into ciphertext using an encryption key",
    "B) Replacing sensitive data with a non-sensitive placeholder value",
    "C) Hashing a password before storing it in a database",
    "D) Splitting data across multiple storage locations"
]
q91_answer = "B"
q91_explanation = "Tokenization replaces sensitive data like credit card numbers with a token. Unlike encryption, the original data is not mathematically derivable from the token."

user_ans, correct, explain = ask_question(q91, q91_options, q91_answer, q91_explanation)
check_answer(user_ans, correct, explain)

# Question 92
q92 = "Q92: Which of the following BEST describes a sandbox environment?"
q92_options = [
    "A) A secured network segment for storing sensitive data",
    "B) An isolated environment used to safely execute and analyze suspicious code",
    "C) A backup server used during disaster recovery",
    "D) A firewall rule that isolates infected devices"
]
q92_answer = "B"
q92_explanation = "A sandbox is an isolated environment where suspicious code can be executed and analyzed safely without risking production systems."

user_ans, correct, explain = ask_question(q92, q92_options, q92_answer, q92_explanation)
check_answer(user_ans, correct, explain)

# Question 93
q93 = "Q93: What is the purpose of a vulnerability assessment?"
q93_options = [
    "A) To actively exploit weaknesses to determine their real impact",
    "B) To identify and prioritize vulnerabilities in systems without exploiting them",
    "C) To train employees on how to respond to security incidents",
    "D) To monitor network traffic for unusual patterns"
]
q93_answer = "B"
q93_explanation = "A vulnerability assessment identifies and prioritizes weaknesses without exploiting them. A penetration test goes further and actively exploits vulnerabilities."

user_ans, correct, explain = ask_question(q93, q93_options, q93_answer, q93_explanation)
check_answer(user_ans, correct, explain)

# Question 94
q94 = "Q94: Which of the following BEST describes mandatory access control (MAC)?"
q94_options = [
    "A) Users can set their own permissions on files they own",
    "B) Access is assigned based on job role",
    "C) Access is determined by the system based on security labels and clearance levels",
    "D) Access is granted based on the time of day"
]
q94_answer = "C"
q94_explanation = "MAC uses security labels and clearance levels enforced by the system, not users. It is commonly used in government and military environments."

user_ans, correct, explain = ask_question(q94, q94_options, q94_answer, q94_explanation)
check_answer(user_ans, correct, explain)

# Question 95
q95 = "Q95: Which of the following is the BEST example of a preventive security control?"
q95_options = [
    "A) Security camera",
    "B) Audit log",
    "C) Firewall",
    "D) Incident response plan"
]
q95_answer = "C"
q95_explanation = "A firewall is a preventive control that stops threats before they occur. Cameras and logs are detective controls. An IR plan is a corrective control."

user_ans, correct, explain = ask_question(q95, q95_options, q95_answer, q95_explanation)
check_answer(user_ans, correct, explain)

# Question 96
q96 = "Q96: What is the purpose of a chain of custody in digital forensics?"
q96_options = [
    "A) To encrypt evidence before it is submitted to court",
    "B) To document the handling of evidence to ensure its integrity and admissibility",
    "C) To assign investigators to a security incident",
    "D) To back up forensic images to a secure server"
]
q96_answer = "B"
q96_explanation = "Chain of custody documents who handled evidence, when, and how, ensuring its integrity is maintained and it remains admissible in legal proceedings."

user_ans, correct, explain = ask_question(q96, q96_options, q96_answer, q96_explanation)
check_answer(user_ans, correct, explain)

# Question 97
q97 = "Q97: Which of the following BEST describes input validation?"
q97_options = [
    "A) Encrypting all data entered into a web form",
    "B) Verifying that user input meets expected criteria before processing it",
    "C) Logging all user input for security auditing",
    "D) Blocking all special characters at the firewall level"
]
q97_answer = "B"
q97_explanation = "Input validation checks that data entered by a user meets expected criteria, preventing attacks like SQL injection and XSS from reaching backend systems."

user_ans, correct, explain = ask_question(q97, q97_options, q97_answer, q97_explanation)
check_answer(user_ans, correct, explain)

# Question 98
q98 = "Q98: Which of the following BEST describes a buffer overflow attack?"
q98_options = [
    "A) Flooding a network with traffic to cause an outage",
    "B) Sending more data to a memory buffer than it can handle to overwrite adjacent memory",
    "C) Injecting malicious SQL into a database query",
    "D) Intercepting data between a client and server"
]
q98_answer = "B"
q98_explanation = "A buffer overflow sends more data than a buffer can hold, potentially overwriting memory and allowing an attacker to execute arbitrary code."

user_ans, correct, explain = ask_question(q98, q98_options, q98_answer, q98_explanation)
check_answer(user_ans, correct, explain)

# Question 99
q99 = "Q99: Which of the following BEST describes the purpose of an acceptable use policy (AUP)?"
q99_options = [
    "A) To define how encryption is applied across the organization",
    "B) To document rules for appropriate use of company systems and resources",
    "C) To outline steps for responding to a security incident",
    "D) To assign user roles and permissions across the network"
]
q99_answer = "B"
q99_explanation = "An AUP defines what is and is not acceptable when using company systems, protecting the organization legally and setting clear behavioral expectations."

user_ans, correct, explain = ask_question(q99, q99_options, q99_answer, q99_explanation)
check_answer(user_ans, correct, explain)

# Question 100
q100 = "Q100: Which of the following BEST describes the difference between a threat and a vulnerability?"
q100_options = [
    "A) A threat is a weakness in a system, a vulnerability is something that exploits it",
    "B) A threat is a potential danger, a vulnerability is a weakness that could be exploited",
    "C) They mean the same thing in cybersecurity",
    "D) A vulnerability is an active attack, a threat is a potential one"
]
q100_answer = "B"
q100_explanation = "A vulnerability is a weakness in a system. A threat is anything that could exploit that weakness. Risk is what happens when a threat exploits a vulnerability."

user_ans, correct, explain = ask_question(q100, q100_options, q100_answer, q100_explanation)
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

def run_quiz():
    all_questions = [
        (q1, q1_options, q1_answer, q1_explanation),
        (q2, q2_options, q2_answer, q2_explanation),
        (q3, q3_options, q3_answer, q3_explanation),
        (q4, q4_options, q4_answer, q4_explanation),
        (q5, q5_options, q5_answer, q5_explanation),
        (q6, q6_options, q6_answer, q6_explanation),
        (q7, q7_options, q7_answer, q7_explanation),
        (q8, q8_options, q8_answer, q8_explanation),
        (q9, q9_options, q9_answer, q9_explanation),
        (q10, q10_options, q10_answer, q10_explanation),
        (q11, q11_options, q11_answer, q11_explanation),
        (q12, q12_options, q12_answer, q12_explanation),
        (q13, q13_options, q13_answer, q13_explanation),
        (q14, q14_options, q14_answer, q14_explanation),
        (q15, q15_options, q15_answer, q15_explanation),
        (q16, q16_options, q16_answer, q16_explanation),
        (q17, q17_options, q17_answer, q17_explanation),
        (q18, q18_options, q18_answer, q18_explanation),
        (q19, q19_options, q19_answer, q19_explanation),
        (q20, q20_options, q20_answer, q20_explanation),
        (q21, q21_options, q21_answer, q21_explanation),
        (q22, q22_options, q22_answer, q22_explanation),
        (q23, q23_options, q23_answer, q23_explanation),
        (q24, q24_options, q24_answer, q24_explanation),
        (q25, q25_options, q25_answer, q25_explanation),
        (q26, q26_options, q26_answer, q26_explanation),
        (q27, q27_options, q27_answer, q27_explanation),
        (q28, q28_options, q28_answer, q28_explanation),
        (q29, q29_options, q29_answer, q29_explanation),
        (q30, q30_options, q30_answer, q30_explanation),
        (q31, q31_options, q31_answer, q31_explanation),
        (q32, q32_options, q32_answer, q32_explanation),
        (q33, q33_options, q33_answer, q33_explanation),
        (q34, q34_options, q34_answer, q34_explanation),
        (q35, q35_options, q35_answer, q35_explanation),
        (q36, q36_options, q36_answer, q36_explanation),
        (q37, q37_options, q37_answer, q37_explanation),
        (q38, q38_options, q38_answer, q38_explanation),
        (q39, q39_options, q39_answer, q39_explanation),
        (q40, q40_options, q40_answer, q40_explanation),
        (q41, q41_options, q41_answer, q41_explanation),
        (q42, q42_options, q42_answer, q42_explanation),
        (q43, q43_options, q43_answer, q43_explanation),
        (q44, q44_options, q44_answer, q44_explanation),
        (q45, q45_options, q45_answer, q45_explanation),
        (q46, q46_options, q46_answer, q46_explanation),
        (q47, q47_options, q47_answer, q47_explanation),
        (q48, q48_options, q48_answer, q48_explanation),
        (q49, q49_options, q49_answer, q49_explanation),
        (q50, q50_options, q50_answer, q50_explanation),
        (q51, q51_options, q51_answer, q51_explanation),
        (q52, q52_options, q52_answer, q52_explanation),
        (q53, q53_options, q53_answer, q53_explanation),
        (q54, q54_options, q54_answer, q54_explanation),
        (q55, q55_options, q55_answer, q55_explanation),
        (q56, q56_options, q56_answer, q56_explanation),
        (q57, q57_options, q57_answer, q57_explanation),
        (q58, q58_options, q58_answer, q58_explanation),
        (q59, q59_options, q59_answer, q59_explanation),
        (q60, q60_options, q60_answer, q60_explanation),
        (q61, q61_options, q61_answer, q61_explanation),
        (q62, q62_options, q62_answer, q62_explanation),
        (q63, q63_options, q63_answer, q63_explanation),
        (q64, q64_options, q64_answer, q64_explanation),
        (q65, q65_options, q65_answer, q65_explanation),
        (q66, q66_options, q66_answer, q66_explanation),
        (q67, q67_options, q67_answer, q67_explanation),
        (q68, q68_options, q68_answer, q68_explanation),
        (q69, q69_options, q69_answer, q69_explanation),
        (q70, q70_options, q70_answer, q70_explanation),
        (q71, q71_options, q71_answer, q71_explanation),
        (q72, q72_options, q72_answer, q72_explanation),
        (q73, q73_options, q73_answer, q73_explanation),
        (q74, q74_options, q74_answer, q74_explanation),
        (q75, q75_options, q75_answer, q75_explanation),
        (q76, q76_options, q76_answer, q76_explanation),
        (q77, q77_options, q77_answer, q77_explanation),
        (q78, q78_options, q78_answer, q78_explanation),
        (q79, q79_options, q79_answer, q79_explanation),
        (q80, q80_options, q80_answer, q80_explanation),
        (q81, q81_options, q81_answer, q81_explanation),
        (q82, q82_options, q82_answer, q82_explanation),
        (q83, q83_options, q83_answer, q83_explanation),
        (q84, q84_options, q84_answer, q84_explanation),
        (q85, q85_options, q85_answer, q85_explanation),
        (q86, q86_options, q86_answer, q86_explanation),
        (q87, q87_options, q87_answer, q87_explanation),
        (q88, q88_options, q88_answer, q88_explanation),
        (q89, q89_options, q89_answer, q89_explanation),
        (q90, q90_options, q90_answer, q90_explanation),
        (q91, q91_options, q91_answer, q91_explanation),
        (q92, q92_options, q92_answer, q92_explanation),
        (q93, q93_options, q93_answer, q93_explanation),
        (q94, q94_options, q94_answer, q94_explanation),
        (q95, q95_options, q95_answer, q95_explanation),
        (q96, q96_options, q96_answer, q96_explanation),
        (q97, q97_options, q97_answer, q97_explanation),
        (q98, q98_options, q98_answer, q98_explanation),
        (q99, q99_options, q99_answer, q99_explanation),
        (q100, q100_options, q100_answer, q100_explanation),
    ]

    random.shuffle(all_questions)

    for question, options, answer, explanation in all_questions:
        correct_text = None
        for opt in options:
            if opt.startswith(answer + ")"):
                correct_text = opt[3:]
                break

        answer_texts = [opt[3:] for opt in options]
        random.shuffle(answer_texts)

        letters = ["A", "B", "C", "D"]
        new_options = [f"{letters[i]}) {answer_texts[i]}" for i in range(4)]

        new_answer = None
        for i, text in enumerate(answer_texts):
            if text == correct_text:
                new_answer = letters[i]
                break

        user_ans, correct, explain = ask_question(question, new_options, new_answer, explanation)
        check_answer(user_ans, correct, explain)

run_quiz()
