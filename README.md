# **Chat English 👀**
<hr>

A faster way to make perpect sentence in English.

## Prerequisite
<hr>

- API Keys
  - [Google Cloud Vision API key](https://console.cloud.google.com/)
  - [ChatGPT API key](https://platform.openai.com/account/api-keys)

- Set environment variable
  - Open a terminal and run:

  ```bash
  $ env:GOOGLE_APPLICATION_CREDENTIALS="your dir/api-key.json"
  $ env:OPENAI_API_KEY="your dir/OpenAI api-key.json"
  ```

## Requirements
<hr>

Open a terminal and run:

```bash
$ conda create -n chat-english python=3.8
$ conda activate chat-english

$ cd [your working directory]
$ pip install requirements.txt
```

## Quickstart
<hr>

Run it open the app!

```bash
streamlit run app.py
```

- You can now view your Streamlit app in your browser.
  - Local URL: http://localhost:8501

## Usage

- You can improve the English sentences.
  - grammar   : correct grammar
  - naturally : more natural
  - easier    : more easy sentence expression
  - typo      : correct typo

<img src="https://user-images.githubusercontent.com/33558083/240276739-7ae82fa0-26a6-4b16-a845-ef767868d192.png" alt="Chat English example" width=500 href="none"></img>

- You can extract sentences from images, such as PDFs.
  - First, upload the image.
  - Second, you can extract sentences.
  - Third, copy and paste them into the message box

<img src="https://user-images.githubusercontent.com/33558083/240276207-793c708a-4792-48b5-9301-0b0f4f30a262.png" alt="OCR example" width=500 href="none"></img>


## License
<hr>

**Chat English** is available for non-commercial use.