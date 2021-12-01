import json
import argparse


def dict_ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, dict_ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(dict_ordered(x) for x in obj)
    else:
        return obj


def get_modified_info(tags, field):
    ids = [x['tag'][field] for x in tags]
    return ids


def dict_has_key(key, obj):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                return True
            else:
                ret = dict_has_key(key, v)
                if ret:
                    return True
    elif isinstance(obj, list):
        for x in obj:
            ret = dict_has_key(key, x)
            if ret:
                return True
    else:
        pass


def validate_keys(obj, keyslist):
    for key in keyslist:
        if dict_has_key(key, obj) is not True:
            print(f'no such key: {key} in result ')


def validate_tag_value(tags, field, expected_value):
    tmp = get_modified_info(tags, field)
    if expected_value not in tmp:
        print(f'the {field} of expected value: {expected_value} not in taglist{tmp}')


def validate_os(obj, expected):
    tmp = obj['market_code']
    if tmp != expected:
        print(f'{tmp} is not expected {expected}')


def validate_images(obj):
    tmp = obj['images']
    count, total = 1, 0
    for item in tmp:
        if not item['src']:
            print(f'validate_images --- The {count}th image url src value is not expected,Null')
            total += 1
        count += 1
    if total !=0:
        print(f'validate_images --- The total of the null image url is  {total} ')


def validate_video_fields(obj):
    tmp = obj['videos']
    count, total = 1, 0
    for item in tmp:
        if not item['cdn_stream'] or not item['cdn_thumbnail']:
            total += 1
            print('validate_video_fields --- The cdn_stream or cdn_thumbnail is not expected', item['cdn_stream'],item['cdn_thumbnail'])
        count += 1
    if total != 0:
        print(f'validate_video_fields --- The total of the null image url is  {total} ')

#todolist
#add tag count& other fields

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='manual to this script')
    parser.add_argument('--file', type=str, default='test.json')
    parser.add_argument('--pid', type=int, default=1000600000000165)
    parser.add_argument('--tagids', type=int, default=500002)
    parser.add_argument('--os', type=str, default='apple-store')
    args = parser.parse_args()
    file, product_id, tagids , os = args.file, args.pid, args.tagids, args.os
    with open(file) as json_file:
        result = json.load(json_file)
    print(result)

    keyslist = ['appName', 'appIcon', 'secondarySubgenreList','primaryGenreId','country_code','initialTagVersion']
    validate_keys(result, keyslist)
    validate_tag_value(result['tags'], 'modifier_id', 500002)
    validate_tag_value(result['tags'], 'modifier_name', 'Cartoony')
    validate_os(result,'apple-store')
    validate_video_fields(result)
    validate_images(result)

