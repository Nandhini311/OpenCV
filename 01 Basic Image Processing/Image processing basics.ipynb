{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "from matplotlib import pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "#accessing and manipulating pixels in openCV and BGR images\n",
    "#loading the image\n",
    "img = cv2.imread('logo.png')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(577, 476, 3)\n"
     ]
    }
   ],
   "source": [
    "#get dimensions of the image\n",
    "print(img.shape) \n",
    "#color image - rows, columns, no. of channel\n",
    "#grayscale - rows, columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "823956\n"
     ]
    }
   ],
   "source": [
    "#image size - height x weight x channels\n",
    "total_number_elements = img.size\n",
    "print(total_number_elements)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "uint8\n"
     ]
    }
   ],
   "source": [
    "#image datatype\n",
    "print(img.dtype)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "-1"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#to display an image\n",
    "cv2.imshow(\"original image\",img)\n",
    "cv2.waitKey(0) #the program waits indefinitely for an keyboard event"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "255 255 255\n",
      "255\n"
     ]
    }
   ],
   "source": [
    "#to access (i.e read) a pixel value , we should provide the row and column of the desired pixel\n",
    "(b,g,r) = img[6,40] #y=6(row),x=40(column)\n",
    "#this will give the pixel value at x=60, y=4\n",
    "print(b,g,r)\n",
    "#accesing one particular channel\n",
    "b = img[6,40,0]\n",
    "print(b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#modifying the pixel value\n",
    "img[6,40] = (0,0,255)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "#dealing a particular region instead of just a pixel\n",
    "top_left_corner = img[0:50,0:50]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## accessing and manipulating pixels in openCV with grayscale image\n",
    "\n",
    "grayscale images have only one scale and hence can't be approached in the same way"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(577, 476, 3)\n"
     ]
    }
   ],
   "source": [
    "imgGray = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)\n",
    "print(img.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#accessing the pixel value\n",
    "i = imgGray[6,40]\n",
    "#modifying the pixel value\n",
    "imgGray[6,40] = 255 #white"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## BGR order in OpenCV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "img_openCV = cv2.imread('logo.png')\n",
    "#splitting the loaded image into its three channels (b,g,r):\n",
    "b, g, r = cv2.split(img_openCV)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "#merge again the three channels but in the RGB \n",
    "img_matplotlib = cv2.merge([r,g,b])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function matplotlib.pyplot.show(*args, **kw)>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#BGR\n",
    "plt.subplot(121)\n",
    "plt.imshow(img_openCV)\n",
    "\n",
    "#RGB\n",
    "plt.subplot(122)\n",
    "plt.imshow(img_matplotlib)\n",
    "plt.show"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "#showing two images in a single window\n",
    "#cv2.imshow('bgr image', img_openCV)\n",
    "#cv2.imshow('rgb image', img_matplotlib)\n",
    "#cv2.waitKey(0)\n",
    "#cv2.destroyAllWindows()\n",
    "\n",
    "#stacking horizontally \n",
    "img_concats = np.concatenate((img_openCV, img_matplotlib), axis=1)\n",
    "#displaying the concatenated image\n",
    "cv2.imshow('bgr image and rgb image', img_concats)\n",
    "cv2.waitKey(0)\n",
    "cv2.destroyAllWindows()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "#using another method instead of split (time consuming)\n",
    "B = img_openCV[:,:,0]\n",
    "G = img_openCV[:,:,1]\n",
    "R = img_openCV[:,:,2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "img_matplotlib = img_openCV[:,:,::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
