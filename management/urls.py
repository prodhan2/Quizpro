from django.urls import path
from . import views

urlpatterns = [
    path("", views.Manage.as_view(), name="manage"),
    path("results/", views.Results.as_view(), name="results"),
    path("upload_questions", views.UploadQuestion.as_view(), name="upload_question")
]
