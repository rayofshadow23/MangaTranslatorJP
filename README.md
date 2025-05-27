# MangaTranslatorJP

MangaTranslatorJP è uno strumento Python che estrae automaticamente il testo giapponese dalle pagine di un manga e lo traduce in italiano utilizzando le API di OpenAI.  
Perfetto per chi vuole tradurre manga digitalizzati in modo rapido e con risultati di qualità, mantenendo il testo originale e la traduzione affiancata.

---

## Funzionalità

- Estrazione del testo giapponese dalle immagini manga tramite OCR (Tesseract OCR con lingua giapponese)
- Traduzione del testo giapponese in italiano con il modello GPT-4o-mini di OpenAI
- Output testuale organizzato per pagina con testo originale e traduzione

---

## Requisiti

- Python 3.7+
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) con supporto alla lingua giapponese (`tesseract-ocr-jpn`)
- API Key OpenAI (con accesso al modello GPT-4o-mini o GPT-3.5-turbo)

---

## Installazione

1. Installa Tesseract OCR con supporto giapponese.

   Su Ubuntu/Debian:
   ```bash
   sudo apt update
   sudo apt install tesseract-ocr tesseract-ocr-jpn
2. Installa le librerie Python necessarie:

   ```bash
   pip install openai pillow pytesseract

3. Clona questo repository
   ```bash
   git clone https://github.com/tuo-username/MangaTranslatorJP.git
   cd MangaTranslatorJP

4. Inserisci la tua API key OpenAI nel file translator.py (oppure usa variabili d’ambiente).
5. Prepara la cartella manga_pages con le immagini delle pagine manga (formati supportati: PNG, JPG).

## Uso
Esegui lo script:
```bash
python translator.py

Il programma elaborerà tutte le immagini in manga_pages/ e genererà un file traduzioni_manga.txt con il testo originale e la traduzione italiana per ogni pagina.


