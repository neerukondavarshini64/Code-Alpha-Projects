import re

def analyze_code(code):
    issues = []

    lines = code.splitlines()

    for line_no, line in enumerate(lines, start=1):

        # Inline JavaScript
        if "<script>" in line.lower():
            issues.append((
                "Medium",
                line_no,
                "Inline JavaScript",
                "Move JavaScript to external files and apply CSP."
            ))

        # onclick
        if "onclick=" in line.lower():
            issues.append((
                "Medium",
                line_no,
                "Inline Event Handler",
                "Avoid inline event handlers."
            ))

        # onload
        if "onload=" in line.lower():
            issues.append((
                "Medium",
                line_no,
                "Inline Event Handler",
                "Avoid inline event handlers."
            ))

        # iframe
        if "<iframe" in line.lower():
            issues.append((
                "Low",
                line_no,
                "Iframe Detected",
                "Ensure iframe sources are trusted."
            ))

        # Form without HTTPS
        if '<form' in line.lower() and 'http://' in line.lower():
            issues.append((
                "High",
                line_no,
                "Insecure Form Action",
                "Use HTTPS instead of HTTP."
            ))

        # TODO
        if "TODO" in line.upper():
            issues.append((
                "Low",
                line_no,
                "TODO Comment",
                "Review unfinished HTML before deployment."
            ))

    return issues