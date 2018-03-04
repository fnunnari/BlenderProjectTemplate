# BlenderProjectSkeleton - Scripts and guidelines to manage multiple Blender projects on the same machine.
# Copyright (C) 2018  Fabrizio Nunnari
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#    
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

def rreload(module):
    """
    Recursive reload of the specified module and (recursively) the used ones.
    Mandatory! Every submodule must have an __init__.py file
    Usage:
        import mymodule
        rreload(mymodule)

    :param module: the module to load (the module itself, not a string)
    :return: nothing
    """

    import os.path
    import sys

    def rreload_deep_scan(module, rootpath, mdict=None):
        from types import ModuleType
        from importlib import reload

        if mdict is None:
            mdict = {}

        if module not in mdict:
            # modules reloaded from this module
            mdict[module] = []
        # print("RReloading " + str(module))
        reload(module)
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            # print ("for attr "+attribute_name)
            if type(attribute) is ModuleType:
                # print ("typeok")
                if attribute not in mdict[module]:
                    # print ("not int mdict")
                    if attribute.__name__ not in sys.builtin_module_names:
                        # print ("not a builtin")
                        # If the submodule is a python file, it will have a __file__ attribute
                        if not hasattr(attribute, '__file__'):
                            raise BaseException("Could not find attribute __file__ for module '"+str(attribute)+"'. Maybe a missing __init__.py file?")

                        attribute_path = os.path.dirname(attribute.__file__)

                        if attribute_path.startswith(rootpath):
                            # print ("in path")
                            mdict[module].append(attribute)
                            rreload_deep_scan(attribute, rootpath, mdict)

    rreload_deep_scan(module, rootpath=os.path.dirname(module.__file__))


# This is an example. Substitute with the name of your addon module.
import mymodule
rreload(mymodule)
