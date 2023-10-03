import numpy as np
import matplotlib.pyplot as plt

class Triangle:
    def __init__(self, v1, v2, v3):
        self.x_batch = []
        self.y_batch = []
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.batch_size = 20
        self.gen_class()

    def gen_class(self):
        for i in range(self.batch_size):
            r1 = np.random.uniform(0, 1)
            r2 = np.random.uniform(0, 1)
            if r1 + r2 > 1:
                r1, r2 = 1 - r1, 1 - r2

            x = (1-r1-r2)*self.v1[0] + r1*self.v2[0] + r2*self.v3[0]
            y = (1-r1-r2)*self.v1[1] + r1*self.v2[1] + r2*self.v3[1]

            self.x_batch.append(x)
            self.y_batch.append(y)

    def get_batch_data(self):
        return self.x_batch, self.y_batch

    def get_class_data(self):
        return self.v1, self.v2, self.v3

classes = []
colors = ['yellow', 'pink', 'black', 'blue', 'purple', 'red', 'green']

try:
    with open('data/class_tr.txt', 'r') as data:
        counter = 0
        for line in data:
            values = line.split(' ')
            values[-1] = values[-1].replace('\n', '')
            v1 = (float(values[0]), float(values[1]))
            v2 = (float(values[2]), float(values[3]))
            v3 = (float(values[4]), float(values[5]))
            classes.append(Triangle(v1, v2, v3))
            counter += 1

except FileNotFoundError:
    print('File not found! Manual data input...\n')
    counter = int(input('Class quantity = '))
    for i in range(counter):
        print(f'Class {counter + 1}\n')
        v1 = tuple(map(float, input('v1 (x, y) = ').split()))
        v2 = tuple(map(float, input('v2 (x, y) = ').split()))
        v3 = tuple(map(float, input('v3 (x, y) = ').split()))
        classes.append(Triangle(v1, v2, v3))

result = open('data/data_batch.txt', 'w')
for i in range(counter):
    x_dat, y_dat = classes[i].get_batch_data()
    v1, v2, v3 = classes[i].get_class_data()
    result.write(f"Class {i + 1}\n")
    result.write(f"Class Info: {v1}, {v2}, {v3}\n")
    for j in range(len(x_dat)):
        result.write(f"{x_dat[j]}, {y_dat[j]}; ")
    result.write('\n')
    plt.scatter(x_dat, y_dat, c=colors[i])
    plt.plot([v1[0], v2[0]], [v1[1], v2[1]], color=colors[i])
    plt.plot([v2[0], v3[0]], [v2[1], v3[1]], color=colors[i])
    plt.plot([v3[0], v1[0]], [v3[1], v1[1]], color=colors[i])

result.close()

plt.grid(color='lightgray', linestyle='--')
plt.show()
