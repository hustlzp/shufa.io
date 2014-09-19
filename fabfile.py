# coding: utf-8
from fabric.api import run, env, cd, prefix, shell_env
from config import load_config

config = load_config()
host_string = config.HOST_STRING


def init():
    """初始化部署"""
    env.host_string = config.HOST_STRING
    with cd('/var/www/shufa'):
        with shell_env(MODE='PRODUCTION'):
            run('git reset --hard HEAD')
            run('git pull')
            run('bower install --allow-root')
            with prefix('source venv/bin/activate'):
                run('pip install -r requirements.txt')
                run('python manage.py createdb')
            run('sudo supervisorctl restart shufa')


def deploy():
    """部署"""
    env.host_string = config.HOST_STRING
    with cd('/var/www/shufa'):
        with shell_env(MODE='PRODUCTION'):
            run('git reset --hard HEAD')
            run('git pull')
            run('bower install --allow-root')
            with prefix('source venv/bin/activate'):
                run('pip install -r requirements.txt')
                run('python manage.py db upgrade')
            run('sudo supervisorctl restart shufa')


def restart():
    """重启"""
    env.host_string = config.HOST_STRING
    run('sudo supervisorctl restart shufa')