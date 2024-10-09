import os
import requests

def esigndocument(source_path, working_path):
    """
    Signs a document by sending it to a remote API and saves the signed document.

    :param source_path: str, path to the document to be signed
    :param working_path: str, path where the signed document will be saved
    """
    # Replace with your actual API endpoint
   # api_url = "http://127.0.0.1:8000/api/documents/post_document/sign/ "  # Update with your API URL

    # Check if the source document exists
    if not os.path.exists(source_path):
        print(f"Error: The source document at '{source_path}' does not exist.")
        return
    else
       print("The path exists" + source_path)

    if not os.path.exists(working_path):
        print(f"Error: The working document at '{working_path}' does not exist.")
        return
    else
       print("The working path exists" + working_path)

if __name__ == "__main__":
    # Set the paths for the source document and the output signed document
    source_document_path = os.environ.get('DOCUMENT_SOURCE_PATH')  # Replace with actual path
    working_document_path = os.environ.get('DOCUMENT_WORKING_PATH')  # Replace with actual path
    esigndocument(source_document_path, working_document_path)
