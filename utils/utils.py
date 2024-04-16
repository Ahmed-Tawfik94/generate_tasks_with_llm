import json , re
import demjson3
from jsonformatter import JsonFormatter
def get_json(data):
  if type(data) != dict:
    pattern = r"(?<!\w)'(.*?)'(?!\w)"
    if ('```json'in data):
      data = data.replace('```json','').replace('```','')
    else:
      return json.dumps(data)
    cleaned_string = re.sub(r'\n', '', data)
    modified_string = cleaned_string.replace("True","true").replace("False","false")
    json_data = demjson3.decode(modified_string)
    formatted = JsonFormatter(json_data)
    return demjson3.encode(formatted.json_fmt)
def is_valid_json(json_str):
    try:
        json.loads(json_str)
        return True
    except json.JSONDecodeError:
      return False