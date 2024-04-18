from base_class import GroundWaterBaseModel


class GroundWaterModelWithOutFlow(GroundWaterBaseModel):  # класс модели потока подземных вод с водоотбором

    def __init__(self, ground_name='sand', outflow=0.0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ground_name = ground_name  # наименование горной породы (песок, глина и т.п.)
        self.outflow = outflow          # величина водоотбора из области моделирования за единицу времени

    def check_outflow(self):  # проверка возможности заданного водоотбора
        return self.outflow <= self.water_flow()  # водоотбор не должен превышать объем подземного потока
