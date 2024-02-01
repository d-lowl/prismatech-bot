# PrismaTech Chatbot

The accompanying [blogpost](https://d-lowl.space/smaller-transformers-as-llm-guardrails-prismatech-party-non-reveal/)

This repo is an example of how one can implement guardrails by fine-tuning BERT.

There are two modules here:
* `bert` -- the notebook and the dataset used for fine-tuning. The data is generated using Claude.
* `server` -- the actual chatbot implemented with streamlit and OpenAI API

## Fine-tuning
* Load the [notebook](bert/prismalab_guardrails.ipynb) in Colab
* Upload the data in the Colab storage
* Run the notebook
* The resulting weights can then be put into the server folder

## Running the server
* `poetry install && poetry shell` to set up the environment
* `streamlit run server/app.py` to start the server

The following environment variables MUST be set before running:
* OPENAI_API_KEY
* PASSPHRASE
* PARTY_DATE
* PARTY_LOCATION
* PARTY_THEME
* PARTY_DRESSCODE
* PARTY_MENU
