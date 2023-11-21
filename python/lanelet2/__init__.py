from os.path import dirname
from pkgutil import iter_modules

# automatically import all files in this module
__all__ = [name for _, name, _ in iter_modules([dirname(__file__)])]

for module_name in __all__:
    from importlib import import_module

    module = import_module(__name__ + "." + module_name)
    if len(__all__) == 1:
        globals().update(module.__dict__)
    del module
