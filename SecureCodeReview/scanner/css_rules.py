import re

def analyze_code(code):
    issues = []

    lines = code.splitlines()

    for line_no, line in enumerate(lines, start=1):

        # expression()
        if "expression(" in line.lower():
            issues.append((
                "High",
                line_no,
                "CSS expression()",
                "Avoid using CSS expression() because it can execute JavaScript."
            ))

        # @import
        if "@import" in line.lower():
            issues.append((
                "Medium",
                line_no,
                "External CSS Import",
                "Review imported CSS files from external sources."
            ))

        # !important
        if "!important" in line.lower():
            issues.append((
                "Low",
                line_no,
                "Use of !important",
                "Avoid excessive use of !important for maintainability."
            ))

        # url(http://...)
        if re.search(r'url\s*\(\s*["\']?http://', line, re.IGNORECASE):
            issues.append((
                "High",
                line_no,
                "Insecure Resource",
                "Use HTTPS resources instead of HTTP."
            ))

        # TODO
        if "TODO" in line.upper():
            issues.append((
                "Low",
                line_no,
                "TODO Comment",
                "Review unfinished CSS before deployment."
            ))

    return issues