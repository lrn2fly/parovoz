# [START functions_ocr_setup]
import base64
import json
import os


from google.cloud import storage
from google.cloud import vision

vision_client = vision.ImageAnnotatorClient()
#translate_client = translate.Client()
#publisher = pubsub_v1.PublisherClient()
storage_client = storage.Client()

project_id = 'skyhacks-1'

# [END functions_ocr_setup]


# [START functions_ocr_detect]
def detect_text(bucket, filename):
    print('Looking for text in image {}'.format(filename))

    futures = []

    text_detection_response = vision_client.text_detection({
        'source': {'image_uri': 'gs://{}/{}'.format(bucket, filename)}
    })
    annotations = text_detection_response.text_annotations
    if len(annotations) > 0:
        text = annotations[0].description
    else:
        text = ''
    print('Extracted text {} from image ({} chars).'.format(text, len(text)))

# [END functions_ocr_detect]
detect_text('skyhack-1-vcm', '640f0973-5d9a-4b60-831c-547771acfa4b.jpg' )
