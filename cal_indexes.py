johns_works = [127, 84, 75, 73, 70, 69, 62, 57, 53, 43, 39, 36, 33, 33, 32, 22, 21, 16, 15, 14, 11, 10, 10, 9, 9, 9,
               9, 8, 8, 8, 8, 6, 5, 4, 3, 3, 3, 2, 2, 1, 1, 0, 0, 0, 0, 0]
h_index = 17


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
        tc_j = sum(johns_works[0:i])
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

