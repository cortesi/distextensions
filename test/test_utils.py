import pylid
from distextensions.utils import *
from distextensions.utils import _fnmatch, _splitAll


class testFindPackages(pylid.TestCase):
    def test_testmodule(self):
        p, d = findPackages("testmodule", dataExclude=["*.exclude"])
        assert p == ["testmodule", "testmodule.subpackage"]
        self.assertEqual(
            d,
            {
            "testmodule": [
                                'pkgdata/foo', 'pkgdata/falsemod/__init__.py'
                            ]
            }
        )

    def test_emptymod(self):
        p, d = findPackages("testmodule/pkgdata", dataExclude=["*.exclude"])
        assert not p


class u_fnmatch(pylid.TestCase):
    def test_match(self):
        assert not _fnmatch("foo", [])
        assert _fnmatch("foo", ["*oo"])
        assert _fnmatch("foo", ["bar", "*oo"])
        assert not _fnmatch("mong", ["bar", "*oo"])


class u_splitAll(pylid.TestCase):
    def _roundtrip(self, *lst):
        j = os.path.join(*lst)
        self.assertEqual(_splitAll(j), list(lst))
        
    def test_splitAll(self):
        self._roundtrip("foo", "bar", "voing")
        self._roundtrip("foo", "bar")
        self._roundtrip("foo")
