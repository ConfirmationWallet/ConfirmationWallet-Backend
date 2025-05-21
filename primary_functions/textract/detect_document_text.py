import boto3
import base64
from constants.textract_constants import confidence_threshold


# The detect_document function just grabs the text as lines, and each word detected
def detect_document_text(request):
    # Initialize a session using Amazon Textract based on credentials put in through the CLI
    textractClient = boto3.client("textract")

    # Get the image from the form-data off the request
    image = request.files["image"]
    image_data = image.read()

    # this seems to not work when I put in the image in base64 even though that's what
    # the documentation asks for...
    # we'll probably end up pulling the image directly from s3 anyways...
    image_base64 = base64.b64encode(image_data).decode("utf-8")

    # Call Amazon Textract to detect text in the image
    response = textractClient.detect_document_text(Document={"Bytes": image_data})

    blocks = response["Blocks"]
    lines = []

    # Loop through the blocks and extract the text as well as the confidence and
    for block in blocks:
        if block["BlockType"] == "LINE":
            confidence = block["Confidence"]
            questionable = confidence < confidence_threshold
            lines.append(
                {
                    "text": block["Text"],
                    "confidence": confidence,
                    "questionable": questionable,
                }
            )
    response = {
        "lines": lines,
    }
    return response
