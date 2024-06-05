## Image Analysis Script

Analyze images using Azure AI Vision to generate captions, tags, objects, and remove backgrounds.

### Prereq's

- Python 3.8+
- Azure Computer Vision resource

### Installation

```sh
pip install python-dotenv pillow matplotlib azure-core azure-ai-vision-imageanalysis requests
export VISION_ENDPOINT="https://your-resource-name.cognitiveservices.azure.com"
export VISION_KEY="your-key"
```

### Usage

```sh
python script.py [path_to_image]
```
(Default: `images/street.jpg`)

### Features

- Generate captions, tags, objects
- Remove background (saves as `background_removed.png`)

### Example Output

```sh
Analyzing image...
Image analysis results:
 Caption: 'A street with cars', Confidence 0.9
 Tags: car (confidence: 0.95)
 Objects: car (confidence: 0.9)
Background removed and saved as background_removed.png
```
