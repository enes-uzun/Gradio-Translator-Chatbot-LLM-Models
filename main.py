from gradio_client import Client
from deep_translator import GoogleTranslator

def translate(text, target_language):
    translation = GoogleTranslator(source='auto', target=target_language).translate(text)
    return translation

#URL of Gradio app
url = "https://hysts-mistral-7b.hf.space/--replicas/ezo3j/"


client = Client(url)

while True:
    # Kullanıcıdan mesaj al
    user_input = input("Mesajınızı girin (çıkmak için 'çıkış' yazın): ")
    if user_input.lower() == "çıkış":
        break

    # Mesajı İngilizce'ye çevir
    translated_input = translate(user_input, "en")

    # Çevrilen mesajı Gradio uygulamasına gönder ve sonucu al
    result = client.predict(
        translated_input,
        511,
        0.1,
        0.05,
        1,
        1,
        api_name="/chat"
    )

    # Gradio'dan gelen yanıtı Türkçe'ye çevir
    translated_response = translate(result, "tr")

    # Çevrilen yanıtı yazdır
    print("Yanıt:", translated_response)

print("Sohbet sonlandırıldı.")
