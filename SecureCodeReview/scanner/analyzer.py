from scanner.python_rules import analyze_code as analyze_python
from scanner.java_rules import analyze_code as analyze_java
from scanner.javascript_rules import analyze_code as analyze_javascript
from scanner.php_rules import analyze_code as analyze_php
from scanner.c_rules import analyze_code as analyze_c
from scanner.cpp_rules import analyze_code as analyze_cpp
from scanner.csharp_rules import analyze_code as analyze_csharp

# These files will be created in the next steps
from scanner.go_rules import analyze_code as analyze_go
from scanner.typescript_rules import analyze_code as analyze_typescript
from scanner.ruby_rules import analyze_code as analyze_ruby
from scanner.kotlin_rules import analyze_code as analyze_kotlin
from scanner.swift_rules import analyze_code as analyze_swift
from scanner.sql_rules import analyze_code as analyze_sql
from scanner.html_rules import analyze_code as analyze_html
from scanner.css_rules import analyze_code as analyze_css
from scanner.shell_rules import analyze_code as analyze_shell


def analyze_file(code, filename):

    extension = filename.lower().split(".")[-1]

    if extension == "py":
        return analyze_python(code)

    elif extension == "java":
        return analyze_java(code)

    elif extension == "js":
        return analyze_javascript(code)

    elif extension == "ts":
        return analyze_typescript(code)

    elif extension == "php":
        return analyze_php(code)

    elif extension == "c":
        return analyze_c(code)

    elif extension == "cpp":
        return analyze_cpp(code)

    elif extension == "cs":
        return analyze_csharp(code)

    elif extension == "go":
        return analyze_go(code)

    elif extension == "rb":
        return analyze_ruby(code)

    elif extension == "kt":
        return analyze_kotlin(code)

    elif extension == "swift":
        return analyze_swift(code)

    elif extension == "sql":
        return analyze_sql(code)

    elif extension == "html":
        return analyze_html(code)

    elif extension == "css":
        return analyze_css(code)

    elif extension == "sh":
        return analyze_shell(code)

    else:
        return [
            (
                "Info",
                "-",
                "Unsupported Language",
                "This language is not supported yet."
            )
        ]