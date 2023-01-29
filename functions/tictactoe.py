from logging import getLogger

from discord import ApplicationContext, Option, User, Embed
from discord.ext.commands import Cog

from config import BAD
from utils import slash_command
from views import TicTacToe

logger = getLogger(__name__)


class TicTacToeGame(Cog):
    @slash_command(name="틱택토", description="틱택토(삼목) 게임을 진행합니다.")
    async def tictactoe(
            self,
            ctx: ApplicationContext,
            rival: Option(User, description="같이 게임을 할 유저를 선택하세요", name="상대"),
    ):
        if rival.bot:
            embed = Embed(
                title="WhiteBot 오류", description="틱택토 기능", color=BAD
            )
            embed.add_field(name="오류 내용:", value="봇과는 대결할 수 없습니다.", inline=False)
            await ctx.respond(embed=embed)
        else:
            await ctx.respond(
                f"틱택토(삼목) 게임을 시작합니다. {ctx.user.mention}(X) vs {rival.mention}(O) - X부터 시작합니다.",
                view=TicTacToe(ctx.user.id, rival.id),
            )


def setup(bot):
    logger.info("Loaded")
    bot.add_cog(TicTacToeGame(bot))
