import os
import subprocess

MONGOSH_PATH = r"C:\Tools\mongosh\mongosh-2.1.4-win32-x64\bin\mongosh.exe"

base_path = os.path.dirname(__file__)
blueprint_path = os.path.join(base_path, 'interface', 'blueprint.txt')
actual_data_path = os.path.join(base_path, 'interface', 'actual_data.txt')

class CreateData:
    def __init__(self):
        self.content = ''
        with open(blueprint_path, 'r', encoding='utf-8') as file:
            self.content = file.read()

    def replace_data(self, name, vorname):
        replaced = self.content.replace('%name%', name).replace('%vorname%', vorname)

        with open(actual_data_path, 'w', encoding='utf-8') as file:
            file.write(replaced)
    
        return replaced

    def creationdb(self, replaced):
        command = replaced
        process = subprocess.Popen(
        [MONGOSH_PATH],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True  # For string input/output
            )
        stdout, stderr = process.communicate(command)
        print('output: ', stdout)
        print('Errors: ', stderr)