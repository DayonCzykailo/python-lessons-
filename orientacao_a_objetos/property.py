class Foo:
    def __init__(self, anything = False):
        self._anything = anything

    @property
    def anything(self):
        return "true FOO" if self._anything  else "false FOO"

    
foo = Foo(True)
print(foo.anything)