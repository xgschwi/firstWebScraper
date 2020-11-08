# Sample use of pytest
# Use commands: python -m pytest/ pytest / py.test 
# (include specific filename afterwards if desired)
# Use numerical terms "1" / "one" following method declaration for tests to be run

import pytest

class TestClass:

    def test1(self):
        print("This is the start of some tests")

    def test2(self):
        x = "this"
        assert "h" in x
