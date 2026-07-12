import re


def analyze_code(code):
    issues = []

    lines = code.splitlines()

    for line_no, line in enumerate(lines, start=1):

        # -------------------------
        # gets()
        # -------------------------
        if "gets(" in line:
            issues.append((
                "High",
                line_no,
                "Unsafe gets()",
                "Avoid gets(). Use fgets() instead."
            ))

        # -------------------------
        # strcpy()
        # -------------------------
        if "strcpy(" in line:
            issues.append((
                "High",
                line_no,
                "Unsafe strcpy()",
                "Use strncpy() or safer string handling functions."
            ))

        # -------------------------
        # sprintf()
        # -------------------------
        if "sprintf(" in line:
            issues.append((
                "Medium",
                line_no,
                "Unsafe sprintf()",
                "Use snprintf() to prevent buffer overflow."
            ))

        # -------------------------
        # system()
        # -------------------------
        if "system(" in line:
            issues.append((
                "High",
                line_no,
                "Command Injection",
                "Avoid system(). Validate all user input before executing commands."
            ))

        # -------------------------
        # scanf("%s")
        # -------------------------
        if re.search(r'scanf\s*\(\s*"%s"', line):
            issues.append((
                "Medium",
                line_no,
                "Unsafe scanf()",
                "Specify a field width or use fgets() instead."
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