## 项目总体规划

### 组员分工

组长：刘永昊

组员：杨璟昊 吕涌波 张翼鹏 曹树

刘永昊：视频、幻灯、文案、解决杂七杂八的问题

杨璟昊：硬件（写端口Mapping，并且和Arduino同学沟通好该如何使用）

<<<<<<< HEAD
吕涌波：负责联动任务
=======
吕涌波: 写代码
>>>>>>> cb2ec417660ab4ea523feec8db370f5e9a00e570

张翼鹏：写代码

曹树：建模

### 项目的工作方式

这个项目工作在树莓派Raspbian上。程序使用opencv-python识别人脸，然后利用波特通讯包控制Arduino操控投石器。树莓派连接Arduino和Microduino。前者操控转向和投石器舵机，后者操控小车传动马达。**关于如何让树莓派同时连接两台\*duino设备：装机后把它们同时连接到树莓派，在命令行窗口里列举所有外围设备的ID，在其中找到两台设备分别的编号**

基础任务：按照老师的要求作出可以工作的单自由度投石机。

附加任务：使用Microduino操控小车。使用超声波等传感器确定和人的距离，跟着人走，并且在瞄准之后发射炮弹（对“瞄准”的定义：瞄准器在一段时间之内没有作出调整动作）。

联动任务：用mcpi连接到Minecraft，Minecraft中的人物随着小车位置的变动而变动。随着炮弹的发射，在该坐标下调用写好的House类方法建造房子和雕像。



### 还没实现的功能

基础任务：舵机方位调整功能；人脸识别准确率需提高。

附加任务：全部。

联动任务：全部。