from flask import Flask, render_template, request
from scanner.analyzer import analyze_file
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def home():

    submitted_code = ""
    issues = []
    language = ""

    total = 0
    high = 0
    medium = 0
    low = 0

    if request.method == "POST":

        submitted_code = request.form.get("code", "").strip()

        selected_language = request.form.get("language", "py")

        uploaded_file = request.files.get("code_file")

        language_map = {
            "py": "Python",
            "java": "Java",
            "js": "JavaScript",
            "php": "PHP",
            "c": "C",
            "cpp": "C++",
            "cs": "C#",
            "go": "Go",
            "ts": "TypeScript",
            "rb": "Ruby",
            "kt": "Kotlin",
            "swift": "Swift",
            "sql": "SQL",
            "html": "HTML",
            "css": "CSS",
            "sh": "Shell Script"
        }

        
        if uploaded_file and uploaded_file.filename != "":

            filename = uploaded_file.filename

            filepath = os.path.join(UPLOAD_FOLDER, filename)

            uploaded_file.save(filepath)

            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                submitted_code = f.read()

            language = language_map.get(
                filename.split(".")[-1].lower(),
                "Unknown"
            )

            issues = analyze_file(submitted_code, filename)

    
        elif submitted_code:

            language = language_map.get(selected_language, "Python")

            filename = "sample." + selected_language

            issues = analyze_file(submitted_code, filename)

    
        total = len(issues)

        for issue in issues:

            severity = issue[0]

            if severity == "High":
                high += 1

            elif severity == "Medium":
                medium += 1

            elif severity == "Low":
                low += 1

    return render_template(
        "index.html",
        submitted_code=submitted_code,
        issues=issues,
        language=language,
        total=total,
        high=high,
        medium=medium,
        low=low
    )


if __name__ == "__main__":
    app.run(debug=True)