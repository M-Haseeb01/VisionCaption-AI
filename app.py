import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load pretrained model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def caption_image(input_image: np.ndarray):
    # Convert numpy array to PIL Image
    raw_image = Image.fromarray(input_image).convert("RGB")

    # Process image
    inputs = processor(images=raw_image, return_tensors="pt")

    # Generate caption
    output = model.generate(**inputs)

    # Decode caption
    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption


# Gradio Interface
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(),
    outputs="text",
    title="Image Captioning",
    description="Upload an image and get an AI-generated caption."
)

iface.launch()
