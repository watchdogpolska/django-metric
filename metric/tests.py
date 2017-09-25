import re
from django.core.management import call_command
from django.core.urlresolvers import reverse
from django.test import TestCase


from .factories import ItemFactory, ValueFactory
from django.utils.six import StringIO


class ValueBrowseListViewTestCase(TestCase):
    def setUp(self):
        self.obj = ItemFactory()
        self.values = ValueFactory.create_batch(size=10, item=self.obj)
        self.url = reverse('metric:item_detail', kwargs={'key': self.obj.key,
                                                         'month': str(self.values[0].time.month),
                                                         'year': str(self.values[0].time.year)})

    def test_valid_status_code_for_detail_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200, "Invalid status code on '{}'".format(self.url))

    def test_output_contains_values(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.values[0].value)

    def test_output_contains_description(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.obj.description)


class CSVValueListViewTestCase(TestCase):
    def setUp(self):
        self.obj = ItemFactory()
        self.values = ValueFactory.create_batch(size=10, item=self.obj)
        self.url = reverse('metric:item_detail_csv', kwargs={'key': self.obj.key,
                                                            'month': self.values[0].time.month,
                                                            'year': self.values[0].time.year,
                                                            })

    def test_valid_status_code_for_detail_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200, "Invalid status code on '{}'".format(self.url))

    def test_output_contains_values(self):
        response = self.client.get(self.url)
        self.assertContains(response, str(self.values[0].value))

    def test_output_contains_item_name(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.obj.name)


class JSONValueListViewTestCase(TestCase):
    def setUp(self):
        self.obj = ItemFactory()
        self.values = ValueFactory.create_batch(size=10, item=self.obj)
        self.url = reverse('metric:item_detail_json', kwargs={'key': self.obj.key,
                                                              'month': self.values[0].time.month,
                                                              'year': self.values[0].time.year})

    def test_valid_status_code_for_detail_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200, "Invalid status code on '{}'".format(self.url))

    def test_output_contains_values(self):
        response = self.client.get(self.url).json()
        sorted(self.values, key=lambda x: x.time)
        self.assertEqual(response['values'][0]['value'], self.values[0].value)

    def test_output_contains_item_name(self):
        response = self.client.get(self.url).json()
        self.assertEqual(response['item']['name'], self.obj.name)


class TestManagementCommand(TestCase):
    def test_command_no_raises_exception(self):
        call_command('update_metric')

    def test_command_outputs(self):
        out = StringIO()
        call_command('update_metric', stdout=out)
        output = out.getvalue()
        self.assertTrue(re.search("Registered .* new items", output))
        self.assertTrue(re.search("Registered .* values.", output))
