"""The pilot app's only function: it answers every request with a short greeting."""

import json


def handler(event, context):
    """Return a fixed JSON greeting. The code does not matter; the template is what is priced."""
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": "hello from the cost-insights pilot"}),
    }
