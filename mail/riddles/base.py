from abc import ABC, abstractmethod

from docx.document import Document

class RiddleBase(ABC):

    @ abstractmethod
    def get_document(self, message: str) -> Document:
        ...

