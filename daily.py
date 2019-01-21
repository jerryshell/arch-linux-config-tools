import os

from utils import run

ARCHLINUXCN = r'''
[archlinuxcn]
Server = https://mirrors.ustc.edu.cn/archlinuxcn/\$arch
'''

FCITX = r'''
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx
'''


def config_archlinuxcn():
    """
    配置 archlinuxcn 软件仓库
    :return:
    """
    os.system('echo "' + ARCHLINUXCN + '" | sudo tee -a /etc/pacman.conf')
    os.system('sudo pacman -Syu --noconfirm archlinuxcn-keyring')
    return None


def config_ohmyzsh():
    """
    配置 oh-my-zsh 和 zsh-autosuggestions
    :return:
    """
    os.system(
        r'''
        sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
        '''
    )
    os.system(
        r'''
        echo 'source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh\' | tee -a ~/.zshrc
        '''
    )
    return None


def config_sogou():
    """
    配置搜狗输入法
    :return:
    """
    cmd_xprofile = 'echo "' + FCITX + '" | tee -a ~/.xprofile'
    cmd_environment = 'echo "' + FCITX + '" | sudo tee -a /etc/environment'
    os.system(cmd_xprofile)
    os.system(cmd_environment)
    return None


groups = [
    {'name': '安装基本环境', 'packages': 'base base-devel htop git gvim curl wget'},
    {'name': '添加 archlinucn 软件仓库', 'packages': 'None', 'config': config_archlinuxcn},
    {'name': '安装 yay', 'packages': 'yay'},
    {'name': '安装浏览器', 'packages': 'google-chrome firefox firefox-i18n-zh-cn'},
    {'name': '睁眼看世界套餐', 'packages': 'tor vidalia shadowsocks shadowsocks-libev shadowsocks-qt5 v2ray'},
    {'name': '安装 oh-my-zsh', 'packages': 'zsh zsh-completions zsh-autosuggestions', 'config': config_ohmyzsh},
    {'name': '安装字体',
     'packages': 'powerline-fonts noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra wqy-bitmapfont wqy-microhei wqy-zenhei adobe-source-code-pro-fonts'},
    {'name': '安装 wps', 'packages': 'wps-office ttf-wps-fonts'},
    {'name': '安装快速启动器', 'packages': 'alber'},
    {'name': '安装词典软件', 'packages': 'goldendict'},
    {'name': '安装命令行下载工具', 'packages': 'aria2-fast'},
    {'name': '安装自动切换壁纸软件', 'packages': 'variety'},
    {'name': '安装图标', 'packages': 'papirus-icon-theme'},
    {'name': '安装绘画软件', 'packages': 'gimp krita'},
    {'name': '安装文件传输工具', 'packages': 'filezilla'},
    {'name': '安装截图工具', 'packages': 'flameshot'},
    {'name': '安装搜狗输入法', 'packages': 'fcitx-im fcitx-configtool fcitx-sogoupinyin', 'config': config_sogou},
    {'name': '安装 privoxy（需要额外配置，见 README）', 'packages': 'proxychains-ng privoxy'},
    {'name': '安装 virtualbox（需要额外配置，见 README）', 'packages': 'virtualbox virtualbox-ext-oracle virtualbox-guest-iso'},
    {'name': '安装 wine（需要额外配置，见 README）', 'packages': 'wine wine_gecko wine-mono winetricks'},
]

if __name__ == '__main__':
    run(groups)
