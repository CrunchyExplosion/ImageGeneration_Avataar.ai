# Image Generation Using Stable Diffusion

## Purpose

This project utilizes the **Stable Diffusion** model to generate high-quality images based on provided text prompts and depth maps. The model allows for guided image generation, resulting in photo-realistic images that match user specifications. The implementation also explores the effects of aspect ratios on image generation quality and measures the latency of the generation process.

# Execution Steps
## Clone the Repository
```bash
git clone <repository_url>
cd <repository_directory>
```

## Installation Instructions

## Setup virtual environment
```bash
virtualenv myenv
.\myenv\Scripts\activate
```

To set up the environment and install the necessary libraries, execute the following commands:

```bash
pip install torch
pip install diffusers
pip install Pillow
pip install numpy
pip install torchvision
pip install tqdm
```



## Prepare Your Metadata
- Update the prompts and depths lists in the code with your own text prompts and corresponding depth map filenames.
- Ensure your depth maps are stored in the correct format (.png or .npy).

## Activate the virtual environment
```bash
.\myenv\Scripts\activate
```

## Run the Code
Execute the following command to generate images:
```bash
python generate_images.py
```

This command will generate images and save them to the specified output directory.

## Results and Analysis
- The generated images are saved in the generated_images directory.
- Aspect ratio tests demonstrate the impact of varying image dimensions on generation quality.
- Latency measurements provide insights into performance optimization through adjustments in the number of inference steps.

## Limitations and Future Directions

- **Limitations:** The quality of generated images may vary based on the complexity of prompts and the fidelity of depth maps. Additionally, running on a CPU may result in significantly longer latency.

- **Future Directions:** Future improvements could include implementing more advanced depth map conditioning methods, exploring additional parameters for image quality enhancement, and conducting user studies to assess visual quality from a subjective perspective.












