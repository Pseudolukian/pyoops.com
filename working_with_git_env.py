import os

os.system('echo VPS=123 >> $GITHUB_ENV')

print("="*8)
print(os.getenv("GITHUB_ENV"))
print("="*8)

