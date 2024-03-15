import os
import xml.etree.ElementTree as ET

def convert_annotation(xml_file_path, class_dict, image_width, image_height):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    yolo_lines = []

    for obj in root.findall('object'):
        obj_class = obj.find('name').text
        if obj_class not in class_dict:
            class_dict[obj_class] = len(class_dict)  # Assign a new index for unseen classes

        class_id = class_dict[obj_class]

        box = obj.find('bndbox')
        xmin = float(box.find('xmin').text)
        ymin = float(box.find('ymin').text)
        xmax = float(box.find('xmax').text)
        ymax = float(box.find('ymax').text)

        # Normalize coordinates
        x_center = (xmin + xmax) / (2.0 * image_width)
        y_center = (ymin + ymax) / (2.0 * image_height)
        box_width = (xmax - xmin) / image_width
        box_height = (ymax - ymin) / image_height

        yolo_lines.append(f"{class_id} {x_center:.6f} {y_center:.6f} {box_width:.6f} {box_height:.6f}")

    return yolo_lines

def main():
    input_folder = "Annotations"
    output_folder = "YOLO"
    class_dict = {}

    for filename in os.listdir(input_folder):
        if filename.endswith(".xml"):
            xml_file_path = os.path.join(input_folder, filename)
            image_filename = os.path.splitext(filename)[0] + ".jpg"
            image_width = 720  # Replace with actual image width
            image_height = 1280  # Replace with actual image height

            yolo_lines = convert_annotation(xml_file_path, class_dict, image_width, image_height)

            yolo_file_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")
            with open(yolo_file_path, 'w') as yolo_file:
                yolo_file.write("\n".join(yolo_lines))

if __name__ == "__main__":
    main()
