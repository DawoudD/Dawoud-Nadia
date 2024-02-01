from lib.make_snippet import *

def test_make_snippet():
    snippet = make_snippet('i love the fresh smell of cofee in the morning')
    assert snippet == 'i love the fresh smell ...'