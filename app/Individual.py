import numpy as np
from PIL import Image, ImageOps, ImageDraw, ImagePath
from PIL import ImageDraw
from IPython.display import display
from colour.difference import delta_E_CIE1976

import matplotlib.pyplot as plt

import random
import math


class Individual:
    def __init__(self, l, w):
        self.l = l
        self.w = w
        self.fitness = float("inf")
        self.array = None
        self.image = None
        self.create_random_image_array()

    def rand_color(self):
        return "#" + "".join([random.choice("0123456789ABCDEF") for j in range(6)])

    def create_one_color(self):
        self.image = Image.new(
            mode="RGBA", size=(self.l, self.w), color=self.rand_color()
        )

    def create_random_image_array(self):
        # number of polygons to add to image
        # the higher this is the higher stochasticity and potential for detail we have
        iterations = random.randint(3, 6)

        region = (self.l + self.w) // 8

        img = Image.new("RGBA", (self.l, self.w), self.rand_color())

        # number of points for each polygon
        for i in range(iterations):
            num_points = random.randint(3, 6)

            region_x = random.randint(0, self.l)
            region_y = random.randint(0, self.w)

            xy = []
            for j in range(num_points):
                xy.append(
                    (
                        random.randint(region_x - region, region_x + region),
                        random.randint(region_y - region, region_y + region),
                    )
                )

            img1 = ImageDraw.Draw(img)
            img1.polygon(xy, fill=self.rand_color())

        self.image = img
        self.array = self.to_array(img)

    def create_random_image_array_2(self):
        self.array = np.random.randint(low=0, high=255, size=(self.l, self.w, 4))
        self.array = self.array.astype("uint8")
        self.image = Image.fromarray(self.array.astype("uint8"))

    def add_shape(self):
        iterations = random.randint(1, 1)

        region = random.randint(1, (self.l + self.w) // 4)

        img = self.image

        for i in range(iterations):
            num_points = random.randint(3, 6)

            region_x = random.randint(0, self.l)
            region_y = random.randint(0, self.w)

            xy = []
            for j in range(num_points):
                xy.append(
                    (
                        random.randint(region_x - region, region_x + region),
                        random.randint(region_y - region, region_y + region),
                    )
                )

            img1 = ImageDraw.Draw(img)
            img1.polygon(xy, fill=self.rand_color())

        self.image = img
        self.array = self.to_array(img)

    def to_image(self):
        im = Image.fromarray(self.array)
        im.show()

    def to_array(self, image):
        return np.array(image)

    def get_fitness(self, target):

        self.fitness = np.mean(delta_E_CIE1976(np.array(target), self.array))

    def get_fitness_euclidean(self, target):
        diff_array = np.subtract(np.array(target), self.array)
        self.fitness = np.mean(np.absolute(diff_array))
