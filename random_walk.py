from random import choice


class RandomWalk:
    """Класс для генерирования случайных блужданий."""

    def __init__(self, num_points=10000):
        """Инициализирует атрибуты блуждания."""
        self.num_points = num_points
        # Все блуждания начинаются с точки (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Вычисляет все точки блуждания."""

        # Шаги генерируются до достижения нужной длины.
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # Отклонение нулевых перемещений.
            if x_step == 0 and y_step == 0:
                continue
            # Вычисление следующих значений x и y.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        """Вычисляет шаг блуждания"""
        # Определение направления и длины перемещения.
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        x_step_in = x_direction * x_distance
        y_direction = choice([1, -1])
        y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        y_step_in = y_direction * y_distance
        return x_step_in and y_step_in
