from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('',views.home,name='home'),
#     path('registerPage/',views.registerPage,name='register'),
#     path('loginPage/',views.loginPage,name='login'),
#     path('user/',views.userPage,name='userPage'), #userPage
    path('product/',views.fooditem,name='fooditem'),
    path('createfooditem/',views.createfooditem,name='createfooditem'),
    
#     path('logout/',views.logoutUser,name='logout'),
#     path('addFooditem/',views.addFooditem,name='addFooditem'),
#      path('reset_password/',
#          auth_views.PasswordResetView.as_view(),
#          name="reset_password"),
#     path('reset_password_sent/',
#          auth_views.PasswordResetDoneView.as_view(),
#          name="password_reset_done"),
#     path('reset/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(),
#          name="password_reset_confirm"),
#     path('reset_password_complete/',
#          auth_views.PasswordResetCompleteView.as_view(),
#          name="password_reset_complete"),
     path('',views.index),
     path('home',views.home),
     path('registerPage',views.registerPage),
     path('loginPage',views.loginPage),
     path('calorie',views.calorie),
     path('calorieview',views.calorieview),
 ]


    


 