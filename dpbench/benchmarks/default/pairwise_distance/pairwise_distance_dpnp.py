# SPDX-FileCopyrightText: 2022 - 2023 Intel Corporation
#
# SPDX-License-Identifier: Apache-2.0

import dpnp as np


def pairwise_distance(X1, X2, D):
    x1 = np.sum(np.square(X1), axis=1, dtype=X1.dtype)
    x2 = np.sum(np.square(X2), axis=1, dtype=X2.dtype)
    np.dot(X1, X2.T, D)
    D *= -2
    x3 = x1.reshape(x1.size, 1)
    np.add(D, x3, D)
    np.add(D, x2, D)
    np.sqrt(D, D)

    np.synchronize_array_data(D)
