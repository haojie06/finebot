import nonebot
import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_builtin_plugins()
    nonebot.run(host='172.17.0.1', port=8088)