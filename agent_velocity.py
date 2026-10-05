import os
import subprocess
import sys

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[Warning/Error] {result.stderr.strip()}")
    return result.stdout.strip()

print("==================================================")
print("🚀 LUXERA HIGH-VELOCITY AUTONOMOUS DEPLOYMENT AGENT")
print("==================================================")

username = input("Enter your GitHub username: ").strip()
repo_name = "casa-app"

if not username:
    print("Username is required. Halting agent.")
    sys.exit(1)

print(f"\n[1/3] Verifying and Staging Core Asset Files...")
required_files = ["index.html", "dispute.html"]
for f in required_files:
    if os.path.exists(f):
        print(f"  ✔ Found production file: {f}")
    else:
        print(f"  ✖ Missing {f}! Make sure it is in this folder.")

print(f"\n[2/3] Initializing Git Pipeline...")
run_cmd("git init")
run_cmd("git add .")
run_cmd('git commit -m "Automated High-Velocity Agent Release"')
run_cmd("git branch -M main")

remote_url = f"https://github.com/{username}/{repo_name}.git"
run_cmd(f"git remote add origin {remote_url}")

print(f"\n[3/3] Pushing to GitHub...")
push_output = run_cmd("git push -u origin main")
print(push_output)

print("\n==================================================")
print("🎯 DEPLOYMENT COMPLETE — YOUR LIVE ASSET URLS:")
print(f"1. Life App:       https://{username}.github.io/{repo_name}/")
print(f"2. Dispute Engine: https://{username}.github.io/{repo_name}/dispute.html")
print("==================================================")
