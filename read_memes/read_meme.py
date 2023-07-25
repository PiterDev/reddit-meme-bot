import pytesseract
from PIL import Image
import string
import cv2
import numpy
import nltk
from nltk.corpus import words

# Download the English words corpus if not already downloaded
nltk.download('words')
nltk.download('punkt')

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

NUMBERS = "123456789"
ALLOWED_SPECIAL = ",.:-\n "


def prep_image(image) -> numpy.array:
    image = cv2.bilateralFilter(image, 5, 55, 60)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Grayscale
    _, image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return image


def remove_garbage(text: str) -> str:
    allowed = string.ascii_letters + NUMBERS + ALLOWED_SPECIAL
    optimized_text = "".join([char for char in text if char in allowed])
    return optimized_text


def is_readable(image) -> bool:
    """Check if can read image"""
    # TODO: Threshold?
    image = prep_image(image)
    white_pix = numpy.sum(image == 255)
    black_pix = numpy.sum(image == 0)
    return white_pix > black_pix


def is_gibberish(text):
    # Tokenize the text into words
    word_tokens = nltk.word_tokenize(text.lower())

    # Get the set of English words
    english_words = set(words.words())

    # Count the number of words in the text that are not in the English word set
    num_non_english_words = sum(word not in english_words for word in word_tokens)

    # Calculate the ratio of non-English words to total words
    gibberish_ratio = num_non_english_words / len(word_tokens)

    # Define a threshold to determine if the text is gibberish or not
    # You can adjust this threshold based on your specific needs
    gibberish_threshold = 0.4
    return gibberish_ratio >= gibberish_threshold


def read_image(img) -> str:
    img = prep_image(img)
    text = pytesseract.image_to_string(img, lang="eng")
    return remove_garbage(text)
