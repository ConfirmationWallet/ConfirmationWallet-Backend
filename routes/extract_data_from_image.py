from primary_functions.openAI.interpret_text import interpret_text
from primary_functions.textract.detect_document_text import (
    detect_document_text,
)


def extract_data_from_image(request):
    extracted_text = detect_document_text(request)
    interpreted_text = interpret_text(extracted_text)
    return interpreted_text
