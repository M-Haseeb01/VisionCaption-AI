# VisionCaption AI

VisionCaption AI is an AI-powered image captioning application that generates descriptive captions for uploaded images using the pretrained **BLIP Transformer** model from Hugging Face.

---

## Working Flow

```
Image Upload
      │
      ▼
Image Preprocessing (AutoProcessor)
      │
      ▼
BLIP Transformer Model
      │
      ▼
Token Generation
      │
      ▼
Caption Decoding
      │
      ▼
Generated Image Caption
```

---

## Technologies Used

- Python
- Gradio
- Hugging Face Transformers
- BLIP Model
- PyTorch
- Pillow

---

## Installation

```bash
git clone https://github.com/your-username/VisionCaption-AI.git

cd VisionCaption-AI

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

---

## Run the Project

```bash
python image_captioning_app.py
```

Open in your browser:

```
http://127.0.0.1:7860
```

---

## Demo

### Input Image

![Input Image](images/input.png)



---
