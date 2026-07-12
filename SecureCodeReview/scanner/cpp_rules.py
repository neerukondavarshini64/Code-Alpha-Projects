import re


def analyze_code(code):
    issues = []

    lines = code.splitlines()

    has_new = False
    has_delete = False

    for line_no, line in enumerate(lines, start=1):

        # -------------------------
        # strcpy()
        # -------------------------
        if "strcpy(" in line:
            issues.append((
                "High",
                line_no,
                "Unsafe strcpy()",
                "Use strncpy() or std::string instead."
            ))

        # -------------------------
        # sprintf()
        # -------------------------
        if "sprintf(" in line:
            issues.append((
                "Medium",
                line_no,
                "Unsafe sprintf()",
                "Use snprintf() to avoid buffer overflow."
            ))

        # -------------------------
        # scanf()
        # -------------------------
        if re.search(r'scanf\s*\(\s*"%s"', line):
            issues.append((
                "Medium",
                line_no,
                "Unsafe scanf()",
                "Specify a field width or use safer input methods."
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
        # new
        # -------------------------
        if "new " in line:
            has_new = True

        # -------------------------
        # delete
        # -------------------------
        if "delete " in line:
            has_delete = True

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

    # -------------------------
    # Memory Leak Check
    # -------------------------
    if has_new and not has_delete:
        issues.append((
            "Medium",
            "-",
            "Possible Memory Leak",
            "Memory allocated using 'new' should be released using 'delete'."
        ))

    return issues