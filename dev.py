import os

from utils import run


def config_pip_douban():
    """
    添加 pip 豆瓣镜像源
    :return:
    """
    os.system(
        r'''
        sudo bash -c "mkdir -p /root/.pip && printf '[global]\nindex-url = http://pypi.douban.com/simple\ntrusted-host = pypi.douban.com\n' | tee /root/.pip/pip.conf"
        '''
    )
    return None


def config_cnpm_hexo_angular_vue():
    """
    配置 cnpm hexo angular vue
    :return:
    """
    cmd_cnpm = 'sudo npm install -g cnpm --registry=https://registry.npm.taobao.org'
    cmd_hexo = 'sudo cnpm install hexo-cli -g'
    cmd_angular = 'sudo cnpm install -g @angular/cli'
    cmd_vue = 'sudo cnpm install -g @vue/cli'
    os.system(cmd_cnpm)
    os.system(cmd_hexo)
    os.system(cmd_angular)
    os.system(cmd_vue)
    return None


def config_mariadb():
    """
    初始化 mariadb
    :return:
    """
    cmd1 = 'sudo mysql_install_db --user=mysql --basedir=/usr --datadir=/var/lib/mysql'
    cmd2 = 'sudo systemctl start mariadb.service'
    cmd3 = 'sudo /usr/bin/mysql_secure_installation'
    os.system(cmd1)
    os.system(cmd2)
    os.system(cmd3)
    return None


def config_postgresql():
    """
    初始化 postgresql
    :return:
    """
    cmd = r'''sudo su - postgres -c "initdb --locale en_US.UTF-8 -E UTF8 -D '/var/lib/postgres/data'"'''
    os.system(cmd)
    return None


groups = [
    # 基本环境
    {'name': 'gvim + vscode + git', 'packages': 'gvim code git'},
    {'name': 'gitkraken + lazygit', 'packages': 'gitkraken lazygit'},

    # python
    {'name': 'python-pip + python2-pip + 豆瓣镜像', 'packages': 'python-pip python2-pip', 'config': config_pip_douban},
    {'name': 'python 爬虫 + 数据挖掘',
     'packages': 'python-requests python-lxml python-beautifulsoup4 python-jieba python-pandas python-selenium python-scipy python-matplotlib'},
    {'name': 'python-pylint + autopep8', 'packages': 'python-pylint autopep8'},
    {'name': 'pycharm-professional', 'packages': 'pycharm-professional'},

    # java
    {'name': 'netbeans + eclipse-jee + gradle + maven', 'packages': 'netbeans eclipse-jee gradle maven'},
    {'name': 'intellij-idea-ultimate-edition + intellij-idea-ultimate-edition-jre',
     'packages': 'intellij-idea-ultimate-edition intellij-idea-ultimate-edition-jre'},
    {'name': 'spring-tool-suite', 'packages': 'spring-tool-suite'},
    {'name': 'android-studio', 'packages': 'android-studio'},

    # go
    {'name': 'go + go-tools + goland + goland-jre + liteide', 'packages': 'go go-tools goland goland-jre liteide'},

    # cpp
    {'name': 'clion + clion-cmake + clion-gdb + clion-jre + clion-lldb',
     'packages': 'clion clion-cmake clion-gdb clion-jre clion-lldb'},

    # 前端
    {'name': 'nodejs + npm + yarn + webstorm + webstorm-jre', 'packages': 'nodejs npm yarn webstorm webstorm-jre'},
    {'name': 'cnmp + hexo + angular + vue', 'packages': 'None', 'config': config_cnpm_hexo_angular_vue},

    # postman
    {'name': 'postman', 'packages': 'postman-bin'},

    # 网络工具
    {'name': '网络工具',
     'packages': 'nmap metasploit aircrack-ng whois kismet wifite wireshark-cli wireshark-common wireshark-qt wireshark-gtk'},

    # 数据库
    {'name': 'dbeaver + mysql-workbench', 'packages': 'dbeaver mysql-workbench'},
    {'name': 'datagrip', 'packages': 'datagrip datagrip-jre'},
    {'name': 'redis + redis-desktop-manager', 'packages': 'redis redis-desktop-manager'},
    {'name': 'mariadb + mycli + 初始化', 'packages': 'mariadb mycli', 'config': config_mariadb},
    {'name': 'postgresql + pgadmin4 + 初始化', 'packages': 'postgresql pgadmin4', 'config': config_postgresql},
]

if __name__ == '__main__':
    run(groups)
