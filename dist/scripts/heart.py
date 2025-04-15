import sys
import os
import subprocess

class Launcher:
    def __init__(self, script_name: str):
        self.script_name = self._normalize(script_name)
        self.base_path = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
        self.scripts_path = os.path.join(self.base_path, 'interface')

    def _normalize(self, name):
        return name.lower().replace('_', '').replace('-', '').replace(' ', '')

    def _find_match(self):
        if not os.path.exists(self.scripts_path):
            print("❌ 'scripts' folder not found.")
            return None

        for file in os.listdir(self.scripts_path):
            name, ext = os.path.splitext(file)
            if ext in ['.py', '.exe'] and self._normalize(name) == self.script_name:
                return os.path.join(self.scripts_path, file)
        return None

    def launch(self):
        print(f"🔍 Searching for: {self.script_name} in {self.scripts_path}")
        match = self._find_match()

        if match:
            if match.endswith('.py'):
                print(f"✅ Found Python script: {match}. Launching...")
                subprocess.Popen([sys.executable, match], shell=True)
                sys.exit()

            elif match.endswith('.exe'):
                print(f"✅ Found EXE file: {match}. Launching...")
                subprocess.Popen([match], shell=True)
        else:
            print("❌ No matching .py or .exe file found in 'scripts' folder.")
