import os
import subprocess

def run(cmd):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(res.stdout)
    if res.stderr:
        print("ERR:", res.stderr)

run("git add .")
run('git commit -m "docs: publish - update cp2/cp3 scope and cp2 timeline curve"')
run("git push")
run("git status")
