import re

def analyze_code(code):
    issues = []

    lines = code.splitlines()

    for line_no, line in enumerate(lines, start=1):

        # eval()
        if "eval(" in line:
            issues.append((
                "High",
                line_no,
                "Use of eval()",
                "Avoid eval(). It can execute malicious code."
            ))

        # innerHTML
        if "innerHTML" in line:
            issues.append((
                "High",
                line_no,
                "Unsafe innerHTML",
                "Use textContent or sanitize user input."
            ))

        # document.write()
        if "document.write(" in line:
            issues.append((
                "Medium",
                line_no,
                "document.write()",
                "Avoid document.write()."
            ))

        # Hardcoded Password
        if re.search(r'password\s*=\s*["\'].*["\']', line, re.IGNORECASE):
            issues.append((
                "High",
                line_no,
                "Hardcoded Password",
                "Store passwords securely."
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