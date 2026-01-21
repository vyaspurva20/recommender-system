import os
import subprocess
from pathlib import Path
from groq import Groq
from github import Github

# 1. Read CI error log
ERROR_LOG = "error.log"

if not Path(ERROR_LOG).exists():
    print("No error log found")
    exit(0)

errors = Path(ERROR_LOG).read_text().strip()
if not errors:
    print("No errors detected")
    exit(0)

# 2. Send error to Qwen-Coder (via Groq)
client = Groq(api_key=os.environ["GROQ_API_KEY"])

prompt = f"""
You are a senior Python engineer.

CI FAILED WITH THIS ERROR:
{errors}

TASK:
1. Fix the bug
2. Return ONLY corrected code
3. First line must be: filename:<file>
"""

response = client.chat.completions.create(
    model="qwen-2.5-coder-32b",
    messages=[{"role": "user", "content": prompt}],
    temperature=0
)

output = response.choices[0].message.content.strip()
print(output)

# 3. Apply fix locally
lines = output.splitlines()
filename = lines[0].replace("filename:", "").strip()
code = "\n".join(lines[1:])

Path(filename).write_text(code)

# 4. Create new git branch
BRANCH = "ai-fix-branch"

subprocess.run(["git", "checkout", "-b", BRANCH])
subprocess.run(["git", "add", filename])
subprocess.run(["git", "commit", "-m", "AI fix: CI failure"])
subprocess.run(["git", "push", "-u", "origin", BRANCH])

# 5. Open Pull Request
g = Github(os.environ["GITHUB_TOKEN"])
repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])

repo.create_pull(
    title="AI Fix: CI failure",
    body="This PR was generated automatically by Qwen-Coder via Groq.",
    head=BRANCH,
    base="main"
)

print("Pull Request created successfully")
