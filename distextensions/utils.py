

import fnmatch, os.path

def _fnmatch(name, patternList):
    for i in patternList:
        if fnmatch.fnmatch(name, i):
            return True
    return False


def _splitAll(path):
    parts = []
    h = path
    while 1:
        if not h:
            break
        h, t = os.path.split(h)
        parts.append(t)
    parts.reverse()
    return parts


def findPackages(path, dataExcludes=[]):
    """
        Recursively find all packages and data files rooted at path. Note that
        only data _directories_ and their contents are returned - non-Python
        files at module scope are not.

        Excludes is a list of fnmatch-compatible expressions for files that
        should not be included in the data directories return.
    """
    packages = []
    datadirs = []
    for root, dirs, files in os.walk(path, topdown=True):
        if "__init__.py" in files:
            p = _splitAll(root)
            packages.append(".".join(p))
        else:
            dirs[:] = []
            if packages:
                datadirs.append(root)

    # Now we recurse into the data directories
    package_data = {}
    for i in datadirs:
        if not _fnmatch(i, dataExcludes):
            parts = _splitAll(i)
            module = ".".join(parts[:-1])
            acc = []
            for root, dirs, files in os.walk(i, topdown=True):
                sub = _splitAll(root)[1:]
                for fname in files:
                    path = sub + [fname]
                    path = os.path.join(*path)
                    acc.append(path)
            package_data[module] = acc
    return packages, package_data


