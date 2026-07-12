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
                "Avoid eval(). It can execute malicious code."
            ))

        # -------------------------
        # exec()
        # -------------------------
        if "exec(" in line:
            issues.append((
                "High",
                line_no,
                "Use of exec()",
                "Avoid exec(). It executes arbitrary Python code."
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
        sql_keywords = ["SELECT", "INSERT", "UPDATE", "DELETE"]

        if any(word in line.upper() for word in sql_keywords):

            if "%" in line or "+" in line or ".format(" in line or "f\"" in line or "f'" in line:

                issues.append((
                    "High",
                    line_no,
                    "Possible SQL Injection",
                    "Use parameterized SQL queries."
                ))

        # -------------------------
        # os.system()
        # -------------------------
        if "os.system(" in line:
            issues.append((
                "High",
                line_no,
                "Command Injection",
                "Avoid os.system(). Use subprocess safely."
            ))

        # -------------------------
        # shell=True
        # -------------------------
        if "shell=True" in line:
            issues.append((
                "High",
                line_no,
                "Shell Execution",
                "Avoid shell=True whenever possible."
            ))

        # -------------------------
        # Dangerous imports
        # -------------------------
        if "import pickle" in line:
            issues.append((
                "Medium",
                line_no,
                "Dangerous Import (pickle)",
                "Review usage of pickle carefully."
            ))

        if "import subprocess" in line:
            issues.append((
                "Medium",
                line_no,
                "Dangerous Import (subprocess)",
                "Review subprocess usage carefully."
            ))

        # -------------------------
        # Bare except
        # -------------------------
        if line.strip() == "except:":
            issues.append((
                "Medium",
                line_no,
                "Bare Except",
                "Catch specific exceptions instead of using except:"
            ))

        # -------------------------
        # chmod 777
        # -------------------------
        if "0o777" in line or "chmod(777" in line:
            issues.append((
                "High",
                line_no,
                "Insecure File Permission",
                "Avoid giving full permissions (777)."
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