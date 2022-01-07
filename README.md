# DataVisualizationUpdate
## 新冠肺炎的可视化分析与研究
### 利用Python的requests库实时获取数据，存储本地MySQL数据库。
### 基于Django后端框架、Bootstrap前端框架和ECharts.js库进行开发，使用到了jQuery的Ajax技术。

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片1.png)

图1 全国疫情实时追踪

左侧两幅折线图分别代表近三个月全国累计确诊、现有疑似、累计治愈和累计死亡的人数以及全国新增确诊和新增疑似的趋势。中间则是当天的人数显示以及累计确诊地图，右侧两幅图则是当天全国新增确诊病例数量TOP5和新增病例地图。

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片2.png)

图2 全国疫情完整过程

该页面使用了2020年1月25日至今的所有数据，左侧改为动态柱状图和折线图。右侧确诊地图以及感染人数前十的省份两幅图则利用时间线组件动态更新，其变化过程如下图3、4所示。

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片3.png)

图3 全国疫情完整过程（01-25）

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片4.png)

图4 全国疫情完整过程（09-03）

全国疫情人数动态柱状图，其变化过程如下图5、6所示。

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片5.png)

图5 全国疫情人数动态柱状图（01-25）

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片6.png)

图6 全国疫情人数动态柱状图（09-03）

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片7.png)

图7 上海疫情实时追踪

该页面使用了2020年1月20日至今上海市的所有数据，左侧两幅折线图也相应调整。右侧确诊地图调整为三维形式，展示累计确诊各区占比。各区确诊人数占比则利用南丁格尔玫瑰图形式的饼状图展示，可以直观看出境外输入占到了极大的比重。

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片8.png)

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片9.png)

图8、9 上海疫情实时追踪（上海累计和新增趋势）

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片10.png)

图10 全球疫情实时追踪

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片11.png)

图11 全球疫情实时追踪（全球确诊人数TOP10）

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片12.png)

图12 全球疫情实时追踪（全球确诊人数占比）

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片13.png)

图13 全球疫情实时追踪（美国疫情累计趋势）

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片14.png)

图14 全球疫情实时追踪（美国疫情累计趋势4月24日至9月9日）

说明：美国疫情累计趋势折线图使用到了可拖动时间轴组件，支持用户查看其间一段时间区域的发展态势。

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片15.png)

图15 全球疫情模拟过程（1月27日）

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片16.png)

图16 全球疫情模拟过程（3月27日）

说明：全球疫情模拟过程部分出于获取到的字段不足以及后续处理的难度，没有使用真实数据。展现形式上，改为使用了可旋转的地球结合各国感染人数的柱状图，更加直观清晰。

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片17.png)

图17 疫情数据后台管理

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片18.png)

图18 查看全国各省份疫情历史数据

![image](https://github.com/Badw0lf613/DataVisualizationUpdate/blob/master/images/图片19.png)

图19 检索湖北省疫情历史数据
