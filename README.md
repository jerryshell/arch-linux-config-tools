# Arch Linux Config Tools

Arch Linux 配置工具

# 使用方法

```sh
# 日常配置
python3 ./daily.py

# 开发配置
python3 ./dev.py
```

输入单个数字（如 2），运行单个功能

输入数字范围（如 4-10），运行多个功能

# daily.py 功能

* 安装基本环境 -- 软件包：base base-devel htop git gvim curl wget
* 添加 archlinucn 软件仓库和安装 yay -- 软件包：archlinuxcn-keyring yay
* 安装浏览器 -- 软件包：google-chrome firefox firefox-i18n-zh-cn
* 睁眼看世界套餐 -- 软件包：tor vidalia shadowsocks shadowsocks-libev shadowsocks-qt5 v2ray
* 安装 oh-my-zsh -- 软件包：zsh zsh-completions zsh-autosuggestions
* 安装字体 -- 软件包：powerline-fonts noto-fonts noto-fonts-cjk noto-fonts-emoji noto-fonts-extra wqy-bitmapfont wqy-microhei wqy-zenhei adobe-source-code-pro-fonts
* 安装 wps -- 软件包：wps-office ttf-wps-fonts
* 安装快速启动器 -- 软件包：alber
* 安装词典软件 -- 软件包：goldendict
* 安装命令行下载工具 -- 软件包：aria2-fast
* 安装自动切换壁纸软件 -- 软件包：variety
* 安装图标 -- 软件包：papirus-icon-theme
* 安装绘画软件 -- 软件包：gimp krita
* 安装文件传输工具 -- 软件包：filezilla
* 安装截图工具 -- 软件包：flameshot
* 安装搜狗输入法 -- 软件包：fcitx-im fcitx-configtool fcitx-sogoupinyin
* 安装代理工具（需要额外配置，见 README） -- 软件包：proxychains-ng privoxy
* 安装 virtualbox（需要额外配置，见 README） -- 软件包：virtualbox virtualbox-ext-oracle virtualbox-guest-iso
* 安装 wine（需要额外配置，见 README） -- 软件包：wine wine_gecko wine-mono winetricks

# dev.py 功能

* gvim + vscode + git
* gitkraken + lazygit
* python-pip + python2-pip + 豆瓣镜像
* python 爬虫 + 数据挖掘
* python-pylint + autopep8
* pycharm-professional
* netbeans + eclipse-jee + gradle + maven
* intellij-idea-ultimate-edition + intellij-idea-ultimate-edition-jre
* spring-tool-suite
* android-studio
* go + go-tools + goland + goland-jre + liteide
* clion + clion-cmake + clion-gdb + clion-jre + clion-lldb
* nodejs + npm + yarn + webstorm + webstorm-jre
* cnmp + hexo + angular + vue
* postman
* 网络工具
* dbeaver + mysql-workbench
* datagrip
* redis + redis-desktop-manager
* mariadb + mycli + 初始化
* postgresql + pgadmin4 + 初始化

# 额外配置说明

## proxychains-ng 配置

```sh
sudo vim /etc/proxychains.conf

# 添加配置
socks5 127.0.0.1 1080
```

## privoxy 配置

```sh
sudo vim /etc/privoxy/match-all.action

# 添加配置
+hide-user-agent{Big Brother is watching you} \
```

默认端口：8118

查看浏览器 UA：http://whatsmyuseragent.org/

## VirtualBox 虚拟机访问 USB 设备配置

需要将用户名添加到 vboxusers 用户组

## Wine 配置

```sh
# 字体
winetricks allfonts
```
