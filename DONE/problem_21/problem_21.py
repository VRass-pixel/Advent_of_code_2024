from functools import cache

@cache
def best_dirpad(x, y, dx, dy, robots, invalid):
    ret = None
    todo = [(x, y, "")]

    while len(todo) > 0:
        x, y, path = todo.pop(0)
        if (x, y) == (dx, dy):
            ret = minn(ret, best_robot(path + "A", robots - 1))
        elif (x, y) != invalid:
            for ox, oy, val in ((-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v")):
                if is_dir(x, dx, ox) or is_dir(y, dy, oy):
                    todo.append((x + ox, y + oy, path + val))

    return ret

@cache
def best_robot(path, robots):
    if robots == 1:
        return len(path)

    ret = 0
    pad = decode_pad(".^A<v>", 3)
    x, y = pad["A"]

    for val in path:
        dx, dy = pad[val]
        ret += best_dirpad(x, y, dx, dy, robots, pad["."])
        x, y = dx, dy

    return ret

def minn(*vals):
    vals = [x for x in vals if x is not None]
    return vals[0] if len(vals) == 1 else min(*vals)

def decode_pad(val, width):
    return {val: (x % width, x // width) for x, val in enumerate(val)}

def is_dir(start, dest, change):
    return (change < 0 and dest < start) or (change > 0 and dest > start)

def cheapest(x, y, dx, dy, robots, invalid):
    ret = None
    todo = [(x, y, "")]
    while len(todo) > 0:
        x, y, path = todo.pop(0)
        if (x, y) == (dx, dy):
            ret = minn(ret, best_robot(path + "A", robots))
        elif (x, y) != invalid:
            for ox, oy, val in ((-1, 0, "<"), (1, 0, ">"), (0, -1, "^"), (0, 1, "v")):
                if is_dir(x, dx, ox) or is_dir(y, dy, oy):
                    todo.append((x + ox, y + oy, path + val))
    return ret

def calc(log, values, mode):
    ret = 0
    pad = decode_pad("789456123.0A", 3)
    for row in values:
        result = 0
        x, y = pad["A"]
        for val in row:
            dx, dy = pad[val]
            result += cheapest(x, y, dx, dy, 3 if mode == 1 else 26, pad["."])
            x, y = dx, dy
        ret += result * int(row[:-1].lstrip("0"))
    return ret 

def test(log):
    values = log.decode_values("""
        029A
        980A
        179A
        456A
        379A
    """)

    log.test(calc(log, values, 1), '126384')

def run(log, values):
    log(calc(log, values, 1))
    log(calc(log, values, 2))

if __name__ == "__main__":
    import sys, os
    with open('problem_21/input_21.txt') as f: values = [x.strip("\r\n") for x in f.readlines()]
    run(print, values)