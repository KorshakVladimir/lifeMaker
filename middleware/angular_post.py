import json


class AngularPOSTMiddleware(object):

    def process_request(self, request):
        if request.method == 'POST':
            try:
                request.DATA = json.loads(next(iter(request.POST)))
            except Exception:
                pass
            finally:
                pass
