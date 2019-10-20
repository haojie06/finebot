from nonebot import on_command, CommandSession
from py_mcpe_stats import query


@on_command('querype', aliases=('pe在线', '基岩版查在线'))
async def querype(session: CommandSession):
    ip = session.get("ip", prompt="你想查询哪个基岩版服务器的在线情况呢?")
    port = session.get("port", prompt="服务器的端口是什么呢？")
    q = query.Query(ip, int(port), 10)
    server_status = q.query()
    await session.send(server_status)
    # 获得服务器的在线情况


@querype.args_parser
async def _(session: CommandSession):
    # 去掉消息首尾的空白符
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            # 第一次运行参数不为空，意味着用户直接将服务器/服务器:端口接在了命令之后
            args = stripped_arg.split(":")
            # 参数为两个
            if len(args) == 2:
                session.state['ip'] = args[0]
                session.state['port'] = args[1]
            elif len(args) == 1:
                session.get('port', prompt="请问服务器的端口是什么呢?")
            else:
                session.pause('查询格式错误')
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的服务器不能为空呢,请使用querype ip:port 的形式进行查询')

    # 如果当前正在向用户询问更多信息，且用户输入有效，则放入会话状态
    session.state[session.current_key] = stripped_arg
