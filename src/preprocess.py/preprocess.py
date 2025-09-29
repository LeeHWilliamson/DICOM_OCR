import matplotlib.pyplot as plt
import numpy as np
import os
import glob
from PIL import Image
import pydicom
import pytesseract


#open a DICOM with dcmread
ds = pydicom.dcmread("images/dicom_files/292821506_07-13-2013-XR_CHEST_AP_PORTABLE_for_Douglas_Davidson-46198_1001_000000-37718_1-1.dcm")
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
#plot it with matplotlib
plt.imshow(ds_pixel_array, cmap='gray')
plt.title(ds.PatientName)
plt.show()
#try extracting text
image = Image.open("pngs/test.png")
text = pytesseract.image_to_string(image)
print(text)

'''
PoC works. Lets make the actual pipeline
For each DICOM, we want to load it, extract relevant metadata, convert it to a png, process it, and then extract text with tesseract and output to a json, then delete the png
When we review the extracted text, look for any possible errors and then keep the associated images as pngs to test processing techniques
'''
#Navigating to dicom files...

root = "images/dicom_files" #set our root that every dicom will have in common
dicomPaths = []
files = os.listdir(root) #create list of paths of studies, we need to navigate to each 
# print(files)
for index in range(len(files)): #some studies contain an extra layer of nested folders so we need to build dicom paths carefully
    types = files[index].split(".")
    if types[-1] == "dcm":
         dicomPath = os.path.join(root, files[index])
         dicomPaths.append(dicomPath)
print(files)
# def scanFolder(folderPathStr):
#         for object in os.listdir(folderPathStr):
#             if ".dcm" in object: #if we are looking at a dicom, add it
#                 dicomPath = os.path.join(folderPathStr, object)
#                 dicomPaths.append(dicomPath)
#             else:
#                 scanFolder(os.path.join(folderPathStr, object))



print(len(dicomPaths))
for index in range(len(dicomPaths)): #now for each image, we read it as a dicom, extract metadata and burned-in text
    ds = pydicom.dcmread(dicomPaths[index])
    #we convert each to a pixel array, and then to a png for easier transformation
    ds_pixel_array = ds.pixel_array
    ds_pixel_array = (ds_pixel_array - np.min(ds_pixel_array)) / (np.max(ds_pixel_array)) * 255
    ds_pixel_array = ds_pixel_array.astype(np.uint8)
    #convert to png and save
    image = Image.fromarray(ds_pixel_array)
    image.save(os.path.join("pngs", "test.png"))
    metadataValues = {}
    #try extracting text
    if index == 10:
        print(dicomPaths[index])
        print(type(ds))
        print(ds.keys)
        metadataValues["Image Type"] = ds.get("Image Type")
        metadataValues["Modality"] = ds.get("Modality")
        metadataValues["Study Date"] = ds.get("Study Date")
        metadataValues["Study Description"] = ds.get("Study Description")
        metadataValues["Body Part Examined"] = ds.get("Body Part Examined")
        print(metadataValues)
        #plot it with matplotlib
        plt.imshow(ds_pixel_array, cmap='gray')
        plt.title(ds.PatientName)
        plt.show()
        image = Image.open("pngs/test.png")
        text = pytesseract.image_to_string(image)
        print(dicomPaths[index])
        print(text)
