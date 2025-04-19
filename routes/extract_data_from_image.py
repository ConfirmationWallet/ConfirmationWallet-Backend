from openAI_functions.interpret_text import interpret_text
from textract_functions.detect_document_text import detect_document_text


def extract_data_from_image(request):
    extracted_text = detect_document_text(request)
    interpreted_text = interpret_text(extracted_text)
    return interpreted_text
