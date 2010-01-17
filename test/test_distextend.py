import libpry
from distextend import *
from distextend import _fnmatch, _splitAll


class uFindPackages(libpry.AutoTree):
    def test_testmodule(self):
        p, d = findPackages("testmodule", dataExclude=["*.exclude"])
        assert p == ["testmodule", "testmodule.subpackage"]
        expected = {
            "testmodule": [
                                'pkgdata/falsemod/__init__.py',
                                'pkgdata/foo',
                                'pkgdata2/one/one',
                                'pkgdata2/two/two',
                            ]
            }
        for i in d.keys():
            d[i].sort()
        assert d == expected

    def test_emptymod(self):
        p, d = findPackages("testmodule/pkgdata", dataExclude=["*.exclude"])
        assert not p


class u_fnmatch(libpry.AutoTree):
    def test_match(self):
        assert not _fnmatch("foo", [])
        assert _fnmatch("foo", ["*oo"])
        assert _fnmatch("foo", ["bar", "*oo"])
        assert not _fnmatch("mong", ["bar", "*oo"])


class u_splitAll(libpry.AutoTree):
    def _roundtrip(self, *lst):
        j = os.path.join(*lst)
        assert _splitAll(j) == list(lst)
        
    def test_splitAll(self):
        self._roundtrip("foo", "bar", "voing")
        self._roundtrip("foo", "bar")
        self._roundtrip("foo")


tests = [
    uFindPackages(),
    u_splitAll(),
    u_fnmatch(),



]
