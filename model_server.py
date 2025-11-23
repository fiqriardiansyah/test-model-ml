from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

MODEL_PATH = "./my-model"

print("Loading local NLLB model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)
print("Model loaded!")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()
    text = data["text"]

    src = data.get("src", "eng_Latn")
    tgt = data.get("tgt", "ind_Latn")

    # IMPORTANT: Set the source language manually
    tokenizer.src_lang = src

    # Tokenize without src_lang param
    inputs = tokenizer(text, return_tensors="pt")

    # Set target language token
    forced_bos = tokenizer.convert_tokens_to_ids(tgt)

    outputs = model.generate(
        **inputs,
        forced_bos_token_id=forced_bos,
        max_length=200
    )

    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return jsonify({"translation": translation})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)
