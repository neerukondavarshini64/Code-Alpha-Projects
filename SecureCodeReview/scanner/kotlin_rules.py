import re

def analyze_code(code):
    issues = []

    lines = code.splitlines()

    for line_no, line in enumerate(lines, start=1):

        # Hardcoded Password
        if re.search(r'password\s*=\s*".*"', line, re.IGNORECASE):
            issues.append((
                "High",
                line_no,
                "Hardcoded Password",
                "Store passwords securely."
            ))

        # Runtime.exec()
        if "Runtime.getRuntime().exec(" in line:
            issues.append((
                "High",
                line_no,
                "Command Execution",
                "Avoid Runtime.exec() with untrusted input."
            ))

        # SQL Injection
        if "SELECT" in line.upper() and "+" in line:
            issues.append((
                "High",
                line_no,
                "Possible SQL Injection",
                "Use prepared statements."
            ))

        # MD5
        if "MD5" in line.upper():
            issues.append((
                "Medium",
                line_no,
                "Weak Cryptography",
                "Use SHA-256 or stronger algorithms."
            ))

        # TODO
        if "TODO" in line.upper():
            issues.append((
                "Low",
                line_no,
                "TODO Comment",
                "Review unfinished code."
            ))

    return issues