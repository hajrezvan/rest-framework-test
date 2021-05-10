from django.urls import path
from tp_book.views import GetAllDate, GetFavData, UpdateFavData, PostData, SearchData, DeleteData

urlpatterns = [
    path('get-all-data/', GetAllDate.as_view()),
    path('get-fav-data/', GetFavData.as_view()),
    path('update-fav-data/<int:primary_key>/', UpdateFavData.as_view()),
    path('post-fav-data/<int:primary_key>/', PostData.as_view()),
    path('search/', SearchData.as_view()),
    path('delete/<int:primary_key>/', DeleteData.as_view()),
]
