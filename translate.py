from googletrans import Translator

def translate_text(text, src_lang='auto', dest_lang='en'):
    """
    Translate text from source language to destination language.
https://github.com/hadi2479/PVG/tree/main
    :param text: Text to be translated
    :param src_lang: Source language (default is 'auto' for auto-detection)
    :param dest_lang: Destination language (default is 'en' for English)
    :return: Translated text
    """
    translator = Translator()
    try:
        translated = translator.translate(text, src=src_lang, dest=dest_lang)
        return translated.text
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    text_to_translate = input("Enter text to translate: ")
    source_language = input("Enter source language (default is 'auto'): ") or 'auto'
    destination_language = input("Enter destination language (default is 'en'): ") or 'en'
    
    translated_text = translate_text(text_to_translate, src_lang=source_language, dest_lang=destination_language)
    print(f"Translated text: {translated_text}")
