# EPS

从 eps 文件中获取图表的信息，目前支持：

* `*柱状图*.eps`
* 更多图表进行中……


```sh
pip install https://github.com/lwzm/eps/archive/master.zip
```

```python
import eps

data = eps.parse('123柱状图示例.eps')
```
