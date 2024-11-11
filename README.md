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