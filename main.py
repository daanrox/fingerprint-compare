import json
import os

class Checker:
    def __init__(self, previous_finger: dict, current_finger: dict):
        self.previous_files = {file['file'] for file in previous_finger['files']}
        self.current_files = {file['file'] for file in current_finger['files']}

    def check_files(self):
        changed = [{'file': file} for file in self.current_files - self.previous_files]
        removed = [file for file in self.previous_files - self.current_files]
        added = [{'file': file} for file in self.current_files - self.previous_files]

        return {'changed': changed, 'removed': removed, 'added': added}

if __name__ == '__main__':
    os.makedirs('main-data', exist_ok=True)

    with open('main-data/28.233.1.json') as previous_finger_file, \
         open('main-data/29.272.1.json') as current_finger_file:
        
        previous_finger_data = json.load(previous_finger_file)
        current_finger_data = json.load(current_finger_file)

    checker = Checker(previous_finger_data, current_finger_data)
    result = checker.check_files()

    print(f'Changed: {len(result["changed"])} files')
    print(f'Removed: {len(result["removed"])} files')
    print(f'Added: {len(result["added"])} files')
