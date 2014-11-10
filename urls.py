import views

#urls = [(r'^$', views.index), (r'hello/?$', views.hello), (r'hello/(.+)$', views.hello),]

def patterns(prefix, *args):
    pattern_list = []
    for t in args:
        if isinstance(t, (list, tuple)):
            t = url(prefix=prefix, *t)
        elif isinstance(t, RegexURLPattern):
            t.add_prefix(prefix)
        pattern_list.append(t)
    return pattern_list

def url(regex, view, kwargs=None, name=None, prefix=''):
    if isinstance(view, (list, tuple)):
        # For include(...) processing.
        urlconf_module, app_name, namespace = view
        return RegexURLResolver(regex, urlconf_module, kwargs, app_name=app_name, namespace=namespace)
    else:
        if isinstance(view, six.string_types):
            warnings.warn(
                'Support for string view arguments to url() is deprecated and '
                'will be removed in Django 2.0 (got %s). Pass the callable '
                'instead.' % view,
                RemovedInDjango20Warning, stacklevel=2
            )
            if not view:
                raise ImproperlyConfigured('Empty URL pattern view name not 
permitted (for pattern %r)' % regex)
            if prefix:
                view = prefix + '.' + view
        return RegexURLPattern(regex, view, kwargs, name)

urlpatterns = patterns('', 
    url(r'^$$', 'views.index'), 
    url(r'hello/?$', 'views.hello'), 
    url(r'hello/(.+)$', 'views.hello'),
    )
