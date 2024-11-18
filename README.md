# AI-Academic-Assistant


修改步骤:
1. 先改 Section_C_input.py 中的dict
2. 再去 Section_C_app copy.py 中print,测试
3. 再把确认的结果放到 Section_C_app.py中,先不要运行
4. 然后去 templeates 文件夹里面的 article_details.html 修改网站的格式,有注释,大概结合网站看看能理解,不懂找Copoilot
5. 运行Section_C_app.py,打开网站

11/11/2024 下午修改Section_B部分-zzh：
1. Section_B_get_cited_by.py: 加入判断，避免因为文章未被引用过而系统终止；
2. Section_C_app、html文件相关部分：按需求改了；
3. 出于把所有输出整合到一起的需求，新增一个Section_B_get_output.py文件来完成这个工作。引用方法：
```python
from Section_B_get_output import get_Section_B_output
output = get_Section_B_output(pdf_name, article_name, translation)
```

11/11/2024 晚上修改:
1. 接入 Section_D部分真实输出，并调试成功

遗留任务：
1. 接入 Section_A & Section_B 部分真实输出，并调试成功 - zzh
2. 检查是否所有的input.py里面的key都在网站里面 - zzh

3. 调整UI格式，没那么丑 - yql&zzh（zzh也需要了解怎么调，给点建议，大家都是直男审美都拉）

11/13/2024 凌晨：
1. 接入Section_B真实输出并调试成功
2. 前端部分新增404页面，用于处理非法路径
3. 修改index.html，主要是把内容移到侧边栏，并增加了小组成员；引入了背景图片
4. 修改style.css，增加了侧边栏和背景图片相关类的定义

11/14/2024 凌晨-zzh：
1. 修改被引用文章模块，增加错误反馈判断与处理，并修改相关前端页面
2. 修改requirements.txt，解决其中模块冲突问题
    · playwright==1.46.0
    · pyee==11.1.0
    · pyppeteer==2.0.0
    · greenlet==3.0.3
    · ↑以上包版本保持这样，不然会有冲突
    · fitz ←这个包不需要，因为pdf解析用的包PyMuPDF在导入文件的时候用的也是import fitz， 这两个fitz不一样，单独下的话会出错
    · 只下一个PyMuPDF足够了
3. 遗留问题：
    · 章节总结和逻辑链部分写的不完善导致ai反馈不尽人意--尚未修改
    · 前端优化
    · AI反馈时间太长？ ->建议考虑加点什么

11/14/2024 下午-zzh：
1. 优化Section B不分逻辑，增加了错误处理模块，完善了prompt设计
2. 主要前端页面增加背景图片

11/19/2024 晚上-zzh：
reloading问题：之前添加了一个图片打压缩包打的逻辑，这个逻辑在打包的过程中会多次修改zip文件，导致web应用在debug模式下因为后台文件被修改而多次重启，最终使服务中断
修改方法：
1. 关闭debug模式：app.py中将debug参数设置为False
2. 关闭打包功能：Section_B_pdf_processing.py中注释掉line 18
其他修改：运行xlsx download的时候报错没有xlsxwriter包，加到requirements.txt里面了