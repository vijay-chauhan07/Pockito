from django.urls import path


from .views import(Home,
 TodoListView,
 TodoDetailView, 
 TodoCreateView, 
 TodoUpdateView, 
 DeleteTodoView, 
 SignUpView, 
 ProfileView,
 ProfileUpdateView)
urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('list/', TodoListView.as_view(), name='list'),
    #path('user/list', UserList.as_view(), name='user_list'),
    #path('form/', GenerateRandomUserView.as_view(), name='form'),
    path('<int:pk>/detail/', TodoDetailView.as_view(), name='detail'),
    path('new/todo/list/', TodoCreateView.as_view(), name='create_todo_list'),
    path('<int:pk>/update/', TodoUpdateView.as_view(), name='update_todo_post'),
    path('<int:pk>/delete/', DeleteTodoView.as_view(), name='delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('<int:pk>/profile/', ProfileView.as_view(), name='profile'),
    path('<int:pk>/update-profile/', ProfileUpdateView.as_view(), name='update_profile'),


]
