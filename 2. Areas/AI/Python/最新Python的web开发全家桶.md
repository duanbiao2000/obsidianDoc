---
typora-copy-images-to: ./
---

## 1.4 字符串类型

```javascript
//声明
var name = "搞钱";
var name = String("搞钱");
```

```JavaScript
//常见功能
var name = "中国联通";

var v1 = name.length;
var v2 = name[0];    //name.charAt(0)
var v3 = name.trim();
var v4 = name.substrim(1,2);  //前取后不取
```

### 案例:跑马灯

## 1.5数组

```javascript
//定义
var v1 = [11,22,33,44];
var v2 = Array([11,22,33,44]);
```

```javascript
//操作
var v1 = [11,22,33,44];
v1[1]
v2[0] = "高倩";

v1.push("联通");   //尾部追加[11,22,33,44,"联通"]
v1.unshift("联通"); //首部追加["联通",11,22,33,44]
v1.splice(1:索引,0,"中国":元素)	//指定位插入[11,"中国",22,33,44] 中间的参数0表示删除项目数,为0表示不删除

v1.pop()	//尾部删除
v1.shift()	//头部删除
v1.splice(2,1); //索引为2的元素删除  [11,22,44]
```

```javascript
var v1 = [11,22,33,44];
for(var idx in v1){
  //idx=0/1/2/3/ 	data=v1[idx]    //遍历的是索引
}
```

```javascript
var v1 = [11,22,33,44];
for(var i=0;i<v1.length;i++){
  //idx=0/1/2/3/ 	data=v1[idx]    //遍历的是索引
}
```

注意: 也有break和continue关键字



案例:动态数据

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<ul id="city">
    <!--<li>北京</li>-->
</ul>
<script type="text/javascript">

    //通过网络请求,获取数据
    var cityList = ["北京", "上海", "深圳"];
    for (var idx in cityList) {
        var text = cityList[idx];

        //创建<li></li>
        var tag = document.createElement("li");
        //在li标签中写入内容
        tag.innerText = text;

        //添加到id=city那个标签里面. DOM
        var parentTag = document.getElementById("city");
        parentTag.appendChild(tag)
    }
</script>
</body>
</html>
```

##1.6对象(python里字典)

```javascript
info = {
  "name":"段彪",
  "age":18
}

//方式2
info = {		
  name:"段彪2",
  age:18
}
```

```javascript
info.age	//读取
info.name = "郭智"	//设置

info["age"]
info["name"] = "郭智"

delete info["age"]
```

```javascript
//循环
info = {
  "name":"段彪",
  "age":18
}

for(var key in info){
  // 键:key=name/age   值:data=info[key]
}
```

### 动态表格

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<table>
    <thread>
        <tr>
            <th>ID</th>
            <th>姓名</th>
            <th>年龄</th>
        </tr>
    </thread>
    <tbody id="body">
    <!--        <tr>-->
    <!--            <td>1</td>-->
    <!--            <td>郭智</td>-->
    <!--            <td>19</td>-->
    <!--        </tr>-->
    </tbody>
</table>

<script type="text/javascript">
    var datalist = [
        {id: 1, name: "郭智", age: 19},
        {id: 2, name: "郭智", age: 19},
        {id: 3, name: "郭智", age: 19},
        {id: 4, name: "郭智", age: 19},
        {id: 5, name: "郭智", age: 19},
    ];
    for (var idx in datalist) {
        var info = datalist[idx];
        var tr = document.createElement("tr")
        for (var key in info) {
            var text = info[key];
            var td = document.createElement('td');
            td.innerText = text;
            tr.appendChild(td);
        }

        var bodyTag = document.getElementById("body");
        bodyTag.appendChild(tr);
    }

</script>
</body>
</html>
```

![1680170209401](1680170209401.png)

### 1.7条件语句

```javascript
if(条件){
  
}else{
  
}

if(1==1){
  
}else if{
  
}else{
  
}
```

### 1.8函数

```javascript
function func(){
  	...	
}

func()
```

# 2.DOM

DOM,就是一个模块,模块可以对HTML页面中的标签进行操作.

```javascript
//根据ID获取标签
var tag = document.getElementById("xx");

//获取标签中的文本
tag.innerText

//设置标签中的文本
tag.innerText = "早学早托生"

//创建标签<div>哈哈哈<div>
var tag = document.createElement("div");

//标签写内容
tag.innerText = "哈哈哈";
```



```html
<ul id="city">
  <li>北京</li>  //由下面代码动态创建生成
</ul>

<script type="text/javascript">
	var tag = document.getElementById("city");
	//<li>北京</li>
	var newTag = document.createElement("li");
	newTag.innerText = "北京";
	tag.appendChild(newTag);
</script>
```

## 2.1事件的绑定

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  	//onclick事件绑定函数addCityInfo()
    <input type="button" value="点击添加" onclick="addCityInfo()">
    <ul id="city">

    </ul>
    <script type="text/javascript">
        function addCityInfo(){
            var newTag = document.createElement("li");
            newTag.innerText="联通";

            var parentTag = document.getElementById("city");
            parentTag.appendChild(newTag);
        }
    </script>
</body>
</html>
```

![1680172963476](1680172963476.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<!--    消除"Missing associated label"警告-->
    <label for="txtUser"></label>
    <input type="text" placeholder="请输入内容" id="txtUser">
    <input type="button" value="点击添加" onclick="addCityInfo()">
    <ul id="city">

    </ul>
    <script type="text/javascript">
        function addCityInfo() {
            //1.先获取输入框中用户输入的数据
            let txtTag = document.getElementById("txtUser")
            //2.获取input框中用户输入的内容
            let newString = txtTag.value;
            //2.1判断用户输入是否为空
            if (newString.length > 0) {
                //3.创建标签 <li></li> 中间的文本信息就是用户输入的内容
                let newTag = document.createElement("li");
                newTag.innerText = newString;

                let parentTag = document.getElementById("city");
                parentTag.appendChild(newTag);
            }else{
                alert("输入不能为空")
            }
        }
    </script>
</body>
</html>
```



![1680176649217](1680176649217.png)

注意:DOM中还有很多操作.

```
DOM可以实现很多功能,但比较繁琐.页面上的效果: jQuery / vue.js / react.js 来实现
```

# 3.知识点回顾

-   编码相关

    ```
    文件存储时,使用某种编码,打开时要使用相同的编码,否则就会乱码.
    字符底层存储时本质上都是0101001010101001001010000100 . 
    字符和二进制的对应关系(编码):
    	- ASCII编码,256中对应关系
    	- GB312,GBK,中文和亚洲国家[中文2个字节]
    	- unicode, ucs2/ucs4,包括现在发现的所有文明.
    	- utf-8编码, [一般中文占用3个字节]
    python默认解释器编码(utf-8):
    	python.exe 
    	
    	如果你将代码文件保存成了gbk编码,将python模式解释器编码修改为gbk.
    ```

```python
data1 = "中"
res1 = data1.encode('utf-8')
print(f"res1:{res1},占用{len(res1)}字节")

data2 = "国"
res2 = data2.encode('gbk')
print(f"res2:{res2},占用{len(res2)}字节")

```

```
res1:b'\xe4\xb8\xad',占用3字节
res2:b'\xb9\xfa',占用2字节
```

-   字符串格式化(三种)

    ```python
    v1 = "我是{},今年{}".format("武沛齐","77")
    v2 = "我是%s,今年%d岁" %("武沛齐","77")

    v3=f"我是{name},今年 {age}岁"
    ```

-   数据类型

    ```python
    常见数据类型: int,bool,str,list,tuple,dict,set,float,None
    	- 哪些转化成布尔值为False: 空, None,0
    	- 可变和不可变划分,可变有哪些? list,dict,set
    	- 可哈希和不可哈希,不可哈希有哪些? list,dict,set(同可变)
    	- 字典的键/集合的元素,必须是可哈希的类型(list,set,dict不能做字典的键和集合元素)
    主要数据类型:
      -str
      		- 独有功能:upper/lower/startswith/split/strip/join
          	注意:str不可变,不会对原字符串进行修改,新的内容.
            - 公共功能: len / 索引 / 切片 /for循环 / 判断是否包含
      -list
    		- 独有: append / insert / remove / pop
      		注意: list可变,功能很多都是对原数据操作.
            - 公共: len / 索引 / 切片 /for循环 / 判断是否包含
      -dict
    		- 独有: get / keys / items / value
            - 公共: len / 索引for循环 / 判断是否包含(判断键效率很高)  
    ```

    -   运算符

        ```python
        基本运算符: 加减乘除

        一般:
            1>2 and 3<10
        特殊的逻辑运算:
            v1 = 99 and 88  # v1 = 88, 因为99为true,所以and运算结果将取决于后值
            v2 = [] or 10  # v2 = 10, 因为[]等于false,所以or运算结果仍取决后值
            v3 = "联通" or [] # "联通"
        ```

-   推导式(简化生成数据)


```python
data = []
for i in range(10)
	data.append(i)
    
data = [ i for i in range(10) ]
data = [ i for i in range(10) if i <5 ]
```

-   函数编程

```python
函数的基础知识
	- 定义
    - 参数,概念: 位置传参/关键字传参/参数默认值/动态参数*args,**kwargs
    - 返回值
    	- 函数中一旦遇到return就立即返回,后续代码不再执行.
        - 函数没有返回值默认返回None
函数的进阶:
    - Python中以函数作为作用域
    - 全局变量和局部变量,规范:全局变量(大写),局部变量(小写)
    - 在局部变量中可以使用global关键字,global的作用? 引用全局的变量(不是在局部新建)
    
内置函数: (python内部提供的函数):
    - bin/hex/odc/max/min/divmod/sorted/open文件操作
文件操作:
    - 基本操作: 打开,操作,关闭,为防止忘记关闭文件,可以怎么做? with
    - 打开文件时有模式
    	- r/rb, 读 [文件(夹)不存在,报错]
        - w/wb, 写 [文件不存在,自动新建]
        - a/ab, 追加[文件不存在,自动新建]
        注意: os.makedirs/os/path.exsits 是否存在,不存在新建目录.
```

-   模块

```python
模块的分类:
    - 自定义模块
    	-os.path 导入模块时python内部都会去那个目录找
        -自己写py文件时,不要与python内置模块同名
        -import/from xx import xx
    - 内置模块: time/datetime/json/re/random/os
    - 第三方模块:requests/openpyxl/python-docx/flask/bs4
查看当前目录下所有的文件: os.listdir / os.walk
关于时间模块: 时间戳/datetime格式/字符串,三种时间格式可以相互转化
关于JSON模块: JSON本质就是字符串, (有一些自己格式的要求)只能序列化python常用数据类型

  python    	json  
  dict      	object
  list,tuple	array 
  str       	string
  int,float 	number
  TRUE      	TRUE  
  FALSE     	FALSE 
  None      	null  


re正则模块:
    - 正则: \d \w
    - 贪婪(默认)和非贪婪匹配. 不贪婪加?
    - re.search/re.match/re.findall
        
```

-   面向对象

    ```python
    目标:不是为了用面向对象编程(推荐使用函数编程,面向对象要看得懂)
    面向对象三大特性: 封装,继承,多态
    ```

-   前端开发

    ```html
    - 前端知识分三部分:
    	- HTML, 标签具有模式特点
    	- CSS, 修改标签的特点
    	- Javascript, 动态
    - HTML标签
    	- div/span/a/img/input/form/table/ul...
    	- 块级和行内标签,例如:div span默认谁是块级标签? div
    		注意:css样式,发现行内 
    ```



JQUERY

$(this) //当前点击的标签

$(this).parent().parent().remove

//当页面框架加载完成之后

案例:

<table border="1">



<table>

# 5.前端整合

-   HTML
-   CSS
-   JavaScript, jQuery
-   Bootstrap

## 案例:添加数据页面

>   人员信息录入功能,需要提供用户信息:
>
>   用户名,年龄,薪资,部门,入职时间(*)
>
>   对于时间的选择:不能输入  选择:(插件) datetimepicker
>
>   -   下载插件
>   -   应用插件

# 总结

1.  了解HTML标签,标签结构,基于它可以实现简单的页面.
2.  CSS 了解基本样式;在别人模板的基础上改就可以
3.  JavaScript,jQuery,了解基本使用
    -   时间绑定/寻找标签/操作标签
    -   导入现成插件

后续开发过程中,对于前端就是在BootStrap的基础整改

# day14 MySQL

-   Python相关:基础,函数,数据类型,面相,模块
-   前端开发:HTML,CSS,JavaScript,jQuery
-   ​

```mysql
show databases;

create database 数据库名字 DEFAULT CHARSET utf8 COLLATE utf8_general_ci;

drop database gx_day14

use dabase(数据库名称);

show tables;


create table tb1(
  id int,
  name varchar(16),
  age int
) default charset=utf8;
```

