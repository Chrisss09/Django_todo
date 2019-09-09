from django.test import TestCase
from .forms import ItemForm

class TestToDoItemForm(TestCase):

    def test_create_item_with_name(self):
        form = ItemForm({'name': 'Create Tests'})
        self.assertTrue(form.is_valid())

    def test_correct_message_for_missing_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], [u'This field is required.'])