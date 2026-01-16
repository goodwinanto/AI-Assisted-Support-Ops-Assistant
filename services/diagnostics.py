import subprocess

HARDWARE_ISSUES = [
    "not switching on", "no power", "dead", "black screen",
    "won't start", "not booting", "no display"
]

EXTERNAL_DEVICE = [
    "friend", "brother", "sister", "someone else's",
    "another laptop", "other device"
]

def run(cmd):
    try:
        return subprocess.check_output(cmd, shell=True, text=True).strip()
    except:
        return "FAILED"

def run_diagnostics():
    return {
        "Ping": run("ping -c 1 google.com"),
        "CPU": run("top -bn1 | head -5"),
        "Disk": run("df -h | head -5"),
        "Network": run("nmcli device status")
    }

def should_run_diagnostics(issue):
    text = issue.lower()

    if any(w in text for w in HARDWARE_ISSUES):
        return False, "Hardware / power issue detected."

    if any(w in text for w in EXTERNAL_DEVICE):
        return False, "Issue relates to another device."

    return True, "Diagnostics applicable."
