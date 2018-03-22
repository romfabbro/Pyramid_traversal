from pyramid.view import view_config, view_defaults
# from .models import MyModel
from .resources import Child1, ChildI, Child2

# @view_config(context=MyModel, renderer='templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'ZOB_test_traversal'}

class TutorialViews:
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(renderer='json')
    def home(self):
        page_title = 'Quick Tutorial: Home'
        return dict(page_title=page_title)

    @view_config(name='hello', renderer='json')
    def hello(self):
        page_title = 'Quick Tutorial: Hello'
        return dict(page_title=page_title)


@view_defaults(context=ChildI)
class ChildView:
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(request_method='GET', renderer='json')
    def home(self):
        page_title = self.context.__name__+': home'
        print(self.context.__name__)
        return dict(page_title=page_title)

    @view_config(name='hello', renderer='json')
    def hello(self):
        page_title = self.context.__name__+': Hello'
        return dict(page_title=page_title)

    @view_config(name='form',request_method=['POST', 'GET'], renderer='json')
    def form(self):

        return dict(form=self.context.getForm())


@view_config(context=Child2, name='toto', renderer='json')
def toto(context, request):
    return context.toto()

@view_config(context=Child1, name='stations', renderer='json')
def sta(context, request):
    return 'confi station actions'