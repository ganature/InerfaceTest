data={1:1,2:2,3:3}
for i, elem in enumerate(data):
    if isinstance(data, dict):
        key, value = elem, data[elem]
        print key,value