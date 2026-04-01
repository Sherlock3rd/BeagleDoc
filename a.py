import subprocess

with open("git_output.txt", "w", encoding="utf-8") as f:
    def run(cmd):
        f.write(f"Running: {cmd}\n")
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        f.write(res.stdout + "\n")
        if res.stderr:
            f.write("ERR: " + res.stderr + "\n")
        f.flush()

    run("git status")
    run("git add .")
    run("git commit -m \"docs: publish - update cp2/cp3 scope and cp2 timeline curve\"")
    run("git push")
    run("git status")
