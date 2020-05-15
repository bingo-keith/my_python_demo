import json
from pygal_maps_world.i18n import COUNTRIES


def get_country_code(country_name):
    """根据指定的国家，返回Pygal使用的两个字母的国别码"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # 如果没有找到指定的国家，返回None
    return None


# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

    # 打印每个国家的人口数量
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name1 = pop_dict['Country Name']
            # 对于浮点数直接用int转化会报错，可以先用float转化再用int
            population = int(float(pop_dict['Value']))
            code1 = get_country_code(country_name1)
            if code1:
                print(code1 + ': ' + str(population))
            else:
                print("Error - " + country_name1)


