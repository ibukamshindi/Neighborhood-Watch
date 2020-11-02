from django.test import TestCase
from .models import Hood,Profile,Business
# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        self.profile=Profile(name='patrick',email_address="patode01@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_method(self):
        self.profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.business=Business(business_name='Joes Plumbing',email="joeplum@gmail.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

    def test_create_method(self):
        self.business.create_business()
        business=Business.objects.all()
        self.assertTrue(len(business)>0)

    def test_delete_method(self):
        self.business.create_business()
        business = Business.objects.all()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business)==0)      