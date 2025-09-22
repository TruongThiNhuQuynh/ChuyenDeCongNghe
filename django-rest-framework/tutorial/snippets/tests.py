from django.test import TestCase
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

class SnippetModelTest(TestCase):
    def setUp(self):
        self.snippet = Snippet.objects.create(
            code='print("Hello, world!")',
            title='Hello World',
            linenos=False,
            language='python',
            style='friendly'
        )

    def test_snippet_creation(self):
        self.assertEqual(self.snippet.code, 'print("Hello, world!")')
        self.assertEqual(self.snippet.title, 'Hello World')
        self.assertFalse(self.snippet.linenos)
        self.assertEqual(self.snippet.language, 'python')
        self.assertEqual(self.snippet.style, 'friendly')

class SnippetSerializerTest(TestCase):
    def setUp(self):
        self.snippet = Snippet.objects.create(
            code='print("Hello, world!")',
            title='Hello World',
            linenos=False,
            language='python',
            style='friendly'
        )
        self.serializer = SnippetSerializer(instance=self.snippet)

    def test_snippet_serializer(self):
        data = self.serializer.data
        self.assertEqual(data['code'], 'print("Hello, world!")')
        self.assertEqual(data['title'], 'Hello World')
        self.assertFalse(data['linenos'])
        self.assertEqual(data['language'], 'python')
        self.assertEqual(data['style'], 'friendly')