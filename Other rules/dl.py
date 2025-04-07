import os
import subprocess
import time
import shutil

# 删除目录下所有的文件
directory = "./data/rules/"

# 确保目录存在并遍历删除其中的文件
if os.path.exists(directory):
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"无法删除文件: {file_path}, 错误: {e}")
else:
    print(f"目录 {directory} 不存在")

# 删除目录本身
try:
    shutil.rmtree(directory)
    print(f"成功删除目录 {directory} 及其中的所有文件")
except Exception as e:
    print(f"无法删除目录 {directory}, 错误: {e}")

# 创建临时文件夹
os.makedirs("./tmp/", exist_ok=True)

# 复制补充规则到tmp文件夹
subprocess.run("cp ./data/mod/adblock.txt ./tmp/adblock01.txt", shell=True)
subprocess.run("cp ./data/mod/whitelist.txt ./tmp/allow01.txt", shell=True)


# 拦截规则
adblock = [
    "https://raw.githubusercontent.com/qq5460168/dangchu/main/black.txt",
    "https://raw.githubusercontent.com/damengzhu/banad/main/jiekouAD.txt",
    "https://raw.githubusercontent.com/afwfv/DD-AD/main/rule/DD-AD.txt",
    "https://raw.githubusercontent.com/Cats-Team/dns-filter/main/abp.txt",
    "https://raw.hellogithub.com/hosts",
    "https://raw.githubusercontent.com/qq5460168/dangchu/main/adhosts.txt",
    "https://raw.githubusercontent.com/qq5460168/dangchu/main/white.txt",
    "https://raw.githubusercontent.com/loveqqzj/AdGuard/master/Mobile.txt",
    "https://raw.githubusercontent.com/mphin/AdGuardHomeRules/main/Blacklist.txt",
    "https://gitee.com/zjqz/ad-guard-home-dns/raw/master/black-list",
    "https://raw.githubusercontent.com/liwenjie119/adg-rules/master/black.txt"
    "https://github.com/entr0pia/fcm-hosts/raw/fcm/fcm-hosts"
    "https://raw.githubusercontent.com/TG-Twilight/AWAvenue-Ads-Rule/main/AWAvenue-Ads-Rule.txt"
    "https://raw.githubusercontent.com/miaoermua/AdguardFilter/main/rule.txt"
]

# 白名单规则
allow = [
    "https://raw.githubusercontent.com/qq5460168/dangchu/main/white.txt",
    "https://raw.githubusercontent.com/mphin/AdGuardHomeRules/main/Allowlist.txt",
    "https://file-git.trli.club/file-hosts/allow/Domains",
    "https://hub.gitmirror.com/https://raw.githubusercontent.com/user001235/112/main/white.txt",
    "https://raw.githubusercontent.com/liwenjie119/adg-rules/master/white.txt",
    "https://raw.githubusercontent.com/qq5460168/dangchu/main/T%E7%99%BD%E5%90%8D%E5%8D%95.txt",
    "https://raw.githubusercontent.com/miaoermua/AdguardFilter/main/whitelist.txt"
]

# 下载
for i, adblock_url in enumerate(adblock):
    subprocess.Popen(f"curl -m 60 --retry-delay 2 --retry 5 -k -L -C - -o tmp/adblock{i}.txt --connect-timeout 60 -s {adblock_url} | iconv -t utf-8", shell=True).wait()
    time.sleep(1)

for j, allow_url in enumerate(allow):
    subprocess.Popen(f"curl -m 60 --retry-delay 2 --retry 5 -k -L -C - -o tmp/allow{j}.txt --connect-timeout 60 -s {allow_url} | iconv -t utf-8", shell=True).wait()
    time.sleep(1)
    
print('规则下载完成')


