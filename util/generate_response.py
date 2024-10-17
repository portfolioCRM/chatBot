from googletrans import Translator
from typing import List, Dict, Optional, Any

translator = Translator()

def translate_text(text: Optional[str], target_language: str = "en") -> str:
    """
    Translate a given text to the specified target language.

    Args:
        text (Optional[str]): The text to translate.
        target_language (str): The language code to translate the text into.

    Returns:
        str: The translated text.
    """
    if not text:
        return text
    try:
        translated = translator.translate(text, dest=target_language).text
        return translated
    except Exception as e:
        return text

def translate_field_in_array(data_array: List[Dict[str, Any]], field_name: str, target_language: str = "en") -> List[Dict[str, Any]]:
    """
    Translate a specific field in an array of dictionaries.

    Args:
        data_array (List[Dict[str, Any]]): The array of dictionaries to process.
        field_name (str): The field name to translate.
        target_language (str): The language code to translate the text into.

    Returns:
        List[Dict[str, Any]]: The array of dictionaries with the translated field.
    """
    return list(map(lambda item: {
        **item,
        field_name: translate_text(item.get(field_name), target_language)
    }, data_array))

def translate_field_in_dict(data_dict: Dict[str, Any], field_name: str, target_language: str = "en") -> Dict[str, Any]:
    """
    Translate a specific field in a dictionary.

    Args:
        data_dict (Dict[str, Any]): The dictionary to process.
        field_name (str): The field name to translate.
        target_language (str): The language code to translate the text into.

    Returns:
        Dict[str, Any]: The dictionary with the translated field.
    """
    if field_name in data_dict:
        data_dict[field_name] = translate_text(data_dict[field_name], target_language)
    return data_dict
