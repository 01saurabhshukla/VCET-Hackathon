# # import math
# # import numpy as np
# # import pandas as pd

# # imag1=r"C:\Users\saurabh shukla\Desktop\IDEX Project\Word Documents\imag1.1"
# # imag2=r"C:\Users\saurabh shukla\Desktop\IDEX Project\Word Documents\img1"



# # # img1 = image.png
# # def calculate_psnr(imag1, imag2):
# #     # img1 and img2 have range [0, 255]
# #     img1 = astype(np.float64).imag1
# #     img2 = astype(np.float64).imag2
# #     mse = np.mean((img1 - img2)**2)
# #     if mse == 0:
# #         return float('inf')
# #     return 20 * math.log10(255.0 / math.sqrt(mse))


# # calculate_psnr(imag1, imag2)

# from math import log10, sqrt
# import cv2
# import numpy as np
  
# def PSNR(original, compressed):
#     img1 = original.astype(np.float64)/255.
#     img2 = compressed.astype(np.float64)/255.
#     mse = np.mean((img1 - img2) ** 2)
#     if(mse == 0):  # MSE is zero means no noise is present in the signal .
#                   # Therefore PSNR have no importance.
#         return 100
#     max_pixel = 255.0
#     psnr = 20 * log10(max_pixel / sqrt(mse))
#     return psnr
  
# def main():
#      original = cv2.imread(r"C:\Users\saurabh shukla\Desktop\IDEX Project\Word Documents\imag1.1.jpg")
#      compressed = cv2.imread(r"C:\Users\saurabh shukla\Desktop\IDEX Project\Word Documents\img1.jpg")
#      value = PSNR(original, compressed)
#      print(f"PSNR value is {value} dB")
       
# if __name__ == "__main__":
#     main()

# # C:\Users\saurabh shukla\Desktop\IDEX Project\Word Documents\imag1.1
from PIL import Image
import cv2
img1 = cv2.imread(r"C:\Users\saurabh shukla\Desktop\IDEX Project\Word Documents\imag1.1.jpg")
img2 = cv2.imread(r"C:\Users\saurabh shukla\Desktop\IDEX Project\Word Documents\img1.jpg")
inp = Image.open(r"C:\Users\saurabh shukla\Desktop\IDEX Project\Word Documents\imag1.1.jpg")
out = Image.open(r"C:\Users\saurabh shukla\Desktop\IDEX Project\Word Documents\img1.jpg")
out = out.resize(inp.size)
print(inp.size,out.size)
psnr = cv2.PSNR(inp, out)