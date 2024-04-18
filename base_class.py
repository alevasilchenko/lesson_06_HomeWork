class GroundWaterBaseModel:  # класс базовой модели потока подземных вод

    def __init__(self, delta_x=1000, delta_y=1000, delta_z=10, kf=1.0, mu=0.1, grad=0.001):
        self.delta_x = delta_x          # размер области моделирования по оси X
        self.delta_y = delta_y          # размер области моделирования по оси Y
        self.delta_z = delta_z          # размер области моделирования по оси Z
        self.kf = kf                    # значение коэффициента фильтрации горной породы (скорость просачивания воды)
        self.mu = mu                    # значение коэффициента водоотдачи горной породы (объем пор)
        self.grad = grad                # градиент подземного потока (величина уклона течения)

    def ground_volume(self):  # расчёт объёма области моделирования
        return self.delta_x * self.delta_y * self.delta_z

    def water_volume(self):  # расчёт величины объёма воды в области моделирования
        return self.ground_volume() * self.mu

    def water_flow(self):  # расчёт объема подземного потока за единицу времени
        return self.ground_volume() * self.kf * self.grad
