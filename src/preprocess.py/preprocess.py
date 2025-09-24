import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image
import pydicom
import pytesseract


#open a DICOM with dcmread
ds = pydicom.dcmread("images/manifest-1617826555824/Pseudo-PHI-DICOM-Data/292821506/07-13-2013-NA-XR CHEST AP PORTABLE for Douglas Davidson-46198/1001.000000-NA-37718/1-1.dcm")
print(type(ds))
print(ds)
#lets extract Image Type, Study Date, Modality, Study Description, Body Part Examined
#convert to png - normalize pixel data
ds_pixel_array = ds.pixel_array
ds_pixel_array = (ds_pixel_array - np.min(ds_pixel_array)) / (np.max(ds_pixel_array)) * 255
ds_pixel_array = ds_pixel_array.astype(np.uint8)
#convert to png and save
image = Image.fromarray(ds_pixel_array)
image.save(os.path.join("pngs", "test.png"))
# #plot it with matplotlib
# plt.imshow(ds_pixel_array, cmap='gray')
# plt.title(ds.PatientName)
# plt.show()
#try extracting text
image = Image.open("pngs/test.png")
text = pytesseract.image_to_string(image)
print(text)