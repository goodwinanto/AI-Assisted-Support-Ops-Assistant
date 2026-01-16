import subprocess

def analyze(issue, report):
    raw = "\n".join([f"{k}:\n{v}" for k, v in report.items()])

    prompt = f"""
You are an operations support assistant.

Return output in this format ONLY:

SYSTEM STATUS:
- Network: OK/Issue
- CPU: OK/High
- Memory: OK/Low
- Disk: OK/High

MAIN ISSUE:
<one short sentence>

RECOMMENDED ACTIONS:
- 3 short bullet points

Rules:
- Be concise
- No explanations
- No filler text
- No assumptions beyond diagnostics

Diagnostics:
{raw}

User issue: {issue}
"""

    try:
        return subprocess.check_output(
            f'ollama run llama3 "{prompt}"',
            shell=True,
            text=True
        ).strip()
    except:
        return "AI analysis failed"
