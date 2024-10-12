from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('index/', IndexView.as_view(), name='index'),
    path('courses/', CoursesList.as_view(), name='courses_list'),

    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),

    path('course/<int:pk>/', CourseDetail.as_view(), name='detail'),
    path('about', about, name='about'),
    path('create_course/', CreateCourse.as_view(), name='create'),
    path('course/<int:pk>/update/', UpdateCourse.as_view(), name='update'),
    path('course/<int:pk>/delete/', DeleteCourse.as_view(), name='delete'),

    path('comment/<int:course_id>/save/', save_comment, name='save_comment'),
    path('profile/<int:pk>/', profile_view, name='profile'),
    path('profile/<int:pk>/', profile_view, name='profile'),
    path('profile/<int:pk>/edit/', UpdateProfile.as_view(), name='edit'),
    path('user/<int:pk>/edit/', UpdateUser.as_view(), name='edit_user'),
    path('search/', SearchView.as_view(), name='search'),
    path('manage_enrollment/<int:course_id>/<str:action>/', manage_enrollment, name='manage_enrollment'),
]
