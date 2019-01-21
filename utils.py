import os
import re

PACMAN_TEMPLATE = 'sudo pacman -S --noconfirm --need'


def show_menu_and_get_user_chose(groups: list) -> str:
    """
    显示菜单
    :return:
    """
    print('----------')
    index = 0
    for group in groups:
        # print(str(index) + ')' + group['name'] + ' -- 软件包：' + group['packages'])
        print(str(index) + ')' + group['name'])
        index += 1
    print('q) 退出')
    print('----------')
    print('使用方法')
    print('输入单个数字（如 2），运行单个功能')
    print('输入数字范围（如 4-10），运行多个功能')
    print('----------')
    chose = input('>>> ')
    return chose


def run(groups: list):
    """
    开始运行
    :param groups 软件包列表
    :return:
    """
    try:
        while True:
            user_chose = show_menu_and_get_user_chose(groups)
            result = re.match(r'(\d+)-(\d+)', user_chose)
            if result is None:
                # 安装单个软件包
                user_chose = int(user_chose)
                install_package(groups[user_chose]['packages'])
                if 'config' in groups[user_chose]:
                    groups[user_chose]['config']()
                continue
            start = int(result.group(1))
            end = int(result.group(2))
            # 安装多个软件包
            for i in range(start, end + 1):
                install_package(groups[i]['packages'])
                if 'config' in groups[i]:
                    groups[i]['config']()
    except ValueError:
        return None


def install_package(packages: str):
    """
    安装软件包
    :param packages: 软件包列表，多个软件使用空格分隔
    :return:
    """
    cmd = PACMAN_TEMPLATE + ' ' + packages
    os.system(cmd)
    return None
