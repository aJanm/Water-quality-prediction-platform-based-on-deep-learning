# Water-quality-prediction-platform-based-on-deep-learning
## 基于深度学习的水质预测平台
### 项目背景：  
>近年来个个江河流域的工厂废水排放问题随着工业的大力发展愈发严重，以往的工业废水水质预测模型依然不能更好的满足需求。本文基于攀枝花市水质检测局的数据资料，利用数据分析、统计检验、深度学习时序模型等技术方法对研究工厂进行研究，依据主要水质检测成分信息构建了长短期记忆循环神经网络（LSTM）模型，对研究地10个工厂的废水排放进行了水质预测。结果显示：长短期记忆循环神经网络模型通过三个门来控制循环和记忆单元，有效控制了输入模型的特征信息，从而加强了模型的学习记忆能力提升了预测准确性。

### 项目介绍：  
>用深度学习中的长短期记忆循环神经网络（LSTM）模型来对某市的部分工厂废水按时间序列数据进行数据分析与研究。通过数据分析、数据预处理、建立模型，对工厂不同时刻排放水的水质进行学习、训练，进而对测试集水质数据进行测试预测。收集多个不同工厂研究预测得到的准确率，已验证该方法的可行性和有效性。并使用Django框架搭建一个可视化平台。

### 项目技术：  
>本平台搭建主要使用的编程语言为python，主要采用的技术为深度学习框架Tensorflow，web框架Django，并使用了Ajax，jQuery，Bootstrap等前端框架。

### 主要功能：  
>该平台的主要分为公众展示页面，管理员页面以及Admin管理工具三部分

>公众展示页面主要功能为：普通用户可以查询管理员上传的各省各市以及各工厂的排水数据，进而查询水质情况

>管理员页面主要功能为：1、查看各省市工厂排水数据；2、根据日期查看某工厂的排水数据；3、上传某工厂排水的数据；(需按照“测试.xls”样本数据中的格式，自定义可修改源码) 4、预测某工厂接下来一周的排水情况

### 操作步骤：
>该平台采用的python版本可为python3.6-python3.8  
>1、导入requirements.txt相关的依赖包  
>&ensp;&ensp;&ensp;具体导入步骤：  
>&ensp;&ensp;&ensp;pip install -r requirements.txt  
>&ensp;&ensp;&ensp;注：导入过程之前建议更换为国内源：  
>&ensp;&ensp;&ensp;pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/  
>&ensp;&ensp;&ensp;国内镜像源：  
>&ensp;&ensp;&ensp;阿里云 https://mirrors.aliyun.com/pypi/simple/ 
><br>&ensp;&ensp;&ensp;中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/  
>&ensp;&ensp;&ensp;豆瓣(douban) http://pypi.douban.com/simple/  
>&ensp;&ensp;&ensp;清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/  
>&ensp;&ensp;&ensp;中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/  
>&ensp;&ensp;&ensp;具体源可参考CSDN：
&ensp;&ensp;&ensp;https://blog.csdn.net/w5206666/article/details/116090935

>2、导入上述依赖包即可完成平台的测试  
&ensp;&ensp;&ensp;注：导入依赖包的过程Tensorflow如若报错，自行检查python版本，依旧报错自行将python版本降至3.6

## 注意：该开源项目只用作学习交流，不要用于商业活动

