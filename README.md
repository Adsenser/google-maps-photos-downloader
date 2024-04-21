# Google-maps-photos-downloader
Google maps's photos auto downloader script

구글맵의 사진들을 손쉽게 일괄 다운로드 할 수 있는 스크립트 입니다.

파이썬 코드로 작성했으며, Instruction의 순서를 따라서 이용해 주시면 됩니다.

## Instruction

First of all, we need the kml file of Google Maps.

### KML file

<p align="center">
  <img width="45%" src="https://pub-995fbd6d8766436bafae8b7b522ebaf8.r2.dev/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202024-04-14%2017.24.56.png">
  <img width="45%" src="https://pub-995fbd6d8766436bafae8b7b522ebaf8.r2.dev/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202024-04-14%2017.25.06.png">
</p>

1. Download KML 
2. Check 'Export as KML instead of KMZ.'
3. Click 'OK'

### Convert to XML

then, it is necessary to convert the kml file into xml format.

1. Open the 'kml-to-xml.py' script and enter the path of the kml file you want to extract.
2. Follow the instructions in the .py comment.

### Auto download

Now, We can download photos in kml

1. Open 'auto-photos-downloader.py' , specify the path of the xml file and the path of the photos to be extracted, and run the script.
2. Photos on Google Maps are automatically downloaded using the marker name as the photo name.

# From kml To xml converter
Google maps's .kml -> .xml 

It is a script that easily converts the kml format used by Google Maps into xml format.

Extract the marker's coordinates, name, description, and added photos, and convert them to xml format.

You can easily download all photos using a script that automatically downloads photos attached to Google Maps using converted xml files.

# Auto photos downloader
By default, we extract it in the form of a jpeg extension.

The photo name is set based on the name set in the marker.

# License

MIT © <a href="https://github.com/Adsenser/">Adsenser</a>
