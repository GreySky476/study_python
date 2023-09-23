"""
python 安装第三方模块是通过 pip 完成
windows 电脑需要另外下载
mac、linux 大部分并存 python2、python3，因此 pip 命令为 pip3
第三方库都会在 python 官方注册，要安装第三方库需要知道库名称，比如 Pillow
命令为 pip install Pillow
安装常用模块
使用 python 开发时，会经常用到第三方库，比如 mysql、flask 等，一个个安装费时费力还需要考虑兼容性
可以直接使用 Anaconda，这是基于 python 的数据处理和科学计算平台，内置了许多非常有用的第三方库
可以从 Anaconda 官网下载：https://www.anaconda.com/download/
mac 安装完后使用 source ~/.bash_profile 刷新下配置文件

模块搜索路径
python 加载模块会在指定的路径下搜索对应的 .py 文件，如果找不到就会报错
默认路径可以使用 sys 模块的 path 变量查看
如果需要添加自己的搜索目录，有两种方式
第一：修改 sys.path，该变量是一个 list，使用 .append() 追加目录，该方式是在运行时修改，运行结束后失效
第二：设置环境变量 PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中，与设置 path 环境变量类似，只需要添加自身的搜索路径即可

"""

import sys

# 1、追加模块
sys.path.append('xxx/xxx.py')
# 2、window 考虑在系统环境变量中增加 PYTHONPATH，linx/mac 在 .bash_profile 中添加 export PYTHONPATH="xxx/"
