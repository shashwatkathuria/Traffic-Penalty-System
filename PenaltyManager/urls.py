from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("register", views.register, name = "register"),
    path("login", views.loginUser, name = "login"),
    path("logout", views.logoutUser, name = "logout"),
    path("summary", views.summary, name = "summary"),
    path("contactus", views.contactus, name = "contactus"),
    path("getpenalties/<str:RFID>", views.getPenalties, name = "getPenalties"),
    path("submitpenalty", views.submitPenalty, name = "submitPenalty"),
    path("paypenalty", views.payPenalty, name = "payPenalty"),
]
