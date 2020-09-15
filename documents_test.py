import unittest
from documents import Documents


class TestDocuments(unittest.TestCase):
    """Test class that defines test cases for the Documents class behavior
    """

    def setUp(self):
        """Set up method to run befor before each test case"""
        self.new_documents = Documents("Facebook", "12345")

    def test_documents_instance(self):
        """Method that tests whether the new_documents have been instantiated correctly"""
        self.assertEqual(self.new_documents.account_name, "Facebook")
        self.assertEqual(self.new_documents.account_password, "12345")

    def test_save_documents(self):
        """Method that tests whether the new document created has been saved"""
        self.new_documents.save_documents()
        self.assertEqual(len(Documents.documents_list), 1)

    def test_save_multiple_documents(self):
        """Method that saves multiple documents to documents_list"""
        self.new_documents.save_documents()
        new_test_documents = Documents("Twitter", "56789")
        new_test_documents.save_documents()
        self.assertEqual(len(Documents.documents_list), 2)

    def tearDown(self):
        """Method that clears the documents_list after every test to ensure that there is no error"""
        Documents.documents_list = []

    def test_find_documents_by_name(self):
        """Test to check if we can find documents and display information"""
        self.new_documents.save_documents()
        new_test_documents = Documents("Twitter", "56789")
        new_test_documents.save_documents()

        found_document = Documents.find_by_name("Twitter")

        self.assertEqual(found_document.account_name, new_test_documents.account_name)

    def test_display_all_documents(self):
        """TestCase to test whether all contacts can be displayed"""
        self.assertEqual(Documents.display_documents(), Documents.documents_list)


if __name__ == '__main__':
    unittest.main()