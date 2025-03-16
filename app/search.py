"""
File Name: search.py
Description: Module contains one function to go through the big (hundreds of GB) TXT file with sorted lines and
             does search for specific string (password)

Created by: Vitaliy Osidach
Date Created: 2024.07.16

Version: 1.0

Usage:
    search('some_text')
"""
import time, os

DATA_DIR = os.environ.get('DATA_DIR', '../data')
PASSWORD_FILE = os.environ.get('PASSWORD_FILE', 'passwords.txt')

def search(st: str) -> tuple:
    start_time = time.time()
    res = []
    res.append([])
    print(os.path.join(DATA_DIR, PASSWORD_FILE))
    file_path = os.path.join(DATA_DIR, PASSWORD_FILE)
    with open(file_path, mode='r', encoding="utf-8", errors='ignore') as f:
        start = 0
        f.seek(0, 2)  # os.SEEK_END = 2
        end = max = f.tell()
        pos = end // 2
        i = 0
        f.seek(pos)
        f.readline()
        line = f.readline().strip()
        res[0].append(f'Pos {i}: {pos * 100 / max:.2f}%, line: {line:.10}')
        while (end - start) > 300:
            if st == line:
                start, end = pos - 100, pos + 100
                res[0].append(f'password is found')
                break
            elif st > line:
                start, pos, end = pos - 100, (pos + end) // 2, end  # 100 - edge effect, should be optimized
                f.seek(pos)
                f.readline()
                line = f.readline().strip()
                res[0].append(f'Pos {i}: {pos * 100 // max}%, line: {line:.10}')
            else:
                start, pos, end = start - 100, (pos + start) // 2, pos + 100  # 100 - edge effect, should be optimized
                f.seek(pos)
                f.readline()
                line = f.readline().strip()
                res[0].append(f'Pos {i}: {pos * 100 // max}%, line: {line:.10}')
            i += 1
        f.seek(start)
        f.readline()
        res.append([])
        while start < end - 20:
            res[1].append(f.readline().strip())
            start = f.tell()
    return res[0], res[1], f'Search time: {(time.time() - start_time) * 1000:.2f} ms'


if __name__ == '__main__':
    print(search('asdf'))

# START -------*-------- POS ------------- END
# START ------POS------- END -------------
#       ------START----- END -------------

# flask --app flask_main run
