import boto3
import base64
from constants.textract_constants import confidence_threshold


# analyze_document not only grabs all the text, but also does some "analysis"
# on the structure of the text and provides querying abilities, as well as a few other things
def analyze_document(request):
    # Initialize a session using Amazon Textract based on credentials put in through the CLI
    textractClient = boto3.client("textract")

    # Get the image from the form-data off the request
    image = request.files["image"]
    image_data = image.read()

    # this seems to not work when I put in the image in base64 even though that's what
    # the documentation asks for...
    # we'll probably end up pulling the image directly from s3 anyways...
    image_base64 = base64.b64encode(image_data).decode("utf-8")

    response = textractClient.analyze_document(
        Document={"Bytes": image_data}, FeatureTypes=["TABLES", "FORMS", "LAYOUT"]
    )

    blocks = response["Blocks"]

    # lines and words come first in the blocks, so we can add each line to this dictionary
    # and then use the relationships to get the lines for each layout
    line_ids = {}

    # arrays to hold different block types
    LINES = []
    LAYOUTS = []
    TABLES = []
    FORMS = []

    # loop through the blocks and put them into the approprate list
    for block in blocks:
        block_text = block.get("Text", "")
        BlockType = block.get("BlockType", "")
        confidence = block.get("Confidence", 0)
        questionable = confidence < confidence_threshold

        # if its a line, we'll store it and add it to the dictionary for when we see layout blocks
        if BlockType == "LINE":
            line_ids[block["Id"]] = block_text

            LINES.append(
                {
                    "text": block_text,
                    "confidence": confidence,
                    "questionable": questionable,
                }
            )

        # right now I don't have test data that has tables, or forms
        elif BlockType == "TABLE":
            TABLES.append(block)
        elif BlockType == "FORM":
            FORMS.append(block)

        # if its a layout block, we'll check to see if it has relationships (children lines)
        # then add the children lines to a list
        elif BlockType.startswith("LAYOUT_"):
            lines = []
            Relationships = block.get("Relationships", [])
            if not Relationships:
                continue

            for line_id in block["Relationships"][0]["Ids"]:
                lines.append(line_ids.get(line_id, ""))

            LAYOUTS.append(
                {
                    "layout_type": BlockType,
                    "lines": lines,
                    "confidence": confidence,
                    "questionable": questionable,
                }
            )
    return {
        "lines": LINES,
        "tables": TABLES,
        "forms": FORMS,
        "layouts": LAYOUTS,
    }
