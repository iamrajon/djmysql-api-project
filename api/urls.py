from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CoursesViewSet, StudentViewSet


# creating instance of router
router = DefaultRouter()
router.register(r'courses', CoursesViewSet )
router.register(r'student', StudentViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', include("rest_framework.urls"))
]
