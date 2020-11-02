from django.test import TestCase
from .models import Hood,Profile,Business
# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(name='patrick',neighborhood='ruiru',email_address="patode01@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)