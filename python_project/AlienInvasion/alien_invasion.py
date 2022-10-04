import sys
import pygame


class AlienInvasion(object):
    """
    管理游戏资源和行为的类
    """
    def __init__(self) -> None:
        """
        初始化游戏并且创建游戏资源
        """
        super(AlienInvasion, self).__init__()
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")
        # 设置背景颜色
        self.bg_color = (230, 230, 230)

    def run_game(self) -> None:
        """
        开始游戏的主循环
        :return:
        """
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # 每次循环都重新绘制屏幕
            self.screen.fill(self.bg_color)
            # 让最近录制的屏幕可见
            pygame.display.flip()


if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
