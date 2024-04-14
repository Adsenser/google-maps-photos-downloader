from xml.etree import ElementTree as ET
import re

# please enter your kml file location
#여기에 변환할 kml 파일 경로 및 이름을 입력하세요.

###########

file_path ='example.kml' 

###########

# From below, you can modify code if you need it.
# 이 밑에서부터는 필요할 경우만 수정해 주시면 됩니다.

# The converted xml file is created under the name extracted_places.xml on the same path.
# 변환된 xml 파일은 동일 경로상에 extracted_places.xml 이름으로 생성됩니다.

###########

# Load and parse KML files
# KML 파일 로드 및 파싱
tree = ET.parse(file_path)
root = tree.getroot()

# Namespace definition (used in KML files)
# 네임스페이스 정의 (KML 파일에서 사용)
ns = {'kml': 'http://www.opengis.net/kml/2.2'}

# Create a root for a new XML file
# 새로운 XML 파일을 위한 루트 생성
new_root = ET.Element("Places")

# Extract required information and configure new XML
# 필요한 정보 추출 및 새 XML 구성
for placemark in root.findall('.//kml:Placemark', ns):
    place = ET.SubElement(new_root, "Place")

    # Extracting and adding names
    # 이름 추출 및 추가
    name = placemark.find('kml:name', ns).text
    ET.SubElement(place, "name").text = name

    # Extracting and processing descriptions
    # 설명 추출 및 처리
    description = placemark.find('kml:description', ns).text

    # Remove HTML tags and extract text only
    # HTML 태그 제거 및 텍스트만 추출
    text_only = re.sub('<[^<]+?>', '', description)
    ET.SubElement(place, "description").text = text_only

    # Extract and add image links
    # 이미지 링크 추출 및 추가
    img_links = re.findall('src="([^"]+)"', description)
    for img_link in img_links:
        ET.SubElement(place, "image").text = img_link

    # Coordinate extraction and processing
    # 좌표 추출 및 처리
    coordinates = placemark.find('.//kml:coordinates', ns).text

    # 5 decimal places limit and remove '0,0'
    # 소수점 5자리 제한 및 ',0' 제거
    coords = ','.join(['{:.5f}'.format(float(coord)) for coord in coordinates.split(',')[:2]])
    ET.SubElement(place, "coordinates").text = coords

# Create ElementTree for New XML File Storage
# 새로운 XML 파일 저장을 위한 ElementTree 생성
new_tree = ET.ElementTree(new_root)

# Define the file path to save
# 저장할 파일 경로 정의
new_file_path = 'extracted_places.xml'

# Save as a new XML file
# 새로운 XML 파일로 저장
new_tree.write(new_file_path, encoding='utf-8', xml_declaration=True)

new_file_path
