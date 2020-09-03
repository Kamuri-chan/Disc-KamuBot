import discord
from discord.ext import commands
from reference_doc import read_doc, print_multiple_str


client = commands.Bot(command_prefix='.')

try:
    @client.event
    async def on_ready():
        print("Bot is ready")

    @client.command()
    async def end(ctx):
        await ctx.send("Encerrado")
        quit()

    @client.command()
    async def ping(ctx):
        await ctx.send(f"Pong! {round(client.latency)}ms")

    @client.command()
    async def bot_help(ctx, arg=""):
        a = """Este é um guia básico de como usar o bot. Para maiores informações, use:
        .bot_help command
        Os comandos presentes no momento são:
        .ping, checa seu ping e retorna a informação.
        .ban(membro, razão), bane um membro, opcionalmente podendo passar uma razão.
        .kick(membro, razão), remove um membro, opcionalmente podendo passar uma razão.
        .clear(quantidade), limpa determinada quantidade de mensagens. O arg é opcional.
        .doc(termo), pesquisa o termo na documentação do python.
        """

        p = """Comando .ping:
        O comando .ping calcula o tempo que a informação leva para chegar ao servidor."""

        b = """Comando .ban membro, (opcional) motivo:
        O comando .ban bane um membro, adicionalmente, pode-se adicionar um motivo."""

        k = """Comando .kick membro, (opcional) motivo:
        O comando .kick remove um membro, adicionalmente, pode-se adicionar um motivo."""

        d = """Comando .doc termo:
        O comando .doc pequisa o termo em https://docs.python.org/3/reference/index.html e
        retorna o conteúdo que encontrar. O conteúdo no momento é em inglês, mas tenho
        futuros planos de usar alguma API para traduzir."""

        if arg == "":
            await ctx.send(a)
        elif arg == ".ping":
            await ctx.send(p)
        elif arg == ".ban":
            await ctx.send(b)
        elif arg == ".kick":
            await ctx.send(k)
        elif arg == ".doc":
            await ctx.send(d)

    @client.command()
    async def ban(ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    @client.command()
    async def clear(ctx, amount=1):
        await ctx.channel.purge(limit=amount)

    @client.command()
    async def kick(ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    @client.command()
    async def doc(ctx, find):
        raw_doc = read_doc(find)

        if (isinstance(raw_doc, list)):
            for char in raw_doc:
                text = (''.join(char))
                if len(text) > 2000:
                    resto = text
                    has_char = True
                    while has_char:
                        char, resto, has_char = print_multiple_str(resto)
                        formmated = (''.join(char))
                        await ctx.send(formmated)
                else:
                    await ctx.send(text)
        elif (isinstance(raw_doc, str)):
            print(raw_doc)
        else:
            await ctx.send("Erro! Não encontrei nada!")

    client.run("token")
except SystemExit:
    print("Encerrado!")
