import pandas as pd
import tensorflow as tf
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense, LSTM, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam


# class Predict_model():
#     def __init__(self, data):
#         self.data = data
#
#     def create_dataset(self, dataset, look_back):
#         X_train, Y_train = [], []
#         for i in range(len(dataset) - look_back):
#             X_train.append(dataset[i:(i + look_back)])
#             Y_train.append(dataset[look_back + i:look_back + i + 1])
#         return np.array(X_train), np.array(Y_train)
#
#     def load_data(self):
#         data1 = self.data[['time', 'ph', 'cod', 'nh4']]
#
#         data1.drop(0, inplace=True)
#         data['time'] = pd.to_datetime(data1['time'], format='%Y-%m-%d')
#         data1 = data1.set_index(['time'])
#
#         data1.drop(index=(data1.loc[(data1['ph'] == '停运')].index), inplace=True)
#
#         ph_data = data1.iloc[:, [0]].values
#         cod_data = data1.iloc[:, [1]].values
#         nh4_data = data1.iloc[:, [2]].values
#         look_back = 720
#         # cod_data = data1.iloc[:, [1]].values
#         #         # nh4_data = data1.iloc[:, [2]].values
#
#         sc = MinMaxScaler(feature_range=[0, 1])
#
#         ph_set = sc.fit_transform(ph_data)
#         ph_test, ph1_test = self.create_dataset(ph_set, look_back)
#         ph_model = tf.keras.models.load_model("pre_model/my_model")
#         predict_ph = ph_model.predict(ph_test)
#         pre_result_ph = sc.inverse_transform(predict_ph)
#         print('aaaaaaaaaaaaa', pre_result_ph)
#
#         cod_set = sc.fit_transform(cod_data)
#         cod_test, cod1_test = self.create_dataset(cod_set, look_back)
#         cod_model = tf.keras.models.load_model("pre_model/my_model1")
#         predict_cod = cod_model.predict(cod_test)
#         pre_result_cod = sc.inverse_transform(predict_cod)
#
#         print('bbbbbbbbbbbbbbbbbbb', pre_result_cod)
#
#         nh4_set = sc.fit_transform(nh4_data)
#         nh4_test, nh41_test = self.create_dataset(nh4_set, look_back)
#         nh4_model = tf.keras.models.load_model("pre_model/my_model2")
#         predict_nh4 = nh4_model.predict(nh4_test)
#         pre_result_nh4 = sc.inverse_transform(predict_nh4)
#
#         print('ccccccccccccccc', pre_result_nh4)
#
#         # return pre_result_ph, pre_result_cod, pre_result_nh4
#         return pre_result_cod, pre_result_nh4

# def create_dataset(dataset, look_back):
#     X_train, Y_train = [], []
#     for i in range(len(dataset) - look_back):
#         X_train.append(dataset[i:(i + look_back)])
#         Y_train.append(dataset[look_back + i:look_back + i + 1])
#     return np.array(X_train), np.array(Y_train)
#
#
# def load_data_ph(data):
#     data1 = data[['time', 'ph', 'cod', 'nh4']]
#
#     data1.drop(0, inplace=True)
#     data['time'] = pd.to_datetime(data1['time'], format='%Y-%m-%d')
#     data1 = data1.set_index(['time'])
#
#     data1.drop(index=(data1.loc[(data1['ph'] == '停运')].index), inplace=True)
#
#     ph_data = data1.iloc[:, [0]].values
#
#     look_back = 720
#     # cod_data = data1.iloc[:, [1]].values
#     #         # nh4_data = data1.iloc[:, [2]].values
#
#     sc = MinMaxScaler(feature_range=[0, 1])
#
#     ph_set = sc.fit_transform(ph_data)
#     ph_test, ph1_test = create_dataset(ph_set, look_back)
#     ph_model = tf.keras.models.load_model("pre_model/my_model")
#     predict_ph = ph_model.predict(ph_test)
#     pre_result_ph = sc.inverse_transform(predict_ph)
#     # print('aaaaaaaaaaaaa', pre_result_ph)
#
#     # return pre_result_ph, pre_result_cod, pre_result_nh4
#     return pre_result_ph
#
#
# def load_data_cod(data):
#     data1 = data[['time', 'ph', 'cod', 'nh4']]
#
#     data1.drop(0, inplace=True)
#     data['time'] = pd.to_datetime(data1['time'], format='%Y-%m-%d')
#     data1 = data1.set_index(['time'])
#
#     data1.drop(index=(data1.loc[(data1['ph'] == '停运')].index), inplace=True)
#
#     ph_data = data1.iloc[:, [1]].values
#
#     look_back = 720
#     # cod_data = data1.iloc[:, [1]].values
#     #         # nh4_data = data1.iloc[:, [2]].values
#
#     sc = MinMaxScaler(feature_range=[0, 1])
#
#     ph_set = sc.fit_transform(ph_data)
#     ph_test, ph1_test = create_dataset(ph_set, look_back)
#     ph_model = tf.keras.models.load_model("pre_model/my_model")
#     predict_ph = ph_model.predict(ph_test)
#     pre_result_ph = sc.inverse_transform(predict_ph)
#     # print('aaaaaaaaaaaaa', pre_result_ph)
#
#     # return pre_result_ph, pre_result_cod, pre_result_nh4
#     return pre_result_ph
#
#
# def load_data_nh4(data):
#     data1 = data[['time', 'ph', 'cod', 'nh4']]
#
#     data1.drop(0, inplace=True)
#     data['time'] = pd.to_datetime(data1['time'], format='%Y-%m-%d')
#     data1 = data1.set_index(['time'])
#
#     data1.drop(index=(data1.loc[(data1['ph'] == '停运')].index), inplace=True)
#
#     ph_data = data1.iloc[:, [2]].values
#
#     look_back = 720
#     # cod_data = data1.iloc[:, [1]].values
#     #         # nh4_data = data1.iloc[:, [2]].values
#
#     sc = MinMaxScaler(feature_range=[0, 1])
#
#     ph_set = sc.fit_transform(ph_data)
#     ph_test, ph1_test = create_dataset(ph_set, look_back)
#     ph_model = tf.keras.models.load_model("pre_model/my_model")
#     predict_ph = ph_model.predict(ph_test)
#     pre_result_ph = sc.inverse_transform(predict_ph)
#     # print('aaaaaaaaaaaaa', pre_result_ph)
#
#     # return pre_result_ph, pre_result_cod, pre_result_nh4
#     return pre_result_ph


# def change_dateframe(ph, cod, nh4):
#     c = {
#         'ph': ph,
#         'cod': cod,
#         'nh4': nh4,
#     }
#     return c


class Predict_model():
    def __init__(self, data):
        self.data = data

    def create_dataset(self, dataset, look_back):
        X_train, Y_train = [], []
        for i in range(len(dataset) - look_back):
            X_train.append(dataset[i:(i + look_back)])
            Y_train.append(dataset[look_back + i:look_back + i + 1])
        return np.array(X_train), np.array(Y_train)

    def load_data(self):
        data1 = self.data[['time', 'ph', 'cod', 'nh4']]

        data1.drop(0, inplace=True)
        data1['time'] = pd.to_datetime(data1['time'], format='%Y-%m-%d')
        data1 = data1.set_index(['time'])

        data1.drop(index=(data1.loc[(data1['ph'] == '停运')].index), inplace=True)
        #
        ph_data = data1.iloc[:, [0]].values

        look_back = 24
        # cod_data = data1.iloc[:, [1]].values
        #         # nh4_data = data1.iloc[:, [2]].values

        sc = MinMaxScaler(feature_range=[0, 1])

        ph_set = sc.fit_transform(ph_data)
        ph_test, ph1_test = self.create_dataset(ph_set, look_back)
        ph_model = tf.keras.models.load_model("pre_model/my_model")
        predict_ph = ph_model.predict(ph_test)
        pre_result_ph = sc.inverse_transform(predict_ph)
        # print('aaaaaaaaaaaaa', pre_result_ph)

        # return pre_result_ph, pre_result_cod, pre_result_nh4
        return pre_result_ph


class Predict_model1():
    def __init__(self, data):
        self.data = data

    def create_dataset(self, dataset, look_back):
        X_train, Y_train = [], []
        for i in range(len(dataset) - look_back):
            X_train.append(dataset[i:(i + look_back)])
            Y_train.append(dataset[look_back + i:look_back + i + 1])
        return np.array(X_train), np.array(Y_train)

    def load_data(self):
        data1 = self.data[['time', 'ph', 'cod', 'nh4']]

        data1.drop(0, inplace=True)
        data1['time'] = pd.to_datetime(data1['time'], format='%Y-%m-%d')
        data1 = data1.set_index(['time'])
        # if data1.loc[(data1['ph'] == '停运')]:
        data1.drop(index=(data1.loc[(data1['ph'] == '停运')].index), inplace=True)

        cod_data = data1.iloc[:, [1]].values

        look_back = 24
        # cod_data = data1.iloc[:, [1]].values
        #         # nh4_data = data1.iloc[:, [2]].values

        sc = MinMaxScaler(feature_range=[0, 1])

        cod_set = sc.fit_transform(cod_data)
        cod_test, cod1_test = self.create_dataset(cod_set, look_back)
        cod_model = tf.keras.models.load_model("pre_model/my_model1")
        predict_cod = cod_model.predict(cod_test)
        pre_result_cod = sc.inverse_transform(predict_cod)

        # print('bbbbbbbbbbbbbbbbbbb', pre_result_cod)

        # return pre_result_ph, pre_result_cod, pre_result_nh4
        return pre_result_cod


class Predict_model2():
    def __init__(self, data):
        self.data = data

    def create_dataset(self, dataset, look_back):
        X_train, Y_train = [], []
        for i in range(len(dataset) - look_back):
            X_train.append(dataset[i:(i + look_back)])
            Y_train.append(dataset[look_back + i:look_back + i + 1])
        return np.array(X_train), np.array(Y_train)

    def load_data(self):
        data1 = self.data[['time', 'ph', 'cod', 'nh4']]

        data1.drop(0, inplace=True)
        data1['time'] = pd.to_datetime(data1['time'], format='%Y-%m-%d')
        data1 = data1.set_index(['time'])
        # if data1.loc[(data1['ph'] == '停运')]:
        #     data1.drop(index=(data1.loc[(data1['ph'] == '停运')].index), inplace=True)
        data1.drop(index=(data1.loc[(data1['ph'] == '停运')].index), inplace=True)
        #
        nh4_data = data1.iloc[:, [2]].values
        look_back = 24
        # cod_data = data1.iloc[:, [1]].values
        #         # nh4_data = data1.iloc[:, [2]].values

        sc = MinMaxScaler(feature_range=[0, 1])

        nh4_set = sc.fit_transform(nh4_data)
        nh4_test, nh41_test = self.create_dataset(nh4_set, look_back)
        nh4_model = tf.keras.models.load_model("pre_model/my_model2")
        predict_nh4 = nh4_model.predict(nh4_test)
        pre_result_nh4 = sc.inverse_transform(predict_nh4)

        # print('ccccccccccccccc', pre_result_nh4)

        # return pre_result_ph, pre_result_cod, pre_result_nh4
        return pre_result_nh4


class Change_data():
    def __init__(self, time, ph, cod, nh4):
        self.time = time
        self.ph = ph
        self.cod = cod
        self.nh4 = nh4

    def change_dateframe(self):
        c = {
            'time': self.time,
            'ph': self.ph,
            'cod': self.cod,
            'nh4': self.nh4,
        }
        c = pd.DataFrame(c)

        return c


if __name__ == '__main__':
    # change_data(ph, cod, nh4)

    data = pd.read_excel('兴辰钒钛外排口.xls', sheet_name="监测数据报表")  # 读取excel表
    data.dropna(inplace=True)
    # print(data)
    time = data['监测时间'].values.tolist()
    ph = data['PH值'].values.tolist()
    cod = data['化学需氧量(COD)(毫克/升)'].values.tolist()
    nh4 = data['氨氮(毫克/升)'].values.tolist()
    # c = {"time": time,
    # "ph": ph,
    # "cod": cod,
    # "nh4": nh4,
    # }  # 将列表a，b转换成字典
    data1 = Change_data(time, ph, cod, nh4).change_dateframe()

    # print(data1)
    # Predict(data1)
    pre = Predict_model(data1).load_data()
    pre1 = Predict_model1(data1).load_data()
    pre2 = Predict_model2(data1).load_data()
    # a, b, c = pre.load_data()
    # a = pre.load_data()
    # b = pre1.load_data()
    # c = pre2.load_data()
    print('aaaaaa', pre[-24:])
    print('bbbbbb', pre1[-24:])
    print('cccccc', pre2[-24:])

    print('dddddddd', pre[:, 0])

    list_data = []
    for x, y, z in zip(pre[:, 0], pre1[:, 0], pre[:, 0]):
        dict_temp = {}

        dict_temp['ph'] = x
        dict_temp['cod'] = y
        dict_temp['nh4'] = z
        list_data.append(dict_temp)

    print(list_data)
