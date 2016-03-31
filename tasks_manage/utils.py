def exclude_token(func):
    def wrapper(*args,**kwargs):
        l_args =list(args)
        request = l_args[1]
        if request.__class__.__name__ == 'WSGIRequest':
            request.DATA = dict(request.POST)
            del request.DATA['csrfmiddlewaretoken']
        return func(*l_args,**kwargs)
    return wrapper
