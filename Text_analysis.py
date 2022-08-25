# -*- encoding:utf-8 -*-
import csv
import os
import re
from itertools import zip_longest

from lxml import etree

'''
# no need
# 保存当事人信息到csv函数
def savelist(film_content):
    with open('../content/2013_subject_0810_1.csv', 'a+', newline='', encoding='gb18030') as f:
        writer = csv.writer(f)
        writer.writerow(film_content)
    print('保存文件成功')

# 逐行遍历TXT文件中的URL链接
url_list = []
def open_txt():
    with open("url.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            url_list.append(line.replace('\n', ''))

def subjects_list(word):
    # 辅助变量
    subject_1 = ''
    subject_2 = ''
    subject_1_rep = ''
    subject_2_rep = ''
    subject_1_list_true = []
    subject_1_rep_list_true = []
    subject_2_list_true = []
    subject_2_rep_list_true = []
    subject_1_list = []
    subject_1_rep_list = []
    subject_2_list = []
    subject_2_rep_list = []

    # 根据关键词正则提取当事人1、当事人2的信息
    if ('再审申请人' in word):
        obj1 = re.compile(r"再审申请人(.+?)(?=',)", re.S)
        subject_1_list = obj1.findall(word)
        if subject_1_list:
            for i in range(0, len(subject_1_list)):
                subject_1_list_true.append('再审申请人' + str(subject_1_list[i]))
            subject_1 = subject_1_list_true[0]
        obj66 = re.compile(r"再审申请人.*?,(.*?)。", re.S)
        subject_1_rep_list = obj66.findall(word)
        if subject_1_rep_list:
            for i in range(0, len(subject_1_rep_list)):
                subject_1_rep_list_true.append(subject_1_rep_list[i].replace(" \'\\u3000\\u3000", ''))
            subject_1_rep = str(subject_1_rep_list_true[0])
        obj2 = re.compile(r"被申请人(.+?)(?=',)", re.S)
        subject_2_list = obj2.findall(word)
        if subject_2_list:
            for i in range(0, len(subject_2_list)):
                subject_2_list_true.append('被申请人' + str(subject_2_list[i]))
            subject_2 = subject_2_list_true[0]
        obj65 = re.compile(r"被申请人.*?,(.*?)。", re.S)
        subject_2_rep_list = obj65.findall(word)
        if subject_2_rep_list:
            for i in range(0, len(subject_2_rep_list)):
                subject_2_rep_list_true.append(subject_2_rep_list[i].replace(" \'\\u3000\\u3000", ''))
            subject_2_rep = str(subject_2_rep_list_true[0])

    elif ('上诉人' in word):
        obj1 = re.compile(r"3000上诉人\((.+?)(?=', ')", re.S)
        subject_1_list = obj1.findall(word)
        if subject_1_list:
            for i in range(0, len(subject_1_list)):
                subject_1_list_true.append('上诉人(' + subject_1_list[i])
            subject_1 = subject_1_list_true[0]
        obj66 = re.compile(r"3000上诉人\(.*?,(.*?)。", re.S)
        subject_1_rep_list = obj66.findall(word)
        # print(subject_1_rep_list)
        if subject_1_rep_list:
            for i in range(0, len(subject_1_rep_list)):
                subject_1_rep_list_true.append(subject_1_rep_list[i].replace(" \'\\u3000\\u3000", ''))
            subject_1_rep = str(subject_1_rep_list_true[0])
        obj2 = re.compile(r"\\u3000被上诉人\((.+?)(?=',)", re.S)
        subject_2_list = obj2.findall(word)
        if subject_2_list:
            for i in range(0, len(subject_2_list)):
                subject_2_list_true.append('被上诉人' + subject_2_list[i])
            subject_2 = subject_2_list_true[0]
        obj65 = re.compile(r"被上诉人\(.*?,(.*?)。", re.S)
        subject_2_rep_list = obj65.findall(word)
        # print(subject_2_rep_list)
        if subject_2_rep_list:
            for i in range(0, len(subject_2_rep_list)):
                subject_2_rep_list_true.append(subject_2_rep_list[i].replace(" \'\\u3000\\u3000", ''))
            subject_2_rep = str(subject_2_rep_list_true[0])

    elif ('原告：' in word):
        obj1 = re.compile(r"原告：(.+?)(?=',)", re.S)
        subject_1_list = obj1.findall(word)
        if subject_1_list:
            for i in range(0, len(subject_1_list)):
                subject_1_list_true.append('原告：' + str(subject_1_list[i]))
            subject_1 = subject_1_list_true[0].replace("\', \'", '')
        obj66 = re.compile(r"原告：.*?,(.*?)。", re.S)
        # print(word)
        subject_1_rep_list = obj66.findall(word)
        # print(subject_1_rep_list)
        if subject_1_rep_list:
            for i in range(0, len(subject_1_rep_list)):
                subject_1_rep_list_true.append(subject_1_rep_list[i].replace(" \'\\u3000\\u3000", ''))
            subject_1_rep = str(subject_1_rep_list_true[0])
        obj2 = re.compile(r"被告：(.+?)(?=',)", re.S)
        subject_2_list = obj2.findall(word)
        if subject_2_list:
            for i in range(0, len(subject_2_list)):
                subject_2_list_true.append('被告：' + str(subject_2_list[i]))
            subject_2 = subject_2_list_true[0]
        obj65 = re.compile(r"被告：.*?,(.*?)。", re.S)
        subject_2_rep_list = obj65.findall(word)
        # print(subject_2_rep_list)
        if subject_2_rep_list:
            for i in range(0, len(subject_2_rep_list)):
                subject_2_rep_list_true.append(subject_2_rep_list[i].replace(" \'\\u3000\\u3000", ''))
            subject_2_rep = str(subject_2_rep_list_true[0])

    # 当事人1列表去重复
    subject_1_rep_list_true_set = sorted(set(subject_1_rep_list_true), key=subject_1_rep_list_true.index)

    # 使用zip将两个当事人list合并成dict
    subject_1_dict = dict(zip_longest(subject_1_list_true, subject_1_rep_list_true_set))
    subject_2_dict = dict(zip_longest(subject_2_list_true, subject_2_rep_list_true))

    # 辅助打印测试当事人情况
    # print("-------------------")
    # print(subject_1_dict)
    # print(subject_2_dict)
    # print("subject_1"+ subject_1)
    # print("subject_1_list:",str(subject_1_list_true))
    # print("subject_1_rep"+ subject_1_rep)
    # print("subject_1_rep_list",subject_1_rep_list_true_set)
    # print("subject_2"+ subject_2)
    # print("subject_2_list",subject_2_list_true)
    # print("subject_2_rep"+subject_2_rep)
    # print("subject_2_rep_list",subject_2_rep_list_true)

def subject_word_list(word):
    word = word.replace("[\'\\r\\n\\r\\n                \',", '').replace("\\u3000\\u3000", '')
    word_list = []
    word_list = word.split('\',')
    word_list_true = word_list
    for i in range(0, len(word_list)):
        try:
            if word_list[i] in (
                    " \'上诉人(一审被告)：", " \'上诉人（一审被告）：", " \'上诉人（一审被告）:", " \'上诉人（一审原告）", " \'上诉人（一审原告）：", " \'上诉人（原审被告）",
                    " \'上诉人(原审被告)：", " \'上诉人（原审被告）：", " \'上诉人（原审被告）:", " \'上诉人(原审被告):", " \'上诉人（原审原告）", " \'上诉人(原审原告)",
                    " \'上诉人(原审原告)：", " \'上诉人（原审原告）：", " \'上诉人（原审原告）:", " \'申请人", " \'申请人：", " \'原告", " \'原告（反诉被告）：",
                    " \'原告：", " \'原告:", " \'原告: ", " \'再审申请人（一审被告、二审被上诉人）：", " \'再审申请人（一审被告、二审上诉人）：",
                    " \'再审申请人（一审原告、二审上诉人）："):
                word_list_true[i] = (word_list[i] + word_list[i + 1]).replace(" \'", '')
                word_list_true.remove(word_list[i + 1])
            if word_list_true[i] in (" \'当事人"):
                word_list_true.remove(" \'当事人")
            if word_list_true[i] in (" \'"):
                word_list_true.remove(" \'")
        except:
            continue
    word_list_true.insert(0, code)
    word_list_true.insert(1, word)
    # print(word_list_true)
'''

# needed
# TODO 修改文件保存名称
def save(film_content):
    with open('../test_file/2013_test4_0825.csv', 'a+', newline='', encoding='gb18030') as f:
        writer = csv.writer(f)
        writer.writerow(film_content)
    print('保存文件成功')

# 循环遍历本地文件夹中的HTML
def get_html():
    path = 'html_2013'
    all_html = os.listdir(path)
    os.chdir(path)
    return all_html


def judge_first(text):
    # 落款中的审判长 judge_first
    judges_first = ''
    if ("二〇") in text:
        obj_9 = re.compile("(?<=判决如下)(.+?)(?=二〇)", re.S).findall(text)
    else:
        obj_9 = re.compile("(?<=判决如下)(.+?)(?=二○)", re.S).findall(text)
    if ("审 判 长") in str(obj_9):
        if ("人民陪审员") in str(obj_9):
            obj_10 = re.compile(r"(?<=审 判 长)(.+?)(?=人民陪审员)", re.S).findall(str(obj_9))
            judges_first = ''.join(obj_10).replace("\\u3000", '').replace(' ', '').replace(
                "<>style=\"font-family:仿宋;font-size:15pt;-aw-import:spaces\">", '')
        else:
            obj_10 = re.compile(r"(?<=审 判 长)(.+?)(?=审 判 员)", re.S).findall(str(obj_9))
            judges_first = ''.join(obj_10).replace("\\u3000", '').replace(' ', '').replace(
                "<>style=\"font-family:仿宋;font-size:15pt;-aw-import:spaces\">", '')
    elif ("审判长") in str(obj_9):
        if ("人民陪审员") in str(obj_9):
            obj_10 = re.compile(r"(?<=审判长)(.+?)(?=人民陪审员)", re.S).findall(str(obj_9))
            judges_first = ''.join(obj_10).replace("\\u3000", '').replace(' ', '').replace(
                "<>style=\"font-family:仿宋;font-size:15pt;-aw-import:spaces\">", '')
        else:
            obj_10 = re.compile(r"(?<=审判长)(.+?)(?=审判员)", re.S).findall(str(obj_9))
            judges_first = ''.join(obj_10).replace("\\u3000", '').replace(' ', '').replace(
                "<>style=\"font-family:仿宋;font-size:15pt;-aw-import:spaces\">", '')
    elif ("审 判 长" or "审判长") not in str(obj_9):
        if ("审判员") in str(obj_9):
            obj_10 = re.compile(r"(?<=审判员 )(.+?)(?= '\])", re.S).findall(str(obj_9))
            judges_first = ''.join(obj_10).replace("\\u3000", '').replace(' ', '').replace(
                "<>style=\"font-family:仿宋;font-size:15pt;-aw-import:spaces\">", '')
        elif ("审 判 员") in str(obj_9):
            obj_10 = re.compile(r"(?<=审 判 员 )(.+?)(?= '\])", re.S).findall(str(obj_9))
            judges_first = ''.join(obj_10).replace("\\u3000", '').replace(' ', '').replace(
                "<>style=\"font-family:仿宋;font-size:15pt;-aw-import:spaces\">", '')
    return judges_first


def court_province_city(court):
    # 提取法院的基本信息，court_level 法院级别；province 法院省份； city 法院城市
    court_level = ''  # 法院级别
    province = ''  # 法院省份
    city = ''  # 法院城市

    try:
        if ("最高" in court):
            court_level = '最高'
            province = '空'
            city = '空'
        elif ("高级" in court):
            court_level = '高级'
            if ("省" in court):
                province = court.split('省')[0] + '省'
                if ("市" in court):
                    city = court.split("省")[1].split('市')[0] + '市'
                else:
                    city = '空'
            elif ("自治州" in court):
                province = court.split('自治州')[0] + '自治州'
                if ("市" in court):
                    city = court.split("自治州")[1].split('市')[0] + '市'
            elif ("市" in court):
                province = court.split('市')[0] + '市'
                city = '空'
            else:
                city = '空'
                province = '空'
        elif ("中级" in court):
            court_level = '中级'
            if ("省" in court):
                province = court.split('省')[0] + '省'
                if ("市" in court):
                    city = court.split("省")[1].split('市')[0] + '市'
            elif ("自治州" in court):
                province = court.split('自治州')[0] + '自治州'
                if ("市" in court):
                    city = court.split("自治州")[1].split('市')[0] + '市'
            elif ("市" in court):
                province = court.split('市')[0] + '市'
                city = '空'
            else:
                city = '空'
                province = '空'
        elif ("知识产权" in court):
            court_level = '专门'
            city = '空'
            province = '空'
        elif ("区" or "县" in court):
            court_level = '基层'
            if ("省" in court):
                province = court.split('省')[0] + '省'
                if ("市" in court):
                    city = court.split("省")[1].split('市')[0] + '市'
            elif ("自治州" in court):
                province = court.split('自治州')[0] + '自治州'
                if ("市" in court):
                    city = court.split("自治州")[1].split('市')[0] + '市'
            elif ("市" in court):
                province = court.split('市')[0] + '市'
                city = '空'
            else:
                city = '空'
                province = '空'


        else:
            court_level = ''
            city = '空'
            province = '空'
    except:
        pass
    return court_level, province, city

# def yuangao_beiago(word):


# 全局变量
items = []
num_select = 10
all_html = get_html()

# 循环遍历，用enumerate()记录个数
for num_text, html in enumerate(all_html):

    # 定义所有用到的字段
    # year = '2019' # TODO 修改年份2013/2019
    year = '2013'  # TODO 修改年份2013/2019
    # code = '' #法宝引证码
    # title = '' #判决书名称
    # case_no = ''  #案号
    url = ''  # 原文链接 href

    case_reason = ''  # 案由
    case_type = ''  # 案件类型
    proceeding = ''  # 审理程序：只要一审和简易程序
    instrument_type = ''  # 文书类型
    keywords = ''  # 权责关键词

    completion_date = ''  # 审结日期
    start_date = ''  # 受理日期

    judges = ''  # 全部审判法官（第1个为审判长）
    # judges_first = '' #审判长
    law_firms = ''  # 代理律师/律所

    legal_count = ''  # 法律依据条数
    legal = ''  # 法律依据列表

    court = ''  # 审理法院
    court_level = ''  # 法院级别
    province = ''  # 法院省份
    city = ''  # 法院城市

    text = '' #完整的正文文本

    word = ''  # 当事人文本
    yuangao = ''  # 第1个原告
    beigao = ''  # 第1个被告
    yuangao_list = []  # 原告列表
    beigao_list = []  # 被告列表

    case_result = ''  # 判决结果文本
    shouli_fee = ''  # 受理费用
    fee_yuangao = ''  # 原告承担受理费
    fee_beigao = ''  # 被告承担受理费

    # HTML文本
    e = etree.parse(html, etree.HTMLParser())
    # print(e)

    # 完整的正文文本 text
    text = e.xpath("//div[@class='fulltext']//text()")
    text = " ".join(text).strip()

    # 法宝引证码code
    code = e.xpath("//div[@class='logo']/div/text()")
    code = "".join(code)

    # 判决书名称title
    title = e.xpath("//div/h2/text()")
    title = "".join(title).strip()

    # 案号 case_no
    try:
        case_no = e.xpath("//div[@class='fields']/ul[1]//li//@title")[1]
        if case_no == '法宝订阅':
            case_no = e.xpath("//div[@class='fields']/ul[1]//li//@title")[2]
        if case_no == '法宝订阅':
            case_no = e.xpath("//div[@class='fields']/ul[1]//li//@title")[3]
    except:
        continue

    # 原文链接 href
    url = e.xpath("//div[@class='link']/a/@href")
    url = "".join(url)

    # 案由 case_reason 
    case_reason = e.xpath("//div[@class='fields']/ul/li[@class='row'][1]/div[@class='box']/a/text()")
    case_reason = "".join(case_reason)

    # 受理日期 start_date
    obj11 = re.compile(r"(?<=本院于)(.+?)(?=后)", re.S)
    obj111 = str(obj11.findall(text))
    obj12 = re.compile(r"\d{4}年\d{1,2}月\d{1,2}日", re.S)
    start_date_list = obj12.findall(obj111)
    if start_date_list:
        start_date = start_date_list[0]

    # 解析HTML页面：当事人+法律依据相关字段
    if e.xpath("//div[@class='fields']/ul//li[1]//text()"):
        # 法律依据legal，法律依据条数legal_count
        legal = e.xpath("//div[@class='correlation-info'][1]/ul/li/a/text()")
        legal = "".join(legal).replace('\r\n', '').replace('侵权责任法 ', '侵权责任法').replace(') ', ')').split()
        legal_count = len(legal)
        legal = ";".join(legal)

        # 当事人，当事人完整字段 word
        text = e.xpath('//div[@id="divFullText"]//text()')
        wor = str(text)
        word = wor.split('审理经过')[0].strip()
        word = str(word)

    #  case_result 完整判决结果文本
    if ('落款' in wor):
        obj4 = re.compile("判决如下(.*?)落款", re.S)
        result_1 = obj4.findall("".join(text))
    else:
        obj4 = re.compile("判决如下(.*?)二〇", re.S)
        result_1 = obj4.findall("".join(text))
    case_result = ''.join(result_1).replace("'", "").replace("\\u3000", "").replace(',', '').strip()

    # 方框中的基本信息
    try:
        for i in range(2, 13):
            contant = e.xpath(f"//div[@class='fields']/ul//li[{i}]//text()")
            data = "".join(contant).split()[0]
            if data == '审理法官：':
                judges = "".join(contant).split()[1::]
                judges = ",".join(judges)
                # 如果judges为空，就用judges_first替代
                if judges == "":
                    judges = judge_first(text)
            elif data == '文书类型：':
                instrument_type = "".join(contant).split()[1]
            elif data == '审理法院：':
                court = "".join(contant).split()[1]
                # 提取法院的基本信息，court_level 法院级别；province 法院省份； city 法院城市
                court_level, province, city = court_province_city(court)
                # 进一步判断知识法院
                if court == "上海知识产权法院":
                    province = "上海市"
                elif court == "北京知识产权法院":
                    province = "北京市"
                elif court == "广州知识产权法院":
                    province = "广东省"
                    city = "广州市"
            elif data[0:5:] == '审结日期：':
                completion_date = data[5::]
            elif data == '案件类型：':
                case_type = "".join(contant).split()[1]
            elif data == '审理程序：':
                proceeding = "".join(contant).split()[1]
            elif data == '代理律师/律所：':
                law_firms = "".join(contant).split()[1::]
                law_firms = ",".join(law_firms).replace(',,', '').replace(',;', '')
            elif data == '权责关键词：':
                keywords = "".join(contant).split()[1::]
                keywords = ",".join(keywords)


        # if(proceeding == '一审' or proceeding == '简易程序'):

        # TODO 原告被告提取函数

        # TODO 审理费用提取函数

        # # 经济赔偿损失，原告与被告负担情况
        # obj_1 = re.compile(r"(?<=[一|二|三|四|五|六|七|八|九|十]、)(?=被告)(.+?)(?=[于本判决|应于本判决])", re.S).findall(case_result)
        # if obj_1:
        #     eco_fee_beigao = ''.join(str(obj_1[0])).replace("被告", '')
        # obj_2 = re.compile(r"(?<=赔偿原告)(.+?)(?=经济损失)", re.S).findall(case_result)
        # eco_fee_yuangao = ''.join(obj_2)
        # obj_3 = re.compile(r"(?<=十日内赔偿原告)(.+?)(?=元)", re.S).findall(case_result)
        # obj_4 = re.compile(r"\d+\.?\d*", re.S).findall(str(obj_3))
        # eco_fee = ''.join(obj_4)

        # 受理费
        # shouli_fee_all = re.compile(r"(?<=[负担|承担|费|费用|计|共计|开支|支出|人民币])(\d+\.?\d*)[元|万]", re.S).findall(case_result)

        # 保存字段
        item = [year, code, title, case_no, url,
                case_reason, case_type, proceeding, instrument_type, keywords,
                completion_date, start_date, judges, law_firms, legal_count, legal,
                court, court_level, province, city,
                text, word, yuangao, beigao, yuangao_list, beigao_list,
                case_result, shouli_fee, fee_yuangao, fee_beigao]
        print(f"第{num_text + 1}个爬取成功,titile是{title}")
        save(item)
    except:
        item = [year, code, title, case_no, url,
                case_reason, case_type, proceeding, instrument_type, keywords,
                completion_date, start_date, judges, law_firms, legal_count, legal,
                court, court_level, province, city,
                text, word, yuangao, beigao, yuangao_list, beigao_list,
                case_result, shouli_fee, fee_yuangao, fee_beigao]
        print(f"第{num_text + 1}个爬取成功,titile是{title}")
        save(item)
        pass
