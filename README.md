download the model translation files from https://huggingface.co/facebook/nllb-200-distilled-600M/tree/main,
and put it inside my-model folder

pastikan python sudah terinstall lalu jalankan:

- pip install transformers flask torch
- python model_server.py

express server:

- npm i
- npm run start

coba akes dari http://localhost:3000/

dengan body post:

{
"text": "Hello, how are you?",
"src": "eng_Latn",
"tgt": "ind_Latn"
}
