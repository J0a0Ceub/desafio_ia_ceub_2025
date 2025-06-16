from diffusers import StableDiffusionXLPipeline
# Carrega o modelo SDXL (Stable Diffusion XL)
pipeline = StableDiffusionXLPipeline.from_pretrained ("stabilityai/stable-diffusion-xl-base-1.0")
# Define a prompt (descrição da imagem a ser gerada)
prompt = "A gamer girl in sideral space playing Minecraft."
# Define o tamanho da imagem
width = 1024
height =1024
# Gera a imagem
image =pipeline(prompt, width=width, height=height).images[0]
# Salva a imagem gerada
image.save("generated_image_resized.png")
# Exibe a imagem
image. show()