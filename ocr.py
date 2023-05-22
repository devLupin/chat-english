import os
import io
from google.cloud import vision
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("GOOGLE_VISION_API_KEY")


def get_text_info(image_path):
    """get text information

    Args:
        image_path (str): image abs path

    Returns:
        _type_: [symbol.text, symbol.bbox.vertices[0]]
    """
    client = vision.ImageAnnotatorClient()

    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.document_text_detection(image=image)
    document = response.full_text_annotation

    return document.text

def remove_space(text):
    text_li = text.split('\n')
    
    correct = ""
    for text in text_li:
        if text[-1] == '-':
            correct += text[:-1] + " "
        else:
            correct += text + " "
            
    return correct

def get_ocr(image_path):
    text_info = get_text_info(image_path)
    text = remove_space(text_info)
    
    return text
    

if __name__ == '__main__':
    text = get_ocr('a.JPG')
    print(text)