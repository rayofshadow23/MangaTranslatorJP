import os
from PIL import Image
import pytesseract
import openai

# Imposta la tua API key OpenAI qui
openai.api_key = "LA_TUA_API_KEY"

# Cartella delle immagini manga
folder_path = "manga_pages"

# File di output
output_file = "traduzioni_manga.txt"

def estrai_testo_giapponese(image_path):
    # Usa pytesseract con lingua giapponese (assicurati di aver installato il pacchetto tesseract-jpn)
    text = pytesseract.image_to_string(Image.open(image_path), lang='jpn')
    return text.strip()

def traduci_testo_giapponese_italiano(testo):
    prompt = (
        f"Sei un traduttore professionista di giapponese in italiano.\n"
        f"Traduci il testo giapponese qui sotto in italiano mantenendo il significato e lo stile:\n\n{testo}\n\nTraduzione:"
    )

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # oppure "gpt-3.5-turbo"
        messages=[
            {"role": "system", "content": "Sei un traduttore di giapponese in italiano."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=1000
    )

    traduzione = response['choices'][0]['message']['content'].strip()
    return traduzione

def main():
    immagini = sorted(os.listdir(folder_path))
    with open(output_file, "w", encoding="utf-8") as f_out:
        for img_name in immagini:
            path_img = os.path.join(folder_path, img_name)
            print(f"Elaboro: {img_name}")

            # Estrai testo giapponese
            testo_giapponese = estrai_testo_giapponese(path_img)
            if not testo_giapponese:
                print(f"Nessun testo estratto da {img_name}, salto.")
                continue

            # Traduci
            traduzione = traduci_testo_giapponese_italiano(testo_giapponese)

            # Scrivi output
            f_out.write(f"<{img_name}>\n")
            f_out.write(testo_giapponese + "\n")
            f_out.write(traduzione + "\n\n")

    print(f"Traduzioni completate e salvate in {output_file}")

if __name__ == "__main__":
    main()
