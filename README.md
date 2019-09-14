# Json-Storage

## Requirements
- python 3.6+ 

### JsonParser.py

> The data store can be exposed as a library to clients that can instantiate a class and work
with the data store.

###### Examples
* Create a file in current folder 
```
python JsonParser.py
```
* To provide a folder path
```
python JsonParser.py <your-path>
windows : python JsonParser.py C:\Users\Arun\dev\Json-Storage
linux : python JsonParser.py /opt/python
```
* To edit a json file
```
python JsonParser.py <your-path/file.json>
windows : python JsonParser.py C:\Users\Arun\dev\Json-Storage\package.json
linux : python JsonParser.py /opt/python/package.json
```

> This works both in windows and linux

### Navigator.py

> You can use this to browse the file system and can choose a folder or json file to work with it but this only works in linux

