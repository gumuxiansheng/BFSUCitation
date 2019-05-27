# *- coding:utf-8 -*-

"""
    Author: Mike Zhu
    Bibliometric indicators calculation, refer to https://home.mikezhu.cn/paper-read/BibliometricsIndicators
"""
import numpy as np
import pandas as pd


def prepare_data():
    data_frame = pd.read_excel(u'./data/山东财经大学sci2016.xls', header=28)
    data_frame = data_frame.iloc[0:, :]
    reference_info = list(data_frame[u'合计引用次数'])
    return reference_info


works = prepare_data()


# h-index
def cal_h_index():
    i = 0
    for info in sorted(works, reverse=True):
        i += 1
        if info < i:
            return i - 1


h_index = cal_h_index()


# A-indices
def a_indices():
    return sum(works[0:h_index - 1]) / float(h_index)


# R-indices
def r_indices():
    return sum(works[0:h_index - 1]) ** 0.5


# Rm-indices
def rm_indices():
    return sum(np.sqrt(works[0:h_index - 1])) ** 0.5


# A-index
def a_index():
    print sum(works[0:h_index - 1])
    return sum(works[0:h_index - 1]) / float(h_index) ** 2


# V-index
def v_index():
    return h_index / float(len(works))


# e-index
def e_index():
    return np.sqrt(sum(works[0:h_index - 1]) - h_index ** 2)


# k-index
def k_index():
    return sum(works) * sum(works[0:h_index - 1]) / float((len(works) * (sum(works) - sum(works[0:h_index - 1]))))


# h-square-lower-index
def h_square_lower_index():
    return 100 * sum(works[h_index:]) / float(sum(works))


# h-square-center-index
def h_square_center_index():
    return 100 * (h_index ** 2) / float(sum(works))


# h-square-upper-index
def h_square_upper_index():
    return 100 * (sum(works) - len(works) * h_index) / float(sum(works))


j_index_delta_h = [500, 250, 100, 50, 25, 10, 5, 4, 3, 2, 1.5, 1.25]
j_index_weight = [1, 0.5, 0.333, 0.25, 0.2, 0.167, 0.143, 0.125, 0.111, 0.1, 0.091, 0.083]


# j-index
def j_index():
    n = []
    result = 0
    for i in range(0, 12):
        thresh = h_index * j_index_delta_h[i]
        for j in range(0, len(works)):
            if works[j] < thresh:
                n.append(j)
                break
            else:
                pass

        result += j_index_weight[i] * n[i] * thresh / float(sum(j_index_weight))

    return result


# h_rat index
def h_rat_index():
    i = 0
    x = 0
    for info in sorted(works, reverse=True):
        i += 1
        if info < (h_index + 1):
            x += h_index + 1 - info
        if i >= h_index + 1:
            break
    print x
    return (h_index + 1) - x / float(2 * h_index + 1)


# h_r index
def h_r_index():
    return ((h_index + 1) * works[h_index - 1] - h_index * works[h_index]) / float(
        1 - works[h_index] + works[h_index - 1])


# Maxprod = max{r( j)*c( j)}
def max_prod():
    max_num = 0
    for i in range(0, len(works)):
        if (i + 1) * works[i] > max_num:
            max_num = (i + 1) * works[i]

    return max_num


# h^(2) = max{j : c( j) >= j^2}
def h_square():
    max_num = 0
    for i in range(0, len(works)):
        if works[i] > (i + 1) ** 2:
            max_num = i + 1
    return max_num


# w= max{j : c( j) >= 10 j and c( j +1) <10( j +1)}
def w_index():
    max_num = 0
    for i in range(0, len(works) - 1):
        if (works[i] >= (i + 1) * 10) and (works[i + 1] < 10 * (i + 2)):
            max_num = i + 1
    return max_num


# h_w = (sum_{0}^{r0}(c(j))) ** 0.5, r0 = max{j: TCj/h<=c(j)}
def h_w_index():
    r0 = 0
    for i in range(0, len(works)):
        tc_j = sum(works[0:i + 1])
        if tc_j / h_index <= works[i]:
            r0 = i + 1

    h_w = sum(works[0:r0]) ** 0.5
    return h_w


# pi = 0.01 * TC_{P_pi}
def pi_index():
    P_pi = int(len(works) ** 0.5)
    pi = 0.01 * sum(works[0:P_pi])
    return pi


# h_mock = (TC_n ** 2 / N)**(1/3)
def h_mock_index():
    tc_n = sum(works)
    n = len(works)
    h_mock = (tc_n ** 2 / n) ** (1.0 / 3.0)
    return h_mock


# g = max{j: TC_j/j >= j and TC_{j+1} / (j+1)<= j+1}
def g_index():
    g = 0
    for i in range(0, len(works) - 1):
        tc_j = sum(works[0:(i + 1)])
        tc_j_1 = sum(works[0:(i + 2)])
        if (tc_j / (i + 1) >= (i + 1)) and (tc_j_1 / (i + 2) <= (i + 2)):
            g = i + 1

    return g


def g_rat_index():
    g = g_index()
    tc_g_1 = sum(works[0:g + 2])
    g_rat = g + 1 - ((g + 1) ** 2 - tc_g_1) / (2 * g + 1)
    return g_rat


def g_r_index():
    g = g_index()
    tc_g = sum(works[0:g + 1])
    g_r = 0.5 * works[g] + (tc_g + 0.25 * (works[g]) ** 2 - g * works[g]) ** 0.5
    return g_r


def f_index():
    f = 0
    c_array = np.array(works)
    c_array = 1.0 / c_array

    for i in range(0, len(c_array) - 1):
        tc_j = sum(c_array[0:(i + 1)]) / (i + 1)
        if 1 / tc_j >= (i + 1):
            f = i + 1

    return f


def t_index():
    t = 0
    c_array = np.array(works)
    c_array = np.log(c_array)

    for i in range(0, len(c_array) - 1):
        tc_j = sum(c_array[0:(i + 1)]) / (i + 1)
        if np.exp(tc_j) >= (i + 1):
            t = i + 1

    return t


def hg_index():
    g = g_index()
    hg = (h_index * g) ** 0.5

    return hg


def get_normalized_citations():
    c_array = np.array(works)
    return c_array / float(max(c_array))


def tc_f_index():
    c_array = get_normalized_citations()
    tc_f = sum(c_array)
    return tc_f

#
# def ar_index():
#     c_array = np.array(sufe_works)
#     y_array = np.array(sufe_years)
#     ar_array = (c_array / (y_array - 2005.0))
#     print (ar_array)
#     ar = sum(ar_array[:h_index]) ** 0.5
#     return ar
#
#
# # hc = max{hc : Sc ( j) >= hc and Sc ( j +1) < hc}
# def hc_index():
#     c_array = np.array(sufe_works)
#     y_array = np.array(sufe_years)
#     sc_array = 4.0 * (1.0 / (2018 - y_array + 1)) * c_array
#     max_num = 0
#     for i in range(0, len(sc_array) - 1):
#         if (sc_array[i] >= sc_array[i + 1]) and sc_array[i] > max_num:
#             max_num = sc_array[i]
#
#     return max_num
#
#
# # ht = max{ht : St ( j) >= ht and St ( j +1) < ht}
# def ht_index():
#     c_array = np.array(sufe_works)
#     y_array = np.array(sufe_years)
#     sc_array = (4.0 * sum((2018 - y_array + 1)))
#     max_num = 0
#     for i in range(0, len(sc_array) - 1):
#         if (sc_array[i] >= sc_array[i + 1]) and sc_array[i] > max_num:
#             max_num = sc_array[i]
#
#     return max_num
