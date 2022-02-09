def imageResize():
    # Import required Image library
    from PIL import Image

    #Create an Image Object from an Image
    im = Image.open("./src/wiki.jpg")

    #Display actual image
    # im.show()

    #Make the new image half the width and half the height of the original image
    resized_im = im.resize((round(im.size[0]*4.36), round(im.size[1]*3.92)))

    #Display the resized imaged
    resized_im.show()

    #Save the cropped image
    resized_im.save('./src/wiki1.jpg')
    

imageResize()