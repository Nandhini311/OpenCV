import matplotlib.pyplot as plt

def show_with_matplotlib(img, title, pos):
    # Convert BGR image to RGB
    img_RGB = img[:, :, ::-1]

    ax = plt.subplot(3, 3, pos)
    plt.imshow(img_RGB)
    plt.title(title)
    plt.axis('off')