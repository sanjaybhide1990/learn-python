import subprocess
import os

print(subprocess.Popen('echo "Hello World!"',shell=True))
print(os.system('echo "Hello World!"'))