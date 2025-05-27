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
