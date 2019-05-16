import numpy as np

johns_works = [127, 84, 75, 73, 70, 69, 62, 57, 53, 43, 39, 36, 33, 33, 32, 22, 21, 16, 15, 14, 11, 10, 10, 9, 9, 9,
               9, 8, 8, 8, 8, 6, 5, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0, 0, 0]
johns_years = [2010, 2015, 2007, 2011, 2013, 2010, 2010, 2006, 2013, 2010, 2008, 2006, 2012, 2006, 2009, 2008, 2014,
               2011, 2009, 2015, 2010, 2017, 2007, 2014, 2012, 2012, 2007, 2017, 2015, 2013, 2010, 2015, 2015, 2017,
               2017, 2013, 2012, 2018, 2011, 2017, 2017, 2018, 2018, 2017, 2010, 2006]
h_index = 17


# A-indices
def a_indices():
    return sum(johns_works[0:h_index - 1]) / float(h_index)


# R-indices
def r_indices():
    return sum(johns_works[0:h_index - 1])**0.5


# Rm-indices
def rm_indices():
    return sum(np.sqrt(johns_works[0:h_index - 1]))**0.5


# Maxprod = max{r( j)*c( j)}
def max_prod():
    max_num = 0
    for i in range(0, len(johns_works)):
        if (i + 1) * johns_works[i] > max_num:
            max_num = (i + 1) * johns_works[i]

    return max_num


# h^(2) = max{j : c( j) >= j^2}
def h_square():
    max_num = 0
    for i in range(0, len(johns_works)):
        if johns_works[i] > (i + 1) ** 2:
            max_num = i + 1
    return max_num


# w= max{j : c( j) >= 10 j and c( j +1) <10( j +1)}
def w_index():
    max_num = 0
    for i in range(0, len(johns_works) - 1):
        if (johns_works[i] >= (i + 1) * 10) and (johns_works[i + 1] < 10 * (i + 2)):
            max_num = i + 1
    return max_num


# h_w = (sum_{0}^{r0}(c(j))) ** 0.5, r0 = max{j: TCj/h<=c(j)}
def h_w_index():
    r0 = 0
    for i in range(0, len(johns_works)):
        tc_j = sum(johns_works[0:i + 1])
        if tc_j / h_index <= johns_works[i]:
            r0 = i + 1

    h_w = sum(johns_works[0:r0]) ** 0.5
    return h_w


# pi = 0.01 * TC_{P_pi}
def pi_index():
    P_pi = int(len(johns_works) ** 0.5)
    pi = 0.01 * sum(johns_works[0:P_pi])
    return pi


# h_mock = (TC_n ** 2 / N)**(1/3)
def h_mock_index():
    tc_n = sum(johns_works)
    n = len(johns_works)
    h_mock = (tc_n ** 2 / n) ** (1.0 / 3.0)
    return h_mock


# g = max{j: TC_j/j >= j and TC_{j+1} / (j+1)<= j+1}
def g_index():
    g = 0
    for i in range(0, len(johns_works) - 1):
        tc_j = sum(johns_works[0:(i + 1)])
        tc_j_1 = sum(johns_works[0:(i + 2)])
        if (tc_j / (i + 1) >= (i + 1)) and (tc_j_1 / (i + 2) <= (i + 2)):
            g = i + 1

    return g


def g_rat_index():
    g = g_index()
    tc_g_1 = sum(johns_works[0:g + 2])
    g_rat = g + 1 - ((g + 1) ** 2 - tc_g_1) / (2 * g + 1)
    return g_rat


def g_r_index():
    g = g_index()
    tc_g = sum(johns_works[0:g + 1])
    g_r = 0.5 * johns_works[g] + (tc_g + 0.25 * (johns_works[g]) ** 2 - g * johns_works[g]) ** 0.5
    return g_r


def f_index():
    f = 0
    c_array = np.array(johns_works)
    c_array = 1.0 / c_array

    for i in range(0, len(c_array) - 1):
        tc_j = sum(c_array[0:(i + 1)]) / (i + 1)
        if 1 / tc_j >= (i + 1):
            f = i + 1

    return f


def t_index():
    t = 0
    c_array = np.array(johns_works)
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
    c_array = np.array(johns_works)
    return c_array / (sum(c_array) / len(c_array))


def tc_f_index():
    c_array = get_normalized_citations()
    tc_f = sum(c_array)
    return tc_f


def ar_index():
    c_array = np.array(johns_works)
    y_array = np.array(johns_years)
    ar_array = (c_array/(y_array - 2005.0))
    print (ar_array)
    ar = sum(ar_array[:h_index]) ** 0.5
    return ar


# hc = max{hc : Sc ( j) >= hc and Sc ( j +1) < hc}
def hc_index():
    c_array = np.array(johns_works)
    y_array = np.array(johns_years)
    sc_array = 4.0 * (1.0 / (2018 - y_array + 1)) * c_array
    max_num = 0
    for i in range(0, len(sc_array) - 1):
        if (sc_array[i] >= sc_array[i + 1]) and sc_array[i] > max_num:
            max_num = sc_array[i]

    return max_num


# ht = max{ht : St ( j) >= ht and St ( j +1) < ht}
def ht_index():
    c_array = np.array(johns_works)
    y_array = np.array(johns_years)
    sc_array = (4.0 * sum((2018 - y_array + 1)))
    max_num = 0
    for i in range(0, len(sc_array) - 1):
        if (sc_array[i] >= sc_array[i + 1]) and sc_array[i] > max_num:
            max_num = sc_array[i]

    return max_num



