# Cv-reader

Display CV information in the browser and CLI

## Project setup

Prerequisites:
- Local machine with Python 3.8 or above installed

Installation:
- Clone project
- Using the command-line interpreter navigate to local cloned directory and run: 
```
pip install -r requirements.txt
```

## API Usage
- To start local server navitate to project directory using the command-line interpreter and run
```
python main.py runserver
```
- In the browser navigate to localhost address provided in the prompt (ex: http://123.0.0.1:5678)
- Append the address with provided endpoints to see the respective sections (/personal, /experience, /education)

## CLI Usage
- Using the command-line interpreter navigate to local cloned directory
- Use the following commands to view the CV sections
```
cli-viewer.py --section personal
cli-viewer.py --section experience
cli-viewer.py --section education
```
- or ```cli-viewer.py``` for additional information on how to use the command
- also can use ```cli-viewer.py``` for additional information