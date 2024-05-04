from PIL import Image
import numpy as np

def encrypt_image(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to numpy array
    img_array = np.array(img)
    
    # Generate encryption key with the same shape as the image
    encryption_key = np.random.randint(0, 256, size=img_array.shape)
    
    # Apply encryption algorithm to each pixel
    encrypted_array = np.bitwise_xor(img_array, encryption_key)
    
    # Create encrypted image from the encrypted array
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    
    # Save the encrypted image
    encrypted_img.save('encrypted_image.png')
    print("Image encrypted successfully.")
    
    # Return the encryption key for decryption
    return encryption_key

def decrypt_image(encrypted_image_path, decryption_key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert the image to numpy array
    encrypted_array = np.array(encrypted_img)
    
    # Apply decryption algorithm to each pixel
    decrypted_array = np.bitwise_xor(encrypted_array, decryption_key)
    
    # Create decrypted image from the decrypted array
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    
    # Save the decrypted image
    decrypted_img.save('decrypted_image.png')
    print("Image decrypted successfully.")

# Example usage
image_path = 'E:/learn/projintern/ne.png'
encryption_key = encrypt_image(image_path)
decrypt_image('encrypted_image.png', encryption_key)


#image_path = 'C://Users/user/Desktop/one.jpg'
