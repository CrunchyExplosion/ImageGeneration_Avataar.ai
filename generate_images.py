import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import numpy as np
from torchvision import transforms
import time
import os

# Define the pipeline
model_id = "CompVis/stable-diffusion-v1-4"
pipe = StableDiffusionPipeline.from_pretrained(model_id)  # Remove torch_dtype for CPU compatibility
pipe = pipe.to("cpu")  # Ensure it's set to use CPU

# Function to prompt user for input
def get_user_input():
    depth_path = input("Enter the path to the depth map (mask) file: ")
    prompt = input("Enter the text prompt: ")
    return prompt, depth_path

# Function to process depth map (handles both PNG and NPY formats)
def process_depth_map(depth_path):
    if depth_path.endswith(".png"):
        depth_map = Image.open(depth_path)
        depth_map = transforms.ToTensor()(depth_map)
    elif depth_path.endswith(".npy"):
        depth_map = torch.from_numpy(np.load(depth_path))
    
    # Ensure depth_map is in the correct format (3D tensor)
    if len(depth_map.shape) == 2:
        depth_map = depth_map.unsqueeze(0)  # Add channel dimension if necessary
    return depth_map

# Function to generate and save image
def generate_image(prompt, depth_map, output_dir):
    os.makedirs(output_dir, exist_ok=True)  # Create output directory if it doesn't exist

    # Measure the generation latency
    start_time = time.time()

    # Generate the image with reduced inference steps (25 steps for faster processing)
    image = pipe(
        prompt=prompt,
        depth=depth_map,
        num_inference_steps=25,
        guidance_scale=7.5,
        seed=12345,
        height=512,
        width=512
    ).images[0]

    end_time = time.time()
    latency = end_time - start_time
    print(f"Generation latency: {latency:.4f} seconds")

    # Save the image
    image_filename = f"{output_dir}/{prompt.replace(' ', '_')}.png"
    image.save(image_filename)
    print(f"Image saved to {image_filename}")

# Main execution flow
if __name__ == "__main__":
    prompt, depth_path = get_user_input()  # Ask user for prompt and mask path
    depth_map = process_depth_map(depth_path)  # Process depth map
    output_dir = "output_images"  # Output directory for generated images
    generate_image(prompt, depth_map, output_dir)  # Generate and save the image
