# Slade Brooks
# spbrooks4@gmail.com
# how much of this is from stack overflow...?

import os
from PIL import Image

imageSet = []
framesASec = 10
loopBool = True

gif = Image
gif.save(fp=fp_out, format="GIF", save_all=True, append_images=imageSet, duration=framesASec, loop=loopBool)