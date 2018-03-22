from pyramid.config import Configurator
from pyramid_zodbconn import get_connection
from .models import appmaker
from .resources import bootstrap
from pyramid.renderers import JSON


def root_factory(request):
    conn = get_connection(request)
    return appmaker(conn.root())


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=bootstrap, settings=settings)
    config.include('pyramid_chameleon')
    json_renderer = JSON()
    config.add_renderer('json', json_renderer)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.scan()
    return config.make_wsgi_app()
