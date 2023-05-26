import os
import io
from google.cloud import vision
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv("GOOGLE_VISION_API_KEY")


def get_text_info(image_path:str):
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

def remove_space(text:str):
    text_li = text.split('\n')
    
    correct = ""
    for text in text_li:
        if text[-1] == '-':
            correct += text[:-1]
        else:
            correct += text + " "
            
    return correct

def split_ocr(text:str):
    ret = []
    
    idx = 0
    for i, c in enumerate(text):
        if c == '.':
            for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if text[i+2] == x:
                    ret.append(text[idx:i+1])
                    idx = i+2
                    break
    ret.append(text[idx:len(text)])
    
    return ret

def preprocess_text(text_info:str, split_ratio:int=2):
    text = remove_space(text_info)
    ocr_li = split_ocr(text)
    
    remain = len(ocr_li) % split_ratio
    ocr_li_len = len(ocr_li)
    
    ret = []
    for i in range(0, ocr_li_len - remain, split_ratio):
        s = ""
        for j in range(i, i+split_ratio):
            s += ocr_li[j] + "\n"
        ret.append(s)
    
    s = ""
    for i in range(ocr_li_len - remain, ocr_li_len):
        s += ocr_li[i] + "\n"    
    ret.append(s)
    
    return ret

def get_ocr(image_path):
    text_info = get_text_info(image_path)
    text = remove_space(text_info)
    
    return text
    

if __name__ == '__main__':
    text = get_ocr('a.JPG')
    print(text)