# cczu_kexie_online_submit
- ### 常州大学校科协线上报名系统

    - 为常大校科协开发的线上报名与管理一体化系统，后期考虑加上投票系统，与活动无缝对接


# 开发与维护依赖环境

- ### 本系统基于django2.2，使用python3.7开发。
- ### 数据库
    - #### postgresql-12
- ### 服务器配置：
    - #### nginx+gunicorn+django

### 使用到的python库：
- django2.2
- django-cleanup
- psycopg2
- gunicorn
- sqlparse

# 特色功能介绍
- ### 高度可自定义
    - 自定义活动名称
    - 自定义活动介绍
    - 自定义活动群号
    - 自定义活动群二维码
    - 自定义界面背景图
    - 自定义界面背景图
    - 自定义活动组队人数
    - 自定义何时截止线上报名
- ### 学院与专业信息可选择
    - 专业选项根据学院的选择动态生成
    - 学院与专业信息可通过后台管理随时修改
- ### 人性化的功能
    - 可在后台管理界面自动生成数据表格并下载，表格数据可根据选择数据生成

# 更新计划(todo)
- ### 学院与专业选项框可搜索
    - 有的学院专业太多，学校的学院也不少，增加筛选搜索功能将提高填写效率
