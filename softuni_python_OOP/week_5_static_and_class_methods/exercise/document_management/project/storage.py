from typing import List

from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:

    def __init__(self):
        self.categories: List = []
        self.topics: List = []
        self.documents: List = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        try:
            category = next(filter(lambda x: x.id == category_id, self.categories))
            category.edit(new_name)
        except StopIteration:
            return

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        try:
            topic = next(filter(lambda x: x.id == topic_id, self.topics))
            topic.edit(new_topic, new_storage_folder)
        except StopIteration:
            return

    def edit_document(self, document_id: int, new_file_name: str):
        try:
            document = next(filter(lambda x: x.id == document_id, self.documents))
            document.edit(new_file_name)
        except StopIteration:
            return

    def delete_category(self, category_id):
        try:
            category = next(filter(lambda x: x.id == category_id, self.categories))
            self.categories.remove(category)
        except StopIteration:
            return

    def delete_topic(self, topic_id):
        try:
            topic = next(filter(lambda x: x.id == topic_id, self.topics))
            self.topics.remove(topic)
        except StopIteration:
            return

    def delete_document(self, document_id):
        try:
            document = next(filter(lambda x: x.id == document_id, self.documents))
            self.documents.remove(document)
        except StopIteration:
            return

    def get_document(self, document_id):
        try:
            document = next(filter(lambda x: x.id == document_id, self.documents))
            return document
        except StopIteration:
            return

    def __repr__(self):
        result = '\n'.join(str(document) for document in self.documents)
        return result
