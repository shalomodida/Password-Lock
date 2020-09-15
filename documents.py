class Documents:
    """Create class for documents"""

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    documents_list = []

    def save_documents(self):
        """Method that saves documents objects into documents_list"""
        self.documents_list.append(self)

    def delete_documents(self):
        """Method which deletes a particular documents"""
        Documents.documents_list.remove(self)

    @classmethod
    def find_by_name(cls, account_name):
        """Method that takes in a name and returns a document that matches that particular name
        Args:
            name: account_name that has a password
        Returns:
            The account_name and it's corresponding PassWord
        """

        for documents in cls.documents_list:
            if document.account_name == account_name:
                return document

    @classmethod
    def document_exists(cls, name):
        """Method to check whether a documents exists
        Args:
        name: name of account to search whether it exists
        boolean: True or False depending if the contatc exists
        """

        for document in cls.documents_list:
            if document.account_name == name:
                return True
        return False

    @classmethod
    def display_documents(cls):
        """Method which displays all current documents"""
        return cls.documents_list