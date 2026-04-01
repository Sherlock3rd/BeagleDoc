import subprocess
result = subprocess.run(["git", "status"], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)
