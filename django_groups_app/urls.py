from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^signup', views.signup, name='signup'),
	url(r'^accounts/login/', views.user_login, name='user_login'),
	url(r'^user_logout', views.user_logout, name='user_logout'),
	url(r'^home', views.home, name='home'),
	url(r'^add_book', views.add_book, name='add_book'),
	url(r'^add-book-author', views.add_book_author, name='add_book_author'),
	url(r'^delete_book/(?P<id>\d+)/', views.delete_book, name='delete_book'),
	url(r'^edit_book/(?P<id>\d+)/', views.update_book, name='edit_book'),
	url(r'^change_password', views.change_password, name='change_password'),
	url(r'^group', views.group, name='group'),
	url(r'^add_employee', views.add_employee, name='add_employee'),
	url(r'^delete_employee/(?P<id>\d+)/', views.delete_employee, name='delete_employee'),
	url(r'^edit_employee/(?P<id>\d+)/', views.edit_employee, name='edit_employee'),
	url(r'^userdata', views.user_data, name='userdata'),
	url(r'^get_book_data', views.get_book_data, name='get_book_data'),
	url(r'^delete_book_data', views.delete_book_data, name='delete_book_data'),
	
]
