from time import sleep,strftime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import WebDriverException
import smtplib
# import email
# 负责构造文本
from email.mime.text import MIMEText
# 负责构造图片
from email.mime.image import MIMEImage
# 负责将多个对象集合起来
from email.mime.multipart import MIMEMultipart
from email.header import Header
# iqncdthwqsejebje授权码
# url:str = 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/jksb?ptopid=sC02BA3DA781B42B48996C4B63E4E3186&amp;sid=221118125401162747&amp;fun2='
url:str = 'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first6?ptopid=s554AE54B6FB74A959900B649458E3DF2&sid=221118095111746531&fun2=&id8='
button_1_xpath = "//*[@id='bak_0']/div[11]/div[3]/div[4]" #本人填报 //*[@id="bak_0"]/div[11]/div[3]/div[4]
button_2_id = 'btn416a'#提交表格
final_text_xpath = "//*[@id='bak_0']/div[2]/div[2]/div[2]/div[2]"   
# =========================================================================================== 
user={
    'user_name': '202207070604',
    'password': 'Dwb.20040216',
    #SMTP服务器,这里使用163邮箱
    'mail_host': "smtp.qq.com",
    # 发件人邮箱
    'mail_sender': "2275317692@qq.com",
    # 邮箱授权码,注意这里不是邮箱密码,如何获取邮箱授权码,请看本文最后教程
        'mail_license': "vsyqjrzvabnzecba",
    # 收件人邮箱，可以为多个收件人
    'mail_receivers': ["duwenba_gongzuo@126.com"]
}
def log_in(url)  :
    edge_options = Options()
    edge_options.add_argument('--headless')
    driver = webdriver.Edge(options=edge_options)
    try:
        driver.get(url)
        driver.implicitly_wait(20)
    except WebDriverException as value:
        print(value)
    except:
        print('unexcepted erro')
    else:
        driver.execute_script('window.location=\'https://jksb.v.zzu.edu.cn/vls6sss/zzujksb.dll/first0\'')
        driver.implicitly_wait(5)
        driver.find_element(By.NAME,'uid').send_keys(user['user_name'])
        driver.find_element(By.NAME,'upw').send_keys(user['password'])
        driver.find_element(By.NAME,'smbtn').click()
        driver.implicitly_wait(5)
        #iframe
        iframe = driver.find_element(By.ID,'zzj_top_6s')
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH,button_1_xpath).click()
        #等待定位
        sleep(15)
        driver.find_element(By.ID,button_2_id).click()
        text=  driver.find_element(By.XPATH,final_text_xpath).text
        driver.close()
        return text
def mail(msg):
    mm = MIMEMultipart('related')
    # 邮件主题
    subject_content = """自动打卡结果"""
    # 设置发送者,注意严格遵守格式,里面邮箱为发件人邮箱
    mm["From"] = "自动打卡<2275317692@qq.com>"
    # 设置接受者,注意严格遵守格式,里面邮箱为接受者邮箱
    mm["To"] = "杜文霸<duwenba_gongzuo@126.com>"
    # 设置邮件主题
    mm["Subject"] = Header(subject_content,'utf-8')
    # 邮件正文内容
    body_content = msg
    # 构造文本,参数1：正文内容，参数2：文本格式，参数3：编码方式
    message_text = MIMEText(body_content,"plain","utf-8")
    # 向MIMEMultipart对象中添加文本对象
    mm.attach(message_text)
    # 创建SMTP对象
    stp = smtplib.SMTP()
    # 设置发件人邮箱的域名和端口，端口地址为25
    stp.connect(user['mail_host'], 25)  
    # set_debuglevel(1)可以打印出和SMTP服务器交互的所有信息
    stp.set_debuglevel(1)
    # 登录邮箱，传递参数1：邮箱地址，参数2：邮箱授权码
    stp.login(user['mail_sender'],user['mail_license'])
    # 发送邮件，传递参数1：发件人邮箱地址，参数2：收件人邮箱地址，参数3：把邮件内容格式改为str
    stp.sendmail(user['mail_sender'], user['mail_receivers'], mm.as_string())
    print("邮件发送成功")
    # 关闭SMTP对象
    stp.quit()
if __name__ == '__main__':
            mail(log_in(url))