# cython: language_level=3

cimport libc.stdint

import numpy

__all__ = (
    'repeated_swap',
)


def repeated_swap(profile, swap_count):
    """Repeatedly swap profile values.

    Parameters
    ----------
    profile : numpy.ndarray
        An equilibrium frequency matrix.
    swap_count : numpy.ndarray
        The number of swaps to perform for each mutation site.
    """
    cdef double[:, :] profile_view = profile
    cdef libc.stdint.int64_t[:] step_count_view = swap_count
    cdef int swap_index = 0
    cdef int column_size = profile.shape[1]
    cdef long total_count = swap_count.sum()
    swap_list = numpy.zeros((total_count, 2), dtype='i8')
    swap_list[:, 0] = numpy.random.randint(column_size, size=total_count)
    swap_list[:, 1] = numpy.random.randint(column_size - 1, size=total_count)
    swap_list[swap_list[:, 1] >= swap_list[:, 0], 1] += 1
    cdef libc.stdint.int64_t[:, :] swap_list_view = swap_list
    cdef int i, j1, j2
    cdef double tmp
    for i in range(profile.shape[0]):
        for __ in range(step_count_view[i]):
            j1 = swap_list_view[swap_index, 0]
            j2 = swap_list_view[swap_index, 1]
            tmp = profile_view[i, j1]
            profile_view[i, j1] = profile_view[i, j2]
            profile_view[i, j2] = tmp
            swap_index += 1
