import sys

# sys.argv[0] is ALWAYS the name of the script
script_name = sys.argv[0]

# Everything after that is a user argument
arguments = sys.argv[1:]

print(f"Running script: {script_name}")
print(f"Arguments passed: {arguments}")

# Example logic:
if "--force" in sys.argv:
    print("Force mode enabled!")


# See everywhere Python is looking for libraries
for path in sys.path:
    print(path)

# PRO TIP: You can manually add a folder to the path
# so you can import local files from anywhere.
sys.path.append('/home/user/my_secret_library')
