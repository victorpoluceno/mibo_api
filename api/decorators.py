from functools import wraps

from flask import Response, request

from werkzeug.contrib.cache import SimpleCache
cache = SimpleCache() #FIXME: use a config option to choose this or memcache

import requests


def jsonp_proxy(url):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            f(*args, **kwargs)
            params = request.args.copy()
            callback = params.get('callback', 'callback')
            del params['callback'] 
            response = requests.get(url, params=params)
            if not response.status_code in [200, 304]:
                # return the origin content and status code
                return Response(response.content, response.status_code, 
                        mimetype=response.headers['content-type'])

            # put content inside a callback
            content = "%s(%s);" % (callback, response.content)
            return Response(content, mimetype='application/javascript')
        return decorated_function
    return decorator


def cached(timeout=5 * 60, key='view/%s'):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            cache_key = key % request.path + request.query_string
            rv = cache.get(cache_key)
            if rv is not None:
                return rv
            rv = f(*args, **kwargs)
            cache.set(cache_key, rv, timeout=timeout)
            return rv
        return decorated_function
    return decorator

