import re

source_path = '/Users/wangyijun/ads/app/forms/staff.py'
target_path = '/Users/wangyijun/ads/app/forms/pydantic_staff.py'
class_str = r'class ([a-zA-Z]+)\(([a-zA-Z\.]+)\)'
class_comp = re.compile(class_str)
attr_str = r'([a-z_]+) = ([A-Za-z]+)\('
attr_comp = re.compile(attr_str)
attr_field_str = r'\'[a-z_]+\'\, validators=\[\]'


def get_match(file_obj, line):
    class_match = class_comp.match(line)
    if class_match:
        data = class_match.groups()
        name = data[0]
        father = data[1]
        if father.startswith('pydantic'):
            return line
        if father == 'PagerForm':
            return f'class {name}(Pager):\n'
        return f'class {name}(pydantic.BaseModel):\n'

    tmp_line = line.strip()
    attr_match = attr_comp.match(tmp_line)
    if attr_match:
        data = attr_match.groups()
        name = data[0]
        field_name = data[1]
        if field_name == 'IntegerField':
            return f'    {name}: int\n'
        elif field_name == 'DateTimeField':
            return f'    {name}: datetime\n'
        elif field_name == 'JSONField':
            return f'    {name}: pydantic.Json\n'
        elif field_name == 'StringField':
            return f'    {name}: str\n'
        elif field_name == 'ObjectIdField':
            return f'    {name}: PydanticObjectId\n'
    return line


def trans_file():
    data = []
    with open(source_path, 'r') as file_obj:
        for line in file_obj:
            target_line = get_match(file_obj, line)
            data.append(target_line)

    with open(target_path, 'w+') as file_obj:
        file_obj.write(''.join(data))


if __name__ == "__main__":
    trans_file()
