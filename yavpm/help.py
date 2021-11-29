def strip_indent(s):
    result = []
    min_indent = None
    lines = tuple(s.split("\n"))
    for line in lines:
        indent = len(line) - len(line.lstrip())
        if min_indent is None or min_indent > indent:
            min_indent = indent
    for line in lines:
        if line.strip().empty():
            continue
        result.append(line[min_indent:])
    return result


def get():
    return strip_indent(
        """
        Usage: yavpm [COMMAND] [OPTIONS]...
        """
    )
