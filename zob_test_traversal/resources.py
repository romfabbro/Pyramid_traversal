from zope.interface import implements
from zope.interface import Interface, implementer

class Root(dict):
    __name__ = ''
    __parent__ = None

    def __init__(self, title):
        self.title = title

    def __getitem__(self, ref):
        if ref == 'child1':
            return Child1(ref, self)
        if ref == 'child2':
            return Child2(ref, self)
        else:
            raise KeyError


def bootstrap(request):
    root = Root('My Site')

    return root


class ChildI(Interface):
    pass


@implementer(ChildI)
class Child(object):
    def __init__(self, ref, parent):
        # print('init child1 : ', ref, parent)
        self.__name__ = ref
        self.__parent__ = parent

    def getForm(self):
        return 'form '+self.__name__


class Child1(Child):

    def __getitem__(self, ref):
        if ref == 'stations':
            return Child1(ref, self)
        if ref == 'individus':
            return Child2(ref, self)
        else:
            raise KeyError


class Child2(Child):
    def toto(self):
        return 'toto'


