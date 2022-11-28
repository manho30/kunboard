# kunboard
鸡你太美键盘

本项目基于MIT许可证开发

# 开发
这是一个简单说明，更详细的内容可在伟大的谷歌上获取。
## 克隆本仓库
``` sh
$ git clone https://github.com/manho30/kunboard
$ cd kunboard
```


### 安装依赖库
``` sh
$ pip install -r requirements.txt
```

> :warning: 此处注意，[playsound](https://github.com/TaylorSMarks/playsound) 模块切勿升级至`1.3.0`版本! 

- 同时需要安装 [Pyinstaller](https://pyinstaller.org/en/stable/) 模块进行编译打包
``` sh
$ pip install pyinstaller
```



## 编译
``` sh
$ pyi-makespec -F -i .\public\img.png -w .\utils.py
```



### 修改.spec文件

找到datas，修改成以下一行
``` spec
datas = datas=[('audios','audios'),('public','public')]
```


###  运行
``` sh
$ pyinstaller .\qt_util.spe
```
