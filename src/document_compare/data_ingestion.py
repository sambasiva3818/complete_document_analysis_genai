import sys
from pathlib import Path
import fitz
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException


class DocumentCompare:
    """
    Compares two documents and extracts differences.
    Automatically logs all actions and supports session-based organization.
    """
    def __init__(self):
        pass

    def delete_existing_files(self):
        """        Deletes existing files in the specified directory.
        """
        pass
    
    def save_uploaded_filke(self):
        """        Saves the uploaded file to a specified directory.
        """
        pass
    
    def read_pdf(self):
        """        Reads a PDF file and extracts text from each page.
        """
        pass