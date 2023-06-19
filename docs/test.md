```python exec="on"
print("Hello Markdown!")
```

```python exec="on"
import subprocess
cmd = """sshpass -p "joderCONdipc123$%&" ssh iortiz@atlas-edr.sw.ehu.es -p 22 'uname -a'"""
cmd1= """ sshpass -p "joderCONdipc123$%&" ssh iortiz@atlas-edr.sw.ehu.es -p 22 'hostname; whoami;ls; exit' """

# Execute the command and capture the output
output = subprocess.getoutput(cmd)
output1 = subprocess.getoutput(cmd1)

# Print the output
print(output)
print(" ")
print(output1)
```

