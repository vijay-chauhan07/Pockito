from django.test import TestCase
from django.contrib.auth.models import User
from todo.models import Todo
from django.utils import timezone
from datetime import timedelta
class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #set up non modified objects used by all test methods
        User.objects.create(username='@xyz', first_name='xyz', last_name='rickson', email='xyz@gmail.com', password='rex9875')

    def test_username(self):
        user = User.objects.get(id=1)
        field_label =user._meta.get_field('username').verbose_name
        self.assertEquals(field_label, 'username')

    def test_first_name(self):
        user = User.objects.get(id=1)
        field_label =user._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label, 'first name')

    def test_last_name(self):
        user = User.objects.get(id=1)
        field_label =user._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name') 


    def test_email(self):
        user = User.objects.get(id=1)
        field_label =user._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email address') 
    def test_password(self):

        user = User.objects.get(id=1)
        field_label =user._meta.get_field('password').verbose_name
        self.assertEquals(field_label, 'password') 




    

class TodoModelTest(TestCase):
    @classmethod
    #set up non modified objects used by all test methods

    def setUpTestData(cls):
        user = User.objects.create(username='vijay', password='vijay@9875')
        Todo.objects.create(author=user,
        title='Todo list', 
        description='This is an event', created=timezone.now(),
         
        updated=timezone.now(),
        deadline=timezone.now() + timedelta(minutes=30)
        )
     
    def test_author(self):
        obj=Todo.objects.get(id=1)
        self.assertEquals(obj.author.username, 'vijay') 


    def test_get_absolute_method(self):
        obj=Todo.objects.get(id=1)
        self.assertEquals(obj.get_absolute_url(),'/1/detail/'
        )
    


    def test__str__(self):
        obj=Todo.objects.get(id=1)
        self.assertEquals(obj.__str__(), 'Todo list')














