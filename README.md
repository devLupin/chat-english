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

## Usage

- You can improve the English sentences.
  - grammar   : correct grammar
  - naturally : more natural
  - easier    : more easy sentence expression
  - typo      : correct typo

<img src="https://user-images.githubusercontent.com/33558083/240260752-293bf1f0-3f21-485c-8007-528973cd0ab2.png" alt="Chat English example" width=500 href="none"></img>

- You can extract sentences from images, such as PDFs.
  - First, upload the image.
  - Second, you can extract sentences.
  - Third, copy and paste them into the message box

<img src="https://user-images.githubusercontent.com/33558083/240270745-d8963d2d-88d2-41b4-ab9e-b5451d5f7da5.png" alt="OCR example" width=500 href="none"></img>


## License
<hr>

**Chat English** is available for non-commercial use.