from django.urls import path
from user.views import UserViewSet, LoginUserView, ManageUserView

urlpatterns = [
    path("register/", UserViewSet.as_view(), name="create"),
    path("login/", LoginUserView.as_view(), name="login"),
    path("me/", ManageUserView.as_view(), name="manage"),

]

app_name = "user"
