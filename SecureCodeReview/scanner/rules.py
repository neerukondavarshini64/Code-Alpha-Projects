import re

def analyze_code(code):
    issues = []

    # 1. eval()
    if "eval(" in code:
        issues.append(("High", "Use of eval()", "Avoid eval(). It can execute malicious code."))

    # 2. exec()
    if "exec(" in code:
        issues.append(("High", "Use of exec()", "Avoid exec(). It executes arbitrary Python code."))

    # 3. Hardcoded Password
    if re.search(r'password\s*=\s*["\'].*["\']', code, re.IGNORECASE):
        issues.append(("High", "Hardcoded Password", "Store passwords securely using environment variables."))

    # 4. SQL Injection
    sql_patterns = [
        "SELECT",
        "INSERT",
        "UPDATE",
        "DELETE"
    ]

    if any(keyword in code.upper() for keyword in sql_patterns) and "%" in code:
        issues.append(("High", "Possible SQL Injection", "Use parameterized SQL queries."))

    # 5. os.system()
    if "os.system(" in code:
        issues.append(("High", "Command Injection", "Avoid os.system(). Use subprocess safely."))

    # 6. subprocess with shell=True
    if "shell=True" in code:
        issues.append(("High", "Shell Execution", "Avoid shell=True whenever possible."))

    # 7. Dangerous Imports
    dangerous_imports = [
        "pickle",
        "subprocess"
    ]

    for module in dangerous_imports:
        if f"import {module}" in code:
            issues.append(("Medium", f"Dangerous Import ({module})",
                           f"Review usage of {module} carefully."))

    # 8. Weak Exception Handling
    if "except:" in code:
        issues.append(("Medium", "Bare Except", "Catch specific exceptions instead of using except:"))

    # 9. chmod 777
    if "chmod(777" in code or "chmod(0o777" in code:
        issues.append(("High", "Insecure File Permission", "Avoid giving full permissions (777)."))

    # 10. TODO Comments
    if "TODO" in code.upper():
        issues.append(("Low", "TODO Comment", "Review unfinished code before deployment."))

    return issues