import re


def analyze_code(code):
    issues = []

    lines = code.splitlines()

    for line_no, line in enumerate(lines, start=1):

        # -------------------------
        # Runtime.exec()
        # -------------------------
        if "Runtime.getRuntime().exec(" in line:
            issues.append((
                "High",
                line_no,
                "Use of Runtime.exec()",
                "Avoid Runtime.exec(). It may lead to command injection."
            ))

        # -------------------------
        # Hardcoded Password
        # -------------------------
        if re.search(r'password\s*=\s*".*"', line, re.IGNORECASE):
            issues.append((
                "High",
                line_no,
                "Hardcoded Password",
                "Store passwords securely."
            ))

        # -------------------------
        # SQL Injection
        # -------------------------
        if "SELECT" in line.upper():

            if "+" in line or ".concat(" in line:

                issues.append((
                    "High",
                    line_no,
                    "Possible SQL Injection",
                    "Use PreparedStatement instead of string concatenation."
                ))

        # -------------------------
        # Weak Cryptography
        # -------------------------
        if "MD5" in line.upper():

            issues.append((
                "Medium",
                line_no,
                "Weak Cryptography",
                "Avoid MD5. Use SHA-256 or stronger algorithms."
            ))

        # -------------------------
        # TODO Comment
        # -------------------------
        if "TODO" in line.upper():

            issues.append((
                "Low",
                line_no,
                "TODO Comment",
                "Review unfinished code before deployment."
            ))

    return issues