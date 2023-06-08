import subprocess

def on_pre_build(config):
    subprocess.run(["python", "myscript.py"])

