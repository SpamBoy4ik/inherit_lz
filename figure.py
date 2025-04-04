import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon
from math import sin, cos, acos

class Square:
    def __init__(self, side_size_a, color, border_width=1, filled=True):
        self.side_size_a = abs(side_size_a)
        self.color = color
        self.border_width = border_width
        self.filled = filled

    def info(self):
        print(f'\nЦвет: {self.color}\nТощина границы: {self.border_width}\nФигура залита внутри: {self.filled}\nДлины сторон: {self.side_size_a}', end=' ')
    
    def patch_figure(self):
        return Rectangle((0.5, 0.5), self.side_size_a, self.side_size_a,
                          facecolor=self.color, edgecolor='black', linewidth=self.border_width, fill=self.filled)

    def draw(self):
        plt.xlim(-1, self.side_size_a * 2)
        plt.ylim(-1, self.side_size_a * 2)
        ax = plt.gca()
        figure = self.patch_figure()
        ax.add_patch(figure)
        ax.grid()
        plt.show()

    def __del__(self):
        print('del done')


class Quadrilateral(Square):
    def __init__(self, side_size_a, side_size_b, side_size_c, side_size_d, color, border_width=1, filled=True):
        super().__init__(side_size_a, color, border_width, filled)
        self.side_size_b = abs(side_size_b)
        self.side_size_c = abs(side_size_c)
        self.side_size_d = abs(side_size_d)
    
    def info(self):
        super().info()
        print(self.side_size_b, self.side_size_c, self.side_size_d)
    
    def check_sides(self): # проверяет, может ли существовать четырехугольник с этими сторонами
        if self.side_size_a + self.side_size_b + self.side_size_c > self.side_size_d: pass
        else: return False
        if self.side_size_a + self.side_size_b + self.side_size_d > self.side_size_c: pass
        else: return False
        if self.side_size_a + self.side_size_d + self.side_size_c > self.side_size_b: pass
        else: return False
        if self.side_size_d + self.side_size_b + self.side_size_c > self.side_size_a: pass
        else: return False
        return True
        
    def coordinates(self): # находит координаты вершин
        coordinates = [(0, 0), (self.side_size_a, 0)]
        angle = acos((self.side_size_a**2 + self.side_size_b**2 - self.side_size_c**2) / (2 * self.side_size_a * self.side_size_b))
        coordinates.append((coordinates[1][0] + self.side_size_c * cos(angle), coordinates[1][1] + self.side_size_c * sin(angle)))
        coordinates.append((self.side_size_d * cos(angle),self.side_size_d * sin(angle)))
        return coordinates
        
    def patch_figure(self):
        coordinates = self.coordinates()
        return Polygon([coordinates[0], coordinates[1], coordinates[2], coordinates[3]],
                        facecolor = self.color, edgecolor = 'black', linewidth = self.border_width, fill = self.filled)
    
    def draw(self):
        if self.check_sides() == False:
            return print('Этот четырехугольник нельзя постороить.')
        super().draw()

    def __del__(self):
        print('del done')