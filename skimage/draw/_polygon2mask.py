import numpy as np

from . import draw


def polygon2mask(image_shape, polygon, offset=None):
    """Compute a mask from polygon.

    Parameters
    ----------
    image_shape : tuple of size 2.
        The shape of the mask.
    polygon : array_like.
        The polygon coordinates of shape (N, 2) where N is
        the number of points.
    offset : tuple  of ints of size 2.
        The pixel offset of the mask.

    Returns
    -------
    mask : 2-D ndarray of type 'bool'.
        The mask that corresponds to the input polygon.

    Notes
    -----
    This function does not do any border checking, so that all
    the vertices need to be within the given shape.

    Examples
    --------
    >>> image_shape = (128, 128)
    >>> polygon = np.array([[60, 100], [100, 40], [40, 40]])
    >>> mask = polygon2mask(image_shape, polygon)
    >>> mask.shape
    (128, 128)
    """
    polygon = np.asarray(polygon)
    vertex_row_coords, vertex_col_coords = polygon.T
    fill_row_coords, fill_col_coords = draw.polygon(
        vertex_row_coords, vertex_col_coords, image_shape, offset)
    if offset is not None:
        image_shape = (image_shape[0] - max(offset[0], 0),
                       image_shape[1] - max(offset[1], 0))
    mask = np.zeros(image_shape, dtype=bool)
    mask[fill_row_coords, fill_col_coords] = True
    return mask
