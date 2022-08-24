# 文件说明

* `html_2013`和`html_2019`是已经爬取下来的判决书HTML文本，分别代表2013年和2019年的商标法。
* `Text_analysis.py`：对所爬取的判决书文本做文本分析，抽取其中所需要字段的程序。
* `Selenium_pkulaw.py`：对北大法宝网站进行selenium模拟点击下载HTML文本的程序。

# TODO

`Text_analysis.py`：

* 说明
  * 以`html_2013`和`html_2019`为样本做文本分析，所提取字段见`all_一审&简易_0823.xlsx`；[此文件中AG列之后的数据现暂不需要，可以删除]
  * `html_2013`中的文本year为2013；`html_2019`中的文本year字段为2019；
  * 由于原告被告以及受理费的各种说法不一致，这里只抽取`proceeding审理程序`字段中为一审或简易程序的案例数据进行`原告yuangao`、`被告beigao`以及 审理费相关信息的分析。

* TODO

- [ ]  提取原告yuangao和被告beigao字段
- [ ]  提取关于审理费的相关信息，最好是能直接有三个变量：审理费总额，原告负担金额，被告负担金额。[如果不能精确的提取，可以先把关于审理费的整句提取出来]
- [ ] 由于后续还有更多的文本需要使用此程序做文本分析，需要做代码重构，e.g.比如封装成函数，以及可以看到`all_一审&简易_0823.xlsx`中有些字段是空的，需要完善。

----

`Selenium_pkulaw.py`

* 说明
  * 本程序用于爬取「引用2013商标法63条的一审判决书」，由于有多个页面，设置了根据年份和省份的循环下载。

* TODO

- [ ] 进行滑块验证的时候会==下载中断==，出现提示框「请选择要下载的文本」。目标需要让其可以在服务器上不中断运行。目前不知道问题在哪里，导致每次中断后都需要重新运行程序，修改页码。

- [ ] 代码效率很低，导致爬取的时候很慢，看能否加入多线程/进程爬取，或者重构代码让其爬取得更快。

- [ ] 每次下载的zip文件分不清是哪一页面的下载内容，比如需要重命名下载的文件以识别下载到哪里了。

- [ ] 目前程序只爬取了「一审判决书」，需要加入对「简易程序判决书」（在页面左边可以点击选择）的爬取。看是否能够使用循环爬取。

  
