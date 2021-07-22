from django.urls import path

import user_api.views as views

# CRUD

urlpatterns = [
    path('accounts/',  views.UsersView.as_view()),
    path('accounts/<int:pk>/',  views.UserView.as_view()),
    path('accounts/create', views.UserCreate.as_view()),
    path('accounts/update/<int:pk>/', views.UserUpdate.as_view()),
    path('accounts/delete/<int:pk>/', views.UserDelete.as_view()),

    path('custom_accounts/',  views.CustomUsersView.as_view(), name='get_users'),
    path('custom_accounts/<int:pk>/',  views.CustomUserView.as_view(), name='get_user'),
    path('custom_accounts/create', views.CustomUserCreate.as_view(), name='create_user'),
    path('custom_accounts/update/<int:pk>/', views.CustomUserUpdate.as_view(), name='update_user'),
    path('custom_accounts/delete/<int:pk>/', views.CustomUserDelete.as_view(), name='delete_user')
]
