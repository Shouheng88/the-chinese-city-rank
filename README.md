# 中国城市排行

选择更适合你定居的城市

## 1、目录

- [方案说明](docs/方案设计.md)
- [最终完整榜单](docs/城市榜单.md)

## 2、个性化定制脚本使用说明

在 scripts 目录下使用如下命令即可输出结果，

```
python Cal.py
```

调节权重可以通过修改 [Cal.py](scripts/Cal.py) 脚本的常量实现，

```
IDEAL_HOUSE_PRICING_MIN = 10000 # 理想房价的最小值
IDEAL_HOUSE_PRICING_MAX = 15000 # 理想房价的最大值
ECONOMIC_PERCENTAGE = 10 # 经济权重
MEDICAL_PERCENTAGE = 10 # 医疗权重
HOUSE_PRICING_PERCENTAGE = 10 # 房价权重
FINANCE_PERCENTAGE = 10 # 财政权重
CONSTRUCTION_PERCENTAGE = 10 # 城建权重
CLIMATE_PERCENTAGE = 10 # 气候权重
TRAFFIC_PERCENTAGE = 10 # 交通权重
EMPLOYMENT_PERCENTAGE = 10 # 就业权重
EDUCATION_PERCENTAGE = 10 # 教育权重
```
