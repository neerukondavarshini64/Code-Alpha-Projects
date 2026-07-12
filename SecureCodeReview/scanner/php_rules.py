import re


def analyze_code(code):
    issues = []

    lines = code.splitlines()

    for line_no, line in enumerate(lines, start=1):

        # -------------------------
        # eval()
        # -------------------------
        if "eval(" in line:
            issues.append((
                "High",
                line_no,
                "Use of eval()",
                "Avoid eval(). It can execute arbitrary PHP code."
            ))

        # -------------------------
        # exec()
        # -------------------------
        if "exec(" in line:
            issues.append((
                "High",
                line_no,
                "Use of exec()",
                "Avoid exec(). It may lead to command injection."
            ))

        # -------------------------
        # system()
        # -------------------------
        if "system(" in line:
            issues.append((
                "High",
                line_no,
                "Command Injection",
                "Avoid system(). Validate user input before executing commands."
            ))

        # -------------------------
        # Hardcoded Password
        # -------------------------
        if re.search(r'password\s*=\s*["\'].*["\']', line, re.IGNORECASE):
            issues.append((
                "High",
                line_no,
                "Hardcoded Password",
                "Store passwords securely using environment variables."
            ))

        # -------------------------
        # SQL Injection
        # -------------------------
        if "SELECT" in line.upper():

            if "." in line or "$_" in line:

                issues.append((
                    "High",
                    line_no,
                    "Possible SQL Injection",
                    "Use prepared statements (PDO or MySQLi)."
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