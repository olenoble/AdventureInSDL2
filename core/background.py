

class BackGround:
    def __init__(self, image, grid_size, height, width):
        self.image = image
        self.grid_size = grid_size
        self.height = height
        self.width = width

    def draw(self, display):
        for bg_x in range(int(self.width / self.grid_size)):
            for bg_y in range(int(self.height / self.grid_size)):
                display.draw(self.image, bg_x * self.grid_size, bg_y * self.grid_size)
