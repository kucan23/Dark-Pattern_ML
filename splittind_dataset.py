import os
import shutil
import random
from math import ceil

source_image_folder = r"C:\Users\User\Desktop\dark pattern\Vins dataset\All Dataset\Android\JPEGImages"
source_label_folder = r"C:\Users\User\Desktop\dark pattern\Vins dataset\All Dataset\Android\labels"
project_folder = r"C:\Users\User\Desktop\dark pattern\Project"

# Create the necessary directories
os.makedirs(os.path.join(project_folder, 'train', 'data'), exist_ok=True)
os.makedirs(os.path.join(project_folder, 'train', 'label'), exist_ok=True)
os.makedirs(os.path.join(project_folder, 'test', 'data'), exist_ok=True)
os.makedirs(os.path.join(project_folder, 'test', 'label'), exist_ok=True)

# Get a list of image files
image_files = [f for f in os.listdir(source_image_folder) if f.endswith('.jpg')]

# Shuffle the list randomly with a consistent seed for reproducibility
random.seed(42)
random.shuffle(image_files)

# Calculate the number of images for each set (70% train, 30% test)
total_images = len(image_files)
train_count = ceil(total_images * 0.7)
test_count = total_images - train_count

# Split data into train and test
train_images = image_files[:train_count]
test_images = image_files[train_count:]

# Copy images and corresponding text files to the respective folders
for img_file in train_images:
    img_path = os.path.join(source_image_folder, img_file)
    shutil.copy(img_path, os.path.join(project_folder, 'train', 'data'))
    
    # Assuming the text files have the same name as the image files but with a '.txt' extension
    txt_file = img_file.replace('.jpg', '.txt')
    txt_path = os.path.join(source_label_folder, txt_file)
    shutil.copy(txt_path, os.path.join(project_folder, 'train', 'label'))

for img_file in test_images:
    img_path = os.path.join(source_image_folder, img_file)
    shutil.copy(img_path, os.path.join(project_folder, 'test', 'data'))
    
    # Assuming the text files have the same name as the image files but with a '.txt' extension
    txt_file = img_file.replace('.jpg', '.txt')
    txt_path = os.path.join(source_label_folder, txt_file)
    shutil.copy(txt_path, os.path.join(project_folder, 'test', 'label'))
