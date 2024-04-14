import requests
import os
import xml.etree.ElementTree as ET
from pathlib import Path

###########

# Set xml file path
# xml 파일 경로 설정
file_path = 'extracted_places.xml'  

# Specify the directory to store the image
# 이미지를 저장할 디렉토리 지정
image_dir = 'downloaded_images'

###########

# From below, you can modify code if you need it.
# 이 밑에서부터는 필요할 경우만 수정해 주시면 됩니다.

###########

Path(image_dir).mkdir(parents=True, exist_ok=True)


def download_image(image_url, file_name):
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        # Fix extension to .jpeg
        # 확장자를 .jpeg로 고정
        file_ext = '.jpeg'  
      
        file_path = os.path.join(image_dir, f"{file_name}{file_ext}")

        with open(file_path, 'wb') as f:
            f.write(response.content)

        print(f"Image downloaded and saved as: {file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download image from {image_url}. Error: {e}")


def parse_and_download_images(file_path):
    # parsing XML files
    # XML 파일 파싱
    tree = ET.parse(file_path)
    root = tree.getroot()

    for placemark in root.findall('.//Place'):
        name = placemark.find('name').text.strip().replace(' ', '_')
        image_urls = placemark.findall('image')
        image_count = 0

        for image in image_urls:
            image_url = image.text.strip()
            image_count += 1
            download_image(image_url, f"{name}_{image_count}")


# 실행
parse_and_download_images(file_path)
