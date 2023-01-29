from logging import getLogger
from random import choice, randint

from discord import ApplicationContext, Embed, Option
from discord.ext.commands import Cog

from config import BAD, COLOR
from utils import slash_command

logger = getLogger(__name__)


class SimpleGame(Cog):
    @slash_command(name="가위바위보", description="봇과 가위바위보 게임을 합니다.")
    async def rsp(
            self,
            ctx: ApplicationContext,
            user: Option(str, "낼 것을 선택하세요", choices=["가위", "바위", "보"], name="입력"),
    ):
        rsp_table = ["가위", "바위", "보"]
        bot = choice(rsp_table)
        result = rsp_table.index(user) - rsp_table.index(bot)
        if result == 0:
            message = f"{user} vs {bot}\n비겼네요!"
        elif result == 1 or result == -2:
            message = f"{user} vs {bot}\n{ctx.user.display_name}님이 이겼어요!"
        else:
            message = f"{user} vs {bot}\n봇이 이겼습니다!"
        embed = Embed(
            title="가위바위보",
            description=f"{ctx.user.display_name} vs 봇",
            color=COLOR,
        )
        embed.add_field(name="**결과:**", value=f"{message}", inline=False)
        await ctx.respond(embed=embed)

    @slash_command(name="주사위", description="주사위를 굴립니다.")
    async def dice(
            self,
            ctx: ApplicationContext,
            firstn: Option(int, "첫번째 숫자를 정하세요. 두번째 숫자가 없을 경우 범위는 1 ~ firstn으로 결정됩니다.", name="범위 1"),
            secondn: Option(
                int, "두번째 숫자가 있을 경우 범위는 firstn ~ secondn으로 결정됩니다. ", required=False, name="범위 2"
            ),
    ):
        try:
            if firstn < 1:
                embed = Embed(
                    title="WhiteBot 오류", description="주사위 기능", color=BAD
                )
                embed.add_field(name="오류 내용:", value="자연수 값만 허용됩니다.", inline=False)
                await ctx.respond(embed=embed)
            elif secondn:
                embed = Embed(
                    title="주사위", description=f"{firstn} ~ {secondn}", color=COLOR
                )
                embed.add_field(
                    name="**결과:**",
                    value=f"주사위를 굴렸더니 {randint(firstn, secondn)}(이)가 나왔어요!",
                    inline=False,
                )
                await ctx.respond(embed=embed)
            else:
                embed = Embed(
                    title="주사위", description=f"1 ~ {firstn}", color=COLOR
                )
                embed.add_field(
                    name="**결과:**",
                    value=f"주사위를 굴렸더니 {randint(1, firstn)}(이)가 나왔어요!",
                    inline=False,
                )
                await ctx.respond(embed=embed)
        except Exception:
            embed = Embed(
                title="WhiteBot 오류", description="주사위 기능", color=BAD
            )
            embed.add_field(
                name="오류 내용:",
                value="1. 자연수가 아닌 수를 쓰셨는지 확인해주세요.\n2. 첫번째 숫자가 두번째 숫자보다 더 큰지 확인해주세요.",
                inline=False,
            )
            await ctx.respond(embed=embed)

    @slash_command(name="홀짝", description="홀짝 게임을 시작합니다.")
    async def holjjac(self, ctx: ApplicationContext):
        dice = randint(1, 6)
        embed = Embed(
            title="홀짝 게임",
            description="1부터 6까지 나오는 주사위의 수가 짝수일지, 홀수일지 아래의 반응을 눌러 예측해보세요!",
            color=COLOR
        )
        embed.add_field(name="> 주사위의 눈", value="?", inline=False)
        embed.add_field(name="> 선택지", value="홀수: 🔴\n짝수: 🔵", inline=True)
        interaction = await ctx.interaction.response.send_message(embed=embed)
        msg = await interaction.original_response()
        await msg.add_reaction("🔴")
        await msg.add_reaction("🔵")
        try:
            def check(check_reaction, check_user):
                return (
                        str(check_reaction) in ["🔴", "🔵"]
                        and check_user == ctx.author
                        and check_reaction.message.id == msg.id
                )

            reaction, user = await ctx.bot.wait_for("reaction_add", check=check)
            if (str(reaction) == "🔴" and dice % 2 == 1) or (
                    str(reaction) == "🔵" and dice % 2 == 0
            ):
                embed = Embed(
                    title="홀짝 게임", description="정답입니다!", color=COLOR
                )
                embed.add_field(name="> 주사위의 눈", value=f"{dice}")
                embed.add_field(name="> 당신의 선택", value=f"{str(reaction)}", inline=False)
            else:
                embed = Embed(
                    title="홀짝 게임", description="틀렸습니다..", color=COLOR
                )
                embed.add_field(name="> 주사위의 눈", value=f"{dice}")
                embed.add_field(name="> 당신의 선택", value=f"{str(reaction)}", inline=False)
            await msg.edit(embed=embed)
        except Exception:
            logger.exception("Unexpected exception from holjjac")
            embed = Embed(
                title="오류가 발생했어요", description="잠시 후에 다시 시도해주세요", color=BAD
            )
            await msg.edit(embed=embed)


def setup(bot):
    bot.add_cog(SimpleGame())
    logger.info("Loaded")
