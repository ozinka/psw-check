import time


def search(st: str) -> tuple:
    start_time = time.time()
    res = []
    res.append([])
    with open(r"c:\Users\kylik\Downloads\rockyou2024\rockyou2024.txt", mode='r', encoding="utf-8",
              errors='ignore') as f:
        start = 0
        f.seek(0, 2)  # os.SEEK_END = 2
        end = max = f.tell()
        pos = end // 2
        i = 0
        f.seek(pos)
        f.readline()
        line = f.readline().strip()
        res[0].append(f'Pos {i}:{pos * 100 // max}%, line: {line}')
        while (end - start) > 300:
            if st == line:
                start, end = pos - 100, pos + 100
                res[0].append(f'password is found')
                break
            elif st > line:
                start, pos, end = pos - 100, (pos + end) // 2, end
                f.seek(pos)
                f.readline()
                line = f.readline().strip()
                res[0].append(f'Pos {i}:{pos * 100 // max}%, line: {line}')
            else:
                start, pos, end = start - 100, (pos + start) // 2, pos + 100
                f.seek(pos)
                f.readline()
                line = f.readline().strip()
                res[0].append(f'Pos {i}:{pos * 100 // max}%, line: {line}')
                i += 1
        f.seek(start)
        f.readline()
        res.append([])
        while start < end - 20:
            res[1].append(f.readline().strip())
            start = f.tell()
        t = str((time.time() - start_time) * 1000)
        print(t)
        t = t[:t.find('.')] + t[t.find('.'):t.find('.') + 4] # 234234.234234
        print(t)
    return res[0], res[1], f'Search time: {int((time.time() - start_time) * 1000)} ms'


if __name__ == '__main__':
    print(search('l0pihara'))

# START -------*-------- POS ------------- END
# START ------POS------- END -------------
#       ------START----- END -------------

# flask --app flask_main run
