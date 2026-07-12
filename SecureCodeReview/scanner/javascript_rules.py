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
                "Avoid eval(). It can execute arbitrary JavaScript code."
            ))

        # -------------------------
        # document.write()
        # -------------------------
        if "document.write(" in line:
            issues.append((
                "Medium",
                line_no,
                "Use of document.write()",
                "Avoid document.write(). It may introduce XSS vulnerabilities."
            ))

        # -------------------------
        # innerHTML
        # -------------------------
        if ".innerHTML" in line:
            issues.append((
                "Medium",
                line_no,
                "Unsafe innerHTML",
                "Use textContent or sanitize user input before assigning to innerHTML."
            ))

        # -------------------------
        # Hardcoded Password
        # -------------------------
        if re.search(r'password\s*=\s*["\'].*["\']', line, re.IGNORECASE):
            issues.append((
                "High",
                line_no,
                "Hardcoded Password",
                "Store secrets securely instead of hardcoding them."
            ))

        # -------------------------
        # SQL Injection
        # -------------------------
        if "SELECT" in line.upper():

            if "+" in line or "`" in line:

                issues.append((
                    "High",
                    line_no,
                    "Possible SQL Injection",
                    "Use parameterized queries instead of string concatenation."
                ))

        # -------------------------
        # TODO
        # -------------------------
        if "TODO" in line.upper():
            issues.append((
                "Low",
                line_no,
                "TODO Comment",
                "Review unfinished code before deployment."
            ))

    return issues