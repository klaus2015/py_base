html = """
<span><a href="/typerank?type_name=剧情&type=11&interval_id=100:90&action=">剧情</a></span>
<span><a href="/typerank?type_name=喜剧&type=24&interval_id=100:90&action=">喜剧</a></span>
<span><a href="/typerank?type_name=动作&type=5&interval_id=100:90&action=">动作</a></span>
<span><a href="/typerank?type_name=爱情&type=13&interval_id=100:90&action=">爱情</a></span>
<span><a href="/typerank?type_name=科幻&type=17&interval_id=100:90&action=">科幻</a></span>

"""
import re
re_bds0 = '<a href="/typerank.*?type=(.*?).*?>(.*?)</a>'
re_bds1 = '<a href="/typerank.*?type=(.*?)&.*?>(.*?)</a>'

pattren = re.compile(re_bds0)
r = pattren.findall(html)
print(r)

pattren = re.compile(re_bds1)
r1 = pattren.findall(html)
print(r)