# Voice transcription bot

## Installation

To run the bot on the local machine, you are going to need this:

* Python 3.6
* [Google cloud account](https://cloud.google.com)

## Configuration
Get credentials json for Google cloud account. See instructions on [this
page](https://cloud.google.com/speech-to-text/docs/reference/libraries?hl=ru#setting_up_authentication)

Configure the bot through the environment variables (or the `.env` file):

```
GOOGLE_APPLICATION_CREDENTIALS=selfmailbot-884932132121.json
TELEGRAM_TOKEN=7997:A-rFdCk_15BQQWao
TELEGRAM_PROXY=HTTP://207.154.200.199:3128
```
TELEGRAM_PROXY is optional variable. Use it if you hav troubles in direct
connections to Telegram API