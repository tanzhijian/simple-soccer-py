class SoccerPitch:
    def __init__(self) -> None:
        self.ball = SoccerBall()

        self.red_team = SoccerTeam()
        self.blue_team = SoccerTeam()

        self.red_goal = Goal()
        self.blue_goal = Goal()

        self.vec_walls = Wall2D()
        self.playing_area = Region()

        self.game_on = False
        self.goalkeeper_has_ball = False

        def update(self) -> None:
            ...

        def render(self) -> None:
            ...


class SoccerBall:
    ...


class SoccerTeam:
    ...


class Goal:
    def __init__(self, left: Vector2D, right: Vector2D) -> None:
        self.left_post = left
        self.right_post = right

        self.facing = Vector2D()  # 球门的朝向向量
        self.center = (left + right) / 2  # 球门线的中间位置

        self.num_goals_scored = 0

    def scored(self) -> bool:
        ...


class Wall2D:
    ...


class Region:
    ...
