
def parse(filename):
    assert filename.endswith(".eps")
    lines = [i.strip() for i in open(filename)]
    assert lines[0].startswith("%!PS-Adobe-3")
    if "柱状图" in filename:
        data = zhuzhuangtu(lines)
    else:
        raise ValueError(filename)
    return data


def zhuzhuangtu(lines):
    """柱状图
    """
    words = [i for i in lines if '(' in i and not i.startswith("%")]

    l_key = []
    l_p = []
    l_height = []
    strata = []

    for s in words[-2:]:
        fs = s.split()
        strata.append(fs[2].strip("()"))


    for i, s in enumerate(words[:-2]):
        fs = s.split()
        try:
            x, y = float(fs[0]), float(fs[1])
        except Exception:
            continue

        if fs[-1] == "ta":
            tail = words[i+1]
            f = tail.index
            tail = tail[f("(")+1:f(")")+1]
            s = s.replace(")", tail)

        fs = s.split()
        key = fs[2].strip("()")

        if y > 400:
            if fs[-3] == ".5" and fs[-2] == '0':
                l_p.append((x, y, key))
        try:
            n = float(fs[-2])
            if 75 < n < 85:
                l_key.append((x, y, key))
                continue
        except Exception:
            continue

    heights = [lines[i+4] for i, s in enumerate(lines) if s.startswith("2.13")]
    for i in heights:
        x, y, _ = i.split()
        l_height.append((float(x), float(y)))

    l_key.sort()
    l_p.sort()
    l_height.sort()
    l_key, l_p, l_height

    it = iter(l_height)
    l = list(zip(l_key, l_p, it, it))

    l_output = []
    for k, p, a, b in l:
        o = {
            "name": k[2],
            "strata_delta": round(a[1] - b[1], 1),
            "p": p[2],
            #"p": map_p[p[2]],
        }
        l_output.append(o)


    return {
        "strata": strata,
        "list": l_output,
    }
