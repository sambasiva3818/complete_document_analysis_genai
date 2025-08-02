import sys
from dotenv import load_dotenv
import pandas as pd
from logger.custom_logger import CustomLogger
from exception.custom_exception import DocumentPortalException
from model.models import *
from prompt.prompt_library import PROPMT_REGISTRY
from utils.model_loader import ModelLoader
from langchain_core.output_parsers import JsonOutputParser
from langchain.output_parsers import OutputFixingParser


class DocumentCompareLLM:
    """
    Compares two documents and extracts differences.
    Automatically logs all actions and supports session-based organization.
    """
    def __init__(self):
        pass
    
    def compare_documents(self):
        """        Compares two documents and extracts differences.
        """
        pass
    
    def _format_response(self, response: dict) -> pd.DataFrame:
        """
        Formats the response from the LLM into a DataFrame.
        """
        pass
    
