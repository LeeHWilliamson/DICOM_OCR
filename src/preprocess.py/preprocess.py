import pydicom
import matplotlib.pyplot as plt

ds = pydicom.dcmread("images/manifest-1617826555824/Pseudo-PHI-DICOM-Data/292821506/07-13-2013-NA-XR CHEST AP PORTABLE for Douglas Davidson-46198/1001.000000-NA-37718/1-1.dcm")
plt.imshow(ds.pixel_array, cmap='gray')
plt.title(ds.PatientName)
plt.show()