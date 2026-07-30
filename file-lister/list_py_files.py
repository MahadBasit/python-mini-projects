import os
import sys
from datetime import datetime

if len(sys.argv) == 2:
    folder = sys.argv[1]
else:
    sys.exit('Usage: list_py_files.py <folder>')
try:
    files = os.listdir(folder)
except FileNotFoundError:
    sys.exit(f'Folder not found!: {folder}')

latest = None

for file in files:
    if os.path.splitext(file)[1] == '.py':
        full_path = os.path.join(folder, file)
        mtime = datetime.fromtimestamp(os.path.getmtime(full_path))
        mtime_str = mtime.strftime("%d/%m/%Y %I:%M %p")
        print(f'{file} - {os.path.getsize(full_path)} - {mtime_str}')

        if latest is None or mtime > latest:
            latest = mtime
            latest_name = file


if latest is None:
    print('No .py files!')
else:
    days_ago = (datetime.now() - latest).days
    print(f'\nMost recent: {latest_name}, {days_ago} days ago')