from glob import iglob
from os import path


def get_extensions():
    extensions_list = set()
    for filepath in iglob(path.join(path.dirname(__file__), "*.py")):
        filename = path.basename(filepath)
        if not filename.startswith("_"):
            extensions_list.add(path.split(path.dirname(__file__))[1] + "." + filename[:-3])
    return extensions_list
