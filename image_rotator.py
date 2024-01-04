import os
import shutil
from PIL import Image

class ImageRotator:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    @staticmethod
    def images_are_same(img1_path, img2_path):
        """
        Checks if two images are the same.
        """
        try:
            img1 = Image.open(img1_path)
            img2 = Image.open(img2_path)
            return list(img1.getdata()) == list(img2.getdata())
        except IOError:
            return False

    @staticmethod
    def rotate_and_save_image(image_path, save_path, angle):
        """
        Rotates an image and saves it to a specified path.
        """
        image = Image.open(image_path)
        rotated_image = image.rotate(angle, expand=True)
        rotated_image.save(save_path)

    def process_folders(self):
        """
        Process each folder in the root directory.
        """
        for folder_name in os.listdir(self.root_dir):
            folder_path = os.path.join(self.root_dir, folder_name)
            if os.path.isdir(folder_path):
                self.process_images(folder_path)

    def process_images(self, folder_path):
        """
        Process each image in the folder.
        """
        background_image_path = os.path.join(folder_path, 'background.png')
        frames_folder_path = os.path.join(folder_path, 'frames')
        
        # Check if the background image exists
        if not os.path.exists(background_image_path):
            print(f"Background image not found in {folder_path}")
            return

        # Check if frames folder and background_0.png exist
        first_frame_path = os.path.join(frames_folder_path, 'background_0.png')
        if os.path.exists(first_frame_path) and self.images_are_same(background_image_path, first_frame_path):
            print(f"No changes needed for {folder_path}")
            return

        # Delete frames folder if it exists and create a new one
        if os.path.exists(frames_folder_path):
            shutil.rmtree(frames_folder_path)
        os.makedirs(frames_folder_path)

        # Rotate and save images
        for angle in range(360):
            save_path = os.path.join(frames_folder_path, f'background_{angle}.png')
            self.rotate_and_save_image(background_image_path, save_path, angle)
            print(f"Saved: {save_path}")

# Usage
images_directory = 'Visuals'
rotator = ImageRotator(images_directory)
rotator.process_folders()
