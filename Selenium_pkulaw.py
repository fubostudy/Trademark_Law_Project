# -*- coding: utf-8 -*-
import base64
import io
import random
import re
import time
import cv2
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lxml import etree
from itertools import zip_longest
import string
# selenium用法参考：http://t.csdn.cn/J2DNs

class qjh(object):

    # 全局变量
    max_page = 200

    '''chrome driver'''
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        # chrome_option.add_argument('--headless') # 设置chrome浏览器无界面模式，使用个人账号时可以使用，使用IP登录时不能使用
        # chromedriver不同版本下载地址：https://chromedriver.storage.googleapis.com/index.html
        self.driver = webdriver.Chrome(executable_path=r"/Users/fubo/Desktop/Git/spider_new/chromedriver", chrome_options=chrome_option)
        self.driver.set_window_size(1440, 900)

    ''' ip登录函数 '''
    def Login_ip(self,account,password):
        # carsi = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="zocial-carsi"]')))
        # self.driver.execute_script("arguments[0].click();", carsi)
        # time.sleep(1)
        # dianji_s =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "idpForm"] / div[3] / div[2] / div / div / div / div[1] / div[20] / a')))
        # self.driver.execute_script("arguments[0].click();", dianji_s)
        # dianji_szu =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '// *[ @ id = "idpForm"] / div[3] / div[3] / div[1] / div / div / ul / li[55]')))
        # self.driver.execute_script("arguments[0].click();", dianji_szu)
        # denglu1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="idpSkipButton"]')))
        # self.driver.execute_script("arguments[0].click();", denglu1)
        # time.sleep(2)
        zhanghao1 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="username"]')))
        zhanghao1.send_keys(account)
        mima1 = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
        mima1.send_keys(password)
        denglu2 = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "casLoginForm"] / p[5] / button')))
        self.driver.execute_script("arguments[0].click();", denglu2)
        time.sleep(1)

    ''' 律协账户登录函数 '''
    def Login_association(self,account,password):
        # 输入账号
        zhanghao = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email-phone"]')))
        zhanghao.send_keys(account)
        # 输入密码
        mima = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
        mima.send_keys(password)
        time.sleep(1)
        # 点击登录
        denglu = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="btn-submit"]')))
        denglu.click()
        time.sleep(1)

    '''2013年，点击一审和法宝推荐之后，进行筛选页面'''
    def to_filter_page(self):
        # 滑动到底部，进行加载
        js_button = 'document.documentElement.scrollTop=100000'
        self.driver.execute_script(js_button)
        # 点击一审 //*[@id="TrialStepport_1_span"]
        yishen_2013 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="TrialStepport_1_span"]')))
        self.driver.execute_script("arguments[0].click();", yishen_2013)
        time.sleep(3)
        # 点击法宝推荐 //*[@id="CaseGradeport_12_span"] //*[@id="CaseGradeport_12_span"]
        tuijian_2013 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="CaseGradeport_12_span"]')))
        self.driver.execute_script("arguments[0].click();", tuijian_2013)
        time.sleep(3)

    '''
    def get_year2022_2013(self):
        # 点击年份 
        year2022_2013 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "LastInstanceDateport_1_span"]')))
        self.driver.execute_script("arguments[0].click();", year2022_2013)
        time.sleep(3)
        # 滑动到底部
        js_button = 'document.documentElement.scrollTop=100000'
        self.driver.execute_script(js_button)
        time.sleep(3)
        # 点击更多
        more = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "rightContent"] / div / div / div[4] / a')))
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(3)

    def get_year2021_2013(self):
        # 点击年份 TODO 修改为循环
        year2022_2013 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "LastInstanceDateport_2_span"]')))
        self.driver.execute_script("arguments[0].click();", year2022_2013)
        time.sleep(3)
        # 滑动到底部
        js_button = 'document.documentElement.scrollTop=100000'
        self.driver.execute_script(js_button)
        time.sleep(3)
        # 点击更多
        more = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "rightContent"] / div / div / div[4] / a')))
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(3)
    '''
    '''根据年份进行爬取 ''' # TODO 修改为循环  0822更新：2022、2021已爬取完成
    # 等待时间需比较长（3s），不然会跳转页面错误
    # 年份的Xpath是固定的，只是修改1、2、3；更多所在的Xpath的div可能会变化，此处2020为div[6]，2021/2022都为div[4]
    def get_year2020_2013(self):
        # 点击年份
        year2022_2013 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "LastInstanceDateport_3_span"]')))
        self.driver.execute_script("arguments[0].click();", year2022_2013)
        time.sleep(4)
        # 滑动到底部
        js_button = 'document.documentElement.scrollTop=100000'
        self.driver.execute_script(js_button)
        time.sleep(4)
        # 点击更多
        more = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "rightContent"] / div / div / div[6] / a')))
        self.driver.execute_script("arguments[0].click();", more)
        time.sleep(4)

    def get_by_province(self):
        # 滑动到底部
        js_button = 'document.documentElement.scrollTop=100000'
        self.driver.execute_script(js_button)
        time.sleep(3)
        # 点击省份的更多 //*[@id="leftContent"]/div[1]/div[6]/div/div/a
        more_province = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '// *[ @ id = "leftContent"] / div[1] / div[6] / div / div / a')))
        self.driver.execute_script("arguments[0].click();", more_province)
        # 获取省份列表
        get_province = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="leftContent"]/div[1]/div[6]/div/ul')))
        province_html = etree.HTML(get_province.get_attribute('innerHTML'))  # 使用etree变成lxml格式
        province_ret = province_html.xpath("//a/span")
        # 存储为列表并转化为xpath格式
        province_list = []
        province_list_xpath = []  # xpath格式的province
        for i in province_ret:
            province = i.xpath(".//@id")
            province_list.append(province)
        # print(province_list)
        for i in province_list:
            province_list_xpath.append('//*[@id=\"' + str(i).split('[\'')[1].split('\']')[0] + '\"]')
        print(province_list_xpath)
        print('====' * 20)


    '''获取最大页数，用在allpage中'''
    def get_maxpage(self):
        page = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="rightContent"]/div/div/div[3]/ul/li[1]/label')))
        global max_page # 访问全局变量，并修改为当前的最大页
        max_page = int(page.text.split('/')[1]) + 1 # eg 有7页，在range中应该设置为（1，8）
        print("应该设置最大页数是:", max_page)
        return max_page

    '''点击全选下载Html'''
    def download(self):
        # 滑动到页面顶端，防止找不到全选框，解决"请选择要下载的内容"的bug
        js_button = 'document.documentElement.scrollTop=1'
        self.driver.execute_script(js_button)
        time.sleep(1)  # 等待加载
        # 第一步：找到全选框，点击  TODO BUG:请选择要下载的内容
        quanxuan = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//span[@class="choose-all"]/input')))
        self.driver.execute_script("arguments[0].click();", quanxuan)  # 这里总报错，使用js增强工具解决了问题
        # print('全选框点击成功')
        # 第二步：点击批量下载
        qxxz = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@class="down-all"]')))
        self.driver.execute_script("arguments[0].click();", qxxz)
        # print('批量下载点击成功')
        # 第三步：选择html格式
        xzhtml = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@name="batchDownload" and @id = "tool-hyper"]')))
        self.driver.execute_script("arguments[0].click();", xzhtml)
        # print('html格式点击成功')
        # 第四步：点击确定
        djqd = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//a[@id="batchDownload"]')))
        self.driver.execute_script("arguments[0].click();", djqd)
        # print('确定点击成功')

    '''往方框中输入页面并进行跳转'''
    def input_page(self, page):
        # 往方框里输入页码
        input = WebDriverWait(self.driver, 100).until(EC.presence_of_element_located((By.XPATH, '//input[@name="jumpToNum"]')))
        input.send_keys(page)
        print('页码输入成功')
        # 点击确定按钮跳转，需要使用js增强，防止页面丢失
        button = WebDriverWait(self.driver, 100).until(EC.element_to_be_clickable((By.XPATH, '//a[@class="jumpBtn"]')))
        self.driver.execute_script("arguments[0].click();", button)
        print('页面跳转点击成功')
        time.sleep(1)  # 等待加载

    def to_buttom(self):
        js_button = 'document.documentElement.scrollTop=100000'
        self.driver.execute_script(js_button)
        time.sleep(2)

    '''验证滑块'''
    def verify(self):
        # 从第21页开始需要破解滑块。由于滑块不是百分百成功，所以多次尝试
        # print("开始",i,"页滑块")
        for l in range(0,20):
            print('开始处理验证码')
            time.sleep(1)
            cut_image_url, cut_location = self.get_image_url('//div[@class="cut_bg"]')
            print('获取图片1成功')
            cut_image = self.mosaic_image(cut_image_url, cut_location)
            cut_image.save("cut.jpg")
            print('获取图片2成功')
            self.driver.execute_script(
                "var x=document.getElementsByClassName('xy_img_bord')[0];"
                "x.style.display='block';")
            print('js代码处理成功')
            cut_fullimage_url = self.get_move_url('//div[@class="xy_img_bord"]')
            resq = base64.b64decode(cut_fullimage_url[22::])
            file1 = open('2.jpg', 'wb')
            file1.write(resq)
            file1.close()
            res = self.FindPic("cut.jpg", "2.jpg")
            print('获取坐标成功')
            res = res[3][0]  #
            print('开始移动验证码滑块')
            self.start_move(res)
            print('滑块移动结束')
            # 判断验证码是否存在的元素
            time.sleep(0.5)
            try:
                if self.driver.find_element_by_xpath('//div[@class="handler handler_bg"]'): #如果没有了滑块的页面，就说明验证成功，可以跳出循环
                    print('滑块未通过')
                    # 点击刷新
                    self.driver.find_element_by_xpath('//div[@id="drag"]/a/div').click()
                    continue
            except Exception as e:
                break

    # 循环下载
    def loop_zip(self):
        allpage = [int(i) for i in range(1, self.get_maxpage())]
        for page in allpage:
            print("第", page, "页开始下载")
            # try:
            if page == 1:  # 如果是第1页，不用输入，直接下载
                self.download()
                time.sleep(1)
                print("第", page, "页下载成功")
                print('====' * 20)
                continue
            else:
                self.input_page(page)
                # 加一个验证码判断使用异常捕获
                try:
                    if self.driver.find_element_by_xpath('//div[@class="handler handler_bg"]'):
                        self.verify()
                        print('已检测出验证码')
                except Exception as e:
                    print('未触发验证码')
                    pass
                self.download()
            print("第", page, "页下载成功")
            print('====' * 20)
            time.sleep(2)  # 跳转到新页面时等待2s

    # 核心函数  # TODO BUG 会中断
    def core(self):
        # 获取url
        # url = "https://szlx.pkulaw.com/clink/pfnl/chl/7b04747abde51656bdfb/58_0_0_0.html"    # 2013
        # url = "https://szlx.pkulaw.com/clink/pfnl/chl/937235cafaf2a66fbdfb/58_0_0_0.html"  # 2019
        # url = "https://www-pkulaw-com.ezproxy.lib.szu.edu.cn/clink/pfnl/chl/937235cafaf2a66fbdfb/63_0_0_0.html?way=textTiaoFblx" # 2019第63条
        url = "https://www-pkulaw-com.ezproxy.lib.szu.edu.cn/clink/pfnl/chl/7b04747abde51656bdfb/63_0_0_0.html?way=textTiaoFblx"  # 2103第63条
        self.driver.get(url)

        # 登录
        self.Login_ip('293474','2000825b')
        # self.Login_association('sz833298','sz@833298')
        # self.Login_association('sz065955','sz@065955')
        # self.Login_association('sz017654','sz@017654')

        # 所在年份小于2000篇，不需要循环下载
        # self.get_year2022_2013()
        # self.get_year2021_2013()
        # self.get_year2020_2013()
        # TODO self.get_year2014_2013()

        # 所在年份大于2000篇，使用循环下载
        # 通过年份的Xpath列表，循环点击。2019-4,2018-5,2017-6,2016-7,2015-8,(2014少于2000，重新定义函数)
        year_list = ['// *[ @ id = "LastInstanceDateport_4_span"]', '// *[ @ id = "LastInstanceDateport_5_span"]',
                     '// *[ @ id = "LastInstanceDateport_6_span"]', '// *[ @ id = "LastInstanceDateport_7_span"]',
                     '// *[ @ id = "LastInstanceDateport_8_span"]']
        provices_list = [['//*[@id="LastInstanceCourtport_1_span"]', '//*[@id="LastInstanceCourtport_11_span"]',
                          '//*[@id="LastInstanceCourtport_20_span"]', '//*[@id="LastInstanceCourtport_27_span"]',
                          '//*[@id="LastInstanceCourtport_39_span"]', '//*[@id="LastInstanceCourtport_58_span"]',
                          '//*[@id="LastInstanceCourtport_73_span"]', '//*[@id="LastInstanceCourtport_90_span"]',
                          '//*[@id="LastInstanceCourtport_103_span"]', '//*[@id="LastInstanceCourtport_114_span"]',
                          '//*[@id="LastInstanceCourtport_135_span"]', '//*[@id="LastInstanceCourtport_184_span"]',
                          '//*[@id="LastInstanceCourtport_231_span"]', '//*[@id="LastInstanceCourtport_265_span"]',
                          '//*[@id="LastInstanceCourtport_290_span"]', '//*[@id="LastInstanceCourtport_309_span"]',
                          '//*[@id="LastInstanceCourtport_356_span"]', '//*[@id="LastInstanceCourtport_392_span"]',
                          '//*[@id="LastInstanceCourtport_421_span"]', '//*[@id="LastInstanceCourtport_452_span"]',
                          '//*[@id="LastInstanceCourtport_511_span"]', '//*[@id="LastInstanceCourtport_533_span"]',
                          '//*[@id="LastInstanceCourtport_537_span"]', '//*[@id="LastInstanceCourtport_579_span"]',
                          '//*[@id="LastInstanceCourtport_584_span"]', '//*[@id="LastInstanceCourtport_593_span"]',
                          '//*[@id="LastInstanceCourtport_612_span"]', '//*[@id="LastInstanceCourtport_625_span"]',
                          '//*[@id="LastInstanceCourtport_634_span"]', '//*[@id="LastInstanceCourtport_637_span"]',
                          '//*[@id="LastInstanceCourtport_653_span"]', '//*[@id="LastInstanceCourtport_657_span"]'],
                         ['//*[@id="LastInstanceCourtport_1_span"]', '//*[@id="LastInstanceCourtport_12_span"]',
                          '//*[@id="LastInstanceCourtport_19_span"]', '//*[@id="LastInstanceCourtport_28_span"]',
                          '//*[@id="LastInstanceCourtport_37_span"]', '//*[@id="LastInstanceCourtport_56_span"]',
                          '//*[@id="LastInstanceCourtport_75_span"]', '//*[@id="LastInstanceCourtport_86_span"]',
                          '//*[@id="LastInstanceCourtport_105_span"]', '//*[@id="LastInstanceCourtport_118_span"]',
                          '//*[@id="LastInstanceCourtport_133_span"]', '//*[@id="LastInstanceCourtport_183_span"]',
                          '//*[@id="LastInstanceCourtport_230_span"]', '//*[@id="LastInstanceCourtport_263_span"]',
                          '//*[@id="LastInstanceCourtport_289_span"]', '//*[@id="LastInstanceCourtport_310_span"]',
                          '//*[@id="LastInstanceCourtport_354_span"]', '//*[@id="LastInstanceCourtport_389_span"]',
                          '//*[@id="LastInstanceCourtport_420_span"]', '//*[@id="LastInstanceCourtport_449_span"]',
                          '//*[@id="LastInstanceCourtport_518_span"]', '//*[@id="LastInstanceCourtport_542_span"]',
                          '//*[@id="LastInstanceCourtport_548_span"]', '//*[@id="LastInstanceCourtport_590_span"]',
                          '//*[@id="LastInstanceCourtport_597_span"]', '//*[@id="LastInstanceCourtport_606_span"]',
                          '//*[@id="LastInstanceCourtport_609_span"]', '//*[@id="LastInstanceCourtport_630_span"]',
                          '//*[@id="LastInstanceCourtport_648_span"]', '//*[@id="LastInstanceCourtport_653_span"]',
                          '//*[@id="LastInstanceCourtport_656_span"]', '//*[@id="LastInstanceCourtport_665_span"]',
                          '//*[@id="LastInstanceCourtport_669_span"]'],
                         ['//*[@id="LastInstanceCourtport_1_span"]', '//*[@id="LastInstanceCourtport_14_span"]',
                          '//*[@id="LastInstanceCourtport_21_span"]', '//*[@id="LastInstanceCourtport_30_span"]',
                          '//*[@id="LastInstanceCourtport_44_span"]', '//*[@id="LastInstanceCourtport_66_span"]',
                          '//*[@id="LastInstanceCourtport_87_span"]', '//*[@id="LastInstanceCourtport_96_span"]',
                          '//*[@id="LastInstanceCourtport_116_span"]', '//*[@id="LastInstanceCourtport_129_span"]',
                          '//*[@id="LastInstanceCourtport_138_span"]', '//*[@id="LastInstanceCourtport_192_span"]',
                          '//*[@id="LastInstanceCourtport_243_span"]', '//*[@id="LastInstanceCourtport_277_span"]',
                          '//*[@id="LastInstanceCourtport_303_span"]', '//*[@id="LastInstanceCourtport_328_span"]',
                          '//*[@id="LastInstanceCourtport_365_span"]', '//*[@id="LastInstanceCourtport_398_span"]',
                          '//*[@id="LastInstanceCourtport_427_span"]', '//*[@id="LastInstanceCourtport_454_span"]',
                          '//*[@id="LastInstanceCourtport_515_span"]', '//*[@id="LastInstanceCourtport_533_span"]',
                          '//*[@id="LastInstanceCourtport_540_span"]', '//*[@id="LastInstanceCourtport_581_span"]',
                          '//*[@id="LastInstanceCourtport_588_span"]', '//*[@id="LastInstanceCourtport_607_span"]',
                          '//*[@id="LastInstanceCourtport_622_span"]', '//*[@id="LastInstanceCourtport_630_span"]',
                          '//*[@id="LastInstanceCourtport_635_span"]', '//*[@id="LastInstanceCourtport_638_span"]',
                          '//*[@id="LastInstanceCourtport_652_span"]', '//*[@id="LastInstanceCourtport_656_span"]'],
                         ['//*[@id="LastInstanceCourtport_1_span"]', '//*[@id="LastInstanceCourtport_15_span"]',
                          '//*[@id="LastInstanceCourtport_22_span"]', '//*[@id="LastInstanceCourtport_32_span"]',
                          '//*[@id="LastInstanceCourtport_43_span"]', '//*[@id="LastInstanceCourtport_54_span"]',
                          '//*[@id="LastInstanceCourtport_65_span"]', '//*[@id="LastInstanceCourtport_76_span"]',
                          '//*[@id="LastInstanceCourtport_84_span"]', '//*[@id="LastInstanceCourtport_93_span"]',
                          '//*[@id="LastInstanceCourtport_100_span"]', '//*[@id="LastInstanceCourtport_152_span"]',
                          '//*[@id="LastInstanceCourtport_205_span"]', '//*[@id="LastInstanceCourtport_235_span"]',
                          '//*[@id="LastInstanceCourtport_258_span"]', '//*[@id="LastInstanceCourtport_279_span"]',
                          '//*[@id="LastInstanceCourtport_317_span"]', '//*[@id="LastInstanceCourtport_351_span"]',
                          '//*[@id="LastInstanceCourtport_377_span"]', '//*[@id="LastInstanceCourtport_400_span"]',
                          '//*[@id="LastInstanceCourtport_461_span"]', '//*[@id="LastInstanceCourtport_482_span"]',
                          '//*[@id="LastInstanceCourtport_487_span"]', '//*[@id="LastInstanceCourtport_505_span"]',
                          '//*[@id="LastInstanceCourtport_510_span"]', '//*[@id="LastInstanceCourtport_519_span"]',
                          '//*[@id="LastInstanceCourtport_533_span"]', '//*[@id="LastInstanceCourtport_543_span"]',
                          '//*[@id="LastInstanceCourtport_548_span"]', '//*[@id="LastInstanceCourtport_551_span"]',
                          '//*[@id="LastInstanceCourtport_563_span"]', '//*[@id="LastInstanceCourtport_567_span"]'],
                         ['//*[@id="LastInstanceCourtport_1_span"]', '//*[@id="LastInstanceCourtport_17_span"]',
                          '//*[@id="LastInstanceCourtport_23_span"]', '//*[@id="LastInstanceCourtport_33_span"]',
                          '//*[@id="LastInstanceCourtport_41_span"]', '//*[@id="LastInstanceCourtport_56_span"]',
                          '//*[@id="LastInstanceCourtport_63_span"]', '//*[@id="LastInstanceCourtport_72_span"]',
                          '//*[@id="LastInstanceCourtport_82_span"]', '//*[@id="LastInstanceCourtport_91_span"]',
                          '//*[@id="LastInstanceCourtport_106_span"]', '//*[@id="LastInstanceCourtport_156_span"]',
                          '//*[@id="LastInstanceCourtport_201_span"]', '//*[@id="LastInstanceCourtport_235_span"]',
                          '//*[@id="LastInstanceCourtport_254_span"]', '//*[@id="LastInstanceCourtport_271_span"]',
                          '//*[@id="LastInstanceCourtport_304_span"]', '//*[@id="LastInstanceCourtport_329_span"]',
                          '//*[@id="LastInstanceCourtport_350_span"]', '//*[@id="LastInstanceCourtport_381_span"]',
                          '//*[@id="LastInstanceCourtport_431_span"]', '//*[@id="LastInstanceCourtport_457_span"]',
                          '//*[@id="LastInstanceCourtport_462_span"]', '//*[@id="LastInstanceCourtport_475_span"]',
                          '//*[@id="LastInstanceCourtport_478_span"]', '//*[@id="LastInstanceCourtport_489_span"]',
                          '//*[@id="LastInstanceCourtport_498_span"]', '//*[@id="LastInstanceCourtport_503_span"]',
                          '//*[@id="LastInstanceCourtport_510_span"]', '//*[@id="LastInstanceCourtport_515_span"]',
                          '//*[@id="LastInstanceCourtport_528_span"]', '//*[@id="LastInstanceCourtport_531_span"]']]
        # 合并为dict格式
        year_province_dict = dict(zip_longest(year_list, provices_list))
        # print(year_province_dict)
        # for item in x.items():
        #     key = item[0]
        #     value = item[1]

        # 首先进入要可筛选的页面
        self.to_filter_page()
        # 循环点击年份
        for item in year_province_dict.items():
            # 点击年份
            print("***"*40)
            print(item[0],"开始下载")
            year = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,item[0])))
            self.driver.execute_script("arguments[0].click();", year)
            time.sleep(4)
            # 滑动到底部，太长，滑动多2下
            self.to_buttom()
            self.to_buttom()
            time.sleep(1)
            # 点击更多 进行法宝推荐页面。有多重情况，所以多次尝试 //*[@id="rightContent"]/div/div/div[8]/a ；//*[@id="rightContent"]/div/div/div[10]/a
            try:
                more = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rightContent"]/div/div/div[8]/a')))
                self.driver.execute_script("arguments[0].click();", more)
                time.sleep(3)
            except:
                try:
                    more = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rightContent"]/div/div/div[10]/a')))
                    self.driver.execute_script("arguments[0].click();", more)
                    time.sleep(3)
                except:
                    more = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rightContent"]/div/div/div[6]/a')))
                    self.driver.execute_script("arguments[0].click();", more)
                    time.sleep(3)

            # 进入更多年份页面后，循环省份
            for i in item[1]:
                print("***" * 40)
                print(item[0],"----",i, "开始下载")
                province_one = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, i)))
                self.driver.execute_script("arguments[0].click();", province_one)
                time.sleep(3)
                # 获取页面，并下载zip文件
                self.loop_zip()
                # TODO 重命名文件名
                print("***" * 40)
                print(item[0], "----", i, "下载完成")
                # 刷新页面，重新进入筛选
                self.driver.refresh()
                time.sleep(4)
                self.to_filter_page()
                # 点击年份
                year = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, item[0])))
                self.driver.execute_script("arguments[0].click();", year)
                time.sleep(4)
                # 滑动到底部，太长，滑动多2下
                self.to_buttom()
                self.to_buttom()
                # 点击更多 进行法宝推荐页面。有多重情况，所以多次尝试 //*[@id="rightContent"]/div/div/div[8]/a ；//*[@id="rightContent"]/div/div/div[10]/a
                try:
                    more = WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, '//*[@id="rightContent"]/div/div/div[8]/a')))
                    self.driver.execute_script("arguments[0].click();", more)
                    time.sleep(3)
                except:
                    try:
                        more = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[@id="rightContent"]/div/div/div[10]/a')))
                        self.driver.execute_script("arguments[0].click();", more)
                        time.sleep(3)
                    except:
                        more = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[@id="rightContent"]/div/div/div[6]/a')))
                        self.driver.execute_script("arguments[0].click();", more)
                        time.sleep(3)

            print("***" * 40)
            print(item[0], "下载完成")

            # 刷新页面，重新进入筛选
            self.driver.refresh()
            time.sleep(4)
            self.to_filter_page()

    def FindPic(self, target, template):
        """
        找出图像中最佳匹配位置
        :param target: 目标即背景图
        :param template: 模板即需要找到的图
        :return: 返回最佳匹配及其最差匹配和对应的坐标
        """
        target_rgb = cv2.imread(target)
        target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
        template_rgb = cv2.imread(template, 0)
        res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
        value = cv2.minMaxLoc(res)
        return value
    def get_move_url(self, xpath):
        # 得到滑块的位置
        # 需要加一次延时时间
        time.sleep(0.3)
        link = re.compile(
            'background-image: url\("(.*?)"\); ')  # 严格按照格式包括空格
        elements = self.driver.find_elements_by_xpath(xpath)
        image_url = None

        for element in elements:
            style = element.get_attribute("style")
            groups = link.search(style)
            url = groups[1]
            image_url = url
        return image_url
    def get_image_url(self, xpath):
        # 得到背景图片
        link = re.compile(
            'background-image: url\("(.*?)"\); width: 30px; height: 100px; background-position: (.*?)px (.*?)px;')  # 严格按照格式包括空格
        elements = self.driver.find_elements_by_xpath(xpath)
        image_url = None
        location = list()
        for element in elements:
            style = element.get_attribute("style")
            groups = link.search(style)

            url = groups[1]
            x_pos = groups[2]
            y_pos = groups[3]

            location.append((int(x_pos), int(y_pos)))
            image_url = url
        return image_url, location
    # 拼接图片
    def mosaic_image(self, image_url, location):

        resq = base64.b64decode(image_url[22::])
        file1 = open('1.jpg', 'wb')
        file1.write(resq)
        file1.close()
        with open("1.jpg", 'rb') as f:
            imageBin = f.read()
        # 很多时候，数据读写不一定是文件，也可以在内存中读写。
        # BytesIO实现了在内存中读写bytes，创建一个BytesIO，然后写入一些bytes：
        buf = io.BytesIO(imageBin)
        img = Image.open(buf)
        image_upper_lst = []
        image_down_lst = []
        count = 1
        for pos in location:
            if pos[0] > 0:
                if count <= 10:
                    if pos[1] == 0:

                        image_upper_lst.append(img.crop((abs(pos[0] - 300), 0, abs(pos[0] - 300) + 30, 100)))
                    else:
                        image_upper_lst.append(img.crop((abs(pos[0] - 300), 100, abs(pos[0] - 300) + 30, 200)))
                else:
                    if pos[1] == 0:

                        image_down_lst.append(img.crop((abs(pos[0] - 300), 0, abs(pos[0] - 300) + 30, 100)))
                    else:
                        image_down_lst.append(img.crop((abs(pos[0] - 300), 100, abs(pos[0] - 300) + 30, 200)))
            elif pos[0] <= -300:

                if count <= 10:
                    if pos[1] == 0:

                        image_upper_lst.append(img.crop((abs(pos[0] + 300), 0, abs(pos[0] + 300) + 30, 100)))
                    else:
                        image_upper_lst.append(img.crop((abs(pos[0] + 300), 100, abs(pos[0] + 300) + 30, 200)))
                else:
                    if pos[1] == 0:

                        image_down_lst.append(img.crop((abs(pos[0] + 300), 0, abs(pos[0] + 300) + 30, 100)))
                    else:
                        image_down_lst.append(img.crop((abs(pos[0] + 300), 100, abs(pos[0] + 300) + 30, 200)))
            else:
                if count <= 10:
                    if pos[1] == 0:

                        image_upper_lst.append(img.crop((abs(pos[0]), 0, abs(pos[0]) + 30, 100)))
                    else:
                        image_upper_lst.append(img.crop((abs(pos[0]), 100, abs(pos[0]) + 30, 200)))
                else:
                    if pos[1] == 0:

                        image_down_lst.append(img.crop((abs(pos[0]), 0, abs(pos[0]) + 30, 100)))
                    else:
                        image_down_lst.append(img.crop((abs(pos[0]), 100, abs(pos[0]) + 30, 200)))
            count += 1
        x_offset = 0
        # 创建一张画布，x_offset主要为新画布使用
        new_img = Image.new("RGB", (300, 200))
        for img in image_upper_lst:
            new_img.paste(img, (x_offset, 0))
            x_offset += 30

        x_offset = 0
        for img in image_down_lst:
            new_img.paste(img, (x_offset, 100))
            x_offset += 30

        return new_img
    def start_move(self, distance):
        element = self.driver.find_element_by_xpath('//div[@class="handler handler_bg"]')
        # 按下鼠标左键
        ActionChains(self.driver).click_and_hold(element).perform()
        time.sleep(0.5)
        while distance > 0:
            if distance > 10:
                # 如果距离大于10，就让他移动快一点
                span = random.randint(10, 15)
            else:
                # 快到缺口了，就移动慢一点
                span = random.randint(2, 3)
            ActionChains(self.driver).move_by_offset(span, 0).perform()
            distance -= span
            time.sleep(random.randint(10, 50) / 100)

        ActionChains(self.driver).move_by_offset(distance, 1).perform()
        ActionChains(self.driver).release(on_element=element).perform()

if __name__ == "__main__":
    h = qjh()
    h.core()
