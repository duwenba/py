import requests
import re#,sys,io
from os import system
import json

def get_respons(url):
    headers={
        "referer": "https://www.bilibili.com/",#防爬链，不加会无法访问
        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62"
    }
    resp=requests.get(url=url,headers=headers)
    # resp.encoding="utf-8"
    return resp

get_playinfo = re.compile(r"<script>window.__playinfo__=(?P<play>.*?)</script>",re.S)
get_title = re.compile(r'''<title data-vue-meta="true">(?P<title>.*?)</title>''')

def download(url,name,path=''):
    resp=get_respons(url)
    with open(path+name,mode='wb') as f:
        f.write(resp.content)
        f.close()


ffmpeg = r"D:\program files\FormatFactory\ffmpeg.exe"
def mix(title,output="output"):
    # system(f"md {output}")
    system(f"\"{ffmpeg}\" -i video.mp4 -i audio.mp3 -c:v copy -c:a aac -strict experimental {output}\\{title}.mp4")

    # sleep(15)
    system("del -f video.mp4")
    system("del -f audio.mp3")


def main(url,output="output"):
    #获取网页源代码
    html=get_respons(url)
    html_src = str(html.content,"utf-8")
    title = get_title.findall(html_src)[0]
    # print(html_src)
    html.close()
    #get  playinfo
    playinfo = get_playinfo.findall(html_src)[0]
    play_json = json.loads(playinfo)
    #获取连接
    #视频
    vidoe_url = play_json['data']['dash']['video'][0]['baseUrl']
    # print("视频链接：",vidoe_url)
    audio_url = play_json['data']['dash']['audio'][0]['baseUrl']
    # print('音频链接：',audio_url)
    download(vidoe_url,"video.mp4")
    download(audio_url,"audio.mp3")
    #合并音视频
    mix(title,output)


if __name__ == "__main__":
    # sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
    # Bid = "BV1DR4y1k7hN"
    Bid = input("请输入视频号：")
    # output = ''
    url=f"https://www.bilibili.com/video/{Bid}/"
    main(url)