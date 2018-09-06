from django.urls import path
from .views import PagesListView, PagesDetailView, PageCreate, PageUpdate, PageDelete

pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PagesDetailView.as_view(), name='page'),
    path('create/',PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name="update"),
    path('delete/<int:pk>/', PageDelete.as_view(), name="delete"),
], 'pages')