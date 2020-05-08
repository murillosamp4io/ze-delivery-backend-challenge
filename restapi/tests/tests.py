from django.test import TestCase
from django.urls import reverse, resolve

from partner.geolocation.viewsets import GeolocationViewSet


class TransactionsUrlsTestCase(TestCase):

    def test_list_url(self):
        resolver = self.resolve_by_name('transactions')

        self.assertEqual(resolver.func.cls, GeolocationViewSet)

    def test_retrieve_url(self):
        resolver = self.resolve_by_name('transaction', pk=1)

        self.assertEqual(resolver.func.cls, GeolocationViewSet)

    def test_actions(self):
        resolver = self.resolve_by_name('transactions')

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('list', resolver.func.actions['get'])

    def test_retrieve_action(self):
        resolver = self.resolve_by_name('transaction', pk=1)

        self.assertIn('get', resolver.func.actions)
        self.assertEqual('retrieve', resolver.func.actions['get'])

    def test_list_url_only_allows_get_and_post(self):
        resolver = self.resolve_by_name('transactions')

        self.assert_has_actions(['get', 'post'], resolver.func.actions)

    def test_single_url_allows_all_methods_except_post(self):
        resolver = self.resolve_by_name('transaction', pk=1)

        self.assert_has_actions(['get'], resolver.func.actions)

    def assert_has_actions(self, allowed, actions):
        self.assertEqual(len(allowed), len(actions))

        for allows in allowed:
            self.assertIn(allows, actions)

    def test_get_all_partners(self):
        response = self.client.get('/partner/')
        self.assertEqual(response.status_code, 200)

    def resolve_by_name(self, name, **kwargs):
        url = reverse(name, kwargs=kwargs)
        return resolve(url)
