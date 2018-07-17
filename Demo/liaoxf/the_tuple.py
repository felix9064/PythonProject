#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# python中的tuple（元组）不可变列表类型

print("tuple和list非常类似，tuple一旦初始化就不能修改")

classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)

t = (1,)
print("只有1个元素的tuple定义时必须加一个逗号, t =", t)

# cannot modify tuple:
# classmates[0] = 'Adam'

# 洛杉矶国际机场经纬度
lax_coordinates = (33.9425, -118.408056)

# 东京市的一些信息（城市名，年份，人口，人口变化，面积）
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

for country, _ in traveler_ids:
    print(country)


metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:^15} | {:^9} | {:^9}'.format('name', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name, cc, _, (latitude, longitude) in metro_areas:
    if longitude < 0:
        print(fmt.format(name, latitude, longitude))
