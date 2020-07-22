# Image-Compression
Project Title: Image Compression by dominant colours representation

Project Description: Large images are an overhead to send over the internet but when we can trade off between the quality of image and its size, Since there are possibly many colours which are present in the real world and one of the representation used is RGB,where we store the quantity of the primary colours for each pixel,then we can reduce a good amount size of the image by representing it by the dominant colours present in it.

Dataset: We took an image form the internet for this project,but any image can be used and worked on.

Project Detail: Firstly we took the image for preprocessing,Since the size of image was too large we resized the image to a new size corresponding to the ratio of original image.Since every pixel is represented by RGB colours so we flattened the whole image. Since all the pixel can be visualized as the points in a three dimensional plane se we used unsupervised machine learning models to find the dominant colours present in it. Since we needed the number of clusters so we used Elbow's method to get the number of clusters to divide the pixels into. Then we initialized clusters with random values and them implemented K-Means Algorithm to it to find the Dominant colours.
After getting the dominant colours we represented the whole original image with that colours.

Outcome: The resultant image was represented from the original image.
