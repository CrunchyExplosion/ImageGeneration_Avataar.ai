# Image Generation Using Stable Diffusion

## Purpose

This project utilizes the **Stable Diffusion** model to generate high-quality images based on provided text prompts and depth maps. The model allows for guided image generation, resulting in photo-realistic images that match user specifications. The implementation also explores the effects of aspect ratios on image generation quality and measures the latency of the generation process.

# Execution Steps
## Clone the Repository
```bash
git clone https://github.com/CrunchyExplosion/StableDiffusion_imageGenerator
```


## Setup virtual environment and activate it
```bash
virtualenv myenv
.\myenv\Scripts\activate
```
remember to do everything in virtual environment

Now install the necessary libraries, execute the following command:
```bash
pip install -r requirements.txt
```



## Prepare Your Metadata
- Ensure your depth maps are stored in the correct format (.png or .npy).


## Run the Code
Execute the following command to generate images:
```bash
python generate_images.py
```
This command will 
1. Ask for the mask
2. Ask for the desired prompt - `describe how you want your image to be`


## Results and Analysis
- Finally the program generates image and save them to the folder named `output_images`.

## Observations directory contain the following observations
- How quality affected for diffrent aspect ratio
- Generation latency and how it can be reduced

## Limitations and Future Directions

- **Limitations:** The quality of generated images may vary based on the complexity of prompts and the fidelity of depth maps. Additionally, running on a CPU may result in significantly longer latency.

- **Future Directions:** Future improvements could include implementing more advanced depth map conditioning methods, exploring additional parameters for image quality enhancement, and conducting user studies to assess visual quality from a subjective perspective.


-------------------------------------------------------------------------------------------

# About the files in whole repo
## Genereated images    = contain many images with mask and promt generated by model
## Observation          = important observations made 
## Image generation pdf = has a pdf summing up all this project
## readme.md            = readme.md
## generate_image.py    = soul of project **THE CODE**
## requirements.txt     = All libraries in one place which you need
## sample_output.png    = The sample successful working of the project

------------------------------------------------------------------------
Thank you for checking out this repo. 
All the best













