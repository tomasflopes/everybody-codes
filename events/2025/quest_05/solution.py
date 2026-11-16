def parse_input(data):
    return list(map(int, data.split(":")[1].split(",")))

def part_1(data):
    data = parse_input(data)
    res = []
    l, r = 0, 0
    res.append(data[0])

    for n in data[1:]:
      print(res, n, l, r)
      if n < res[-1] and l <= 0:
        l += 1
      elif n > res[-1] and r <= 0:
        r += 1
      else:
        res.append(n)
        l -= 1
        r -= 1

    return "".join(map(str, res))
    #454432136364633153

def part_2(data):
    data = parse_input(data)
    return data

def part_3(data):
    data = parse_input(data)
    return data
      