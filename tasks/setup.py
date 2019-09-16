import sys, os, subprocess
from io import StringIO
from pip._internal import main as pip
import argparse

parser = argparse.ArgumentParser(description="Prettify some Html.")
parser.add_argument("-p", "--path", type=str, required=False, default="./env", help="Path of virtual enviroment to create.")
parser.add_argument("-r", "--requirements", type=str, required=False, default="./requirements.txt", help="Path of requirements.")
args = parser.parse_args()

env_path = args.path
requirements_path = args.requirements

# Make sure 'virtualenv' is installed
defaultOutput = sys.stdout
output = StringIO()
sys.stdout = output

pip(["list"])
packages = output.getvalue()
packages = packages.split("\n")
packages.pop(0)
packages.pop(0)
packages = list(map(lambda x: x.split(' ')[0], packages))

sys.stdout = defaultOutput

if("virtualenv" not in packages):
    command = "python -m pip install virtualenv"
    subprocess.run(command)
else:
    print("'virtialenv' package found")

# Create virtual enviroment
print("Create virtual enviroment...")
command = "virtualenv " + env_path
subprocess.run(command)

# Install required packages
print("Install required packages...")
command = env_path + "/Scripts/pip install -r " + requirements_path
subprocess.run(command)

print("Setup of virtual enviroment finished.")
