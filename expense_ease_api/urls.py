from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import SignUpAPIView, TransactionViewSet

router = SimpleRouter()
router.register("transactions", TransactionViewSet)

urlpatterns = [path("signup/", SignUpAPIView.as_view())]
urlpatterns += router.urls
