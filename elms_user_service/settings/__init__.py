from .base import *

if os.environ.get('ENV', 'local') == 'production':
    from .production import *
elif os.environ.get('ENV', 'local') == 'development':
    from .development import *
else:
    from .local import *
