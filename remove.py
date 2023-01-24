from rembg import remove
from PIL import Image

input_path = 'files/grupo-de-mulheres-diferentes-felizes-na-roupa-ocasional-70838365.jpg'
output_path = '2.png'
input_file = Image.open(input_path)
output = remove(input_file)
output.save(output_path)
