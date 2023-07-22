import os

from channels.routing import ProtocolTypeRouter,URLRouter
from django.core.asgi import get_asgi_application
# import app.router
import app1.router
import app2.router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket':URLRouter(app2.router.websocket_urlpatterns)
})