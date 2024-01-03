from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (UserViewSet, RoleViewSet, DeveloperProfileViewSet, BoardViewSet,
                    ListViewSet, CardViewSet, CommentViewSet)

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("roles", RoleViewSet, basename="roles")
router.register("developerprofile", DeveloperProfileViewSet, basename="developerprofile")
router.register("board", BoardViewSet, basename="board")
router.register("list", ListViewSet, basename="list")
router.register("card", CardViewSet, basename="card")
router.register("comment", CommentViewSet, basename="comment")
urlpatterns = router.urls
