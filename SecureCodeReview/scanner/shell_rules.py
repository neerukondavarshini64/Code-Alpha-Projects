import re

def analyze_code(code):
    issues = []

    lines = code.splitlines()

    for line_no, line in enumerate(lines, start=1):

        # rm -rf
        if "rm -rf" in line:
            issues.append((
                "High",
                line_no,
                "Dangerous Command",
                "Avoid using 'rm -rf' as it can permanently delete files."
            ))

        # sudo
        if line.strip().startswith("sudo"):
            issues.append((
                "Medium",
                line_no,
                "Use of sudo",
                "Avoid unnecessary root privileges."
            ))

        # curl | sh
        if "curl" in line and "|" in line and "sh" in line:
            issues.append((
                "High",
                line_no,
                "Remote Script Execution",
                "Avoid executing downloaded scripts directly."
            ))

        # wget | sh
        if "wget" in line and "|" in line and "sh" in line:
            issues.append((
                "High",
                line_no,
                "Remote Script Execution",
                "Avoid executing downloaded scripts directly."
            ))

        # chmod 777
        if "chmod 777" in line:
            issues.append((
                "High",
                line_no,
                "Insecure File Permission",
                "Avoid granting 777 permissions."
            ))

        # TODO
        if "TODO" in line.upper():
            issues.append((
                "Low",
                line_no,
                "TODO Comment",
                "Review unfinished shell script before deployment."
            ))

    return issues