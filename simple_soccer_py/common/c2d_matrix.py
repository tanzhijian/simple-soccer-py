import math
import typing

from .vector2d import Vector2D


class Matrix:
    def __init__(self):
        self._m11 = 0.0
        self._m12 = 0.0
        self._m13 = 0.0

        self._m21 = 0.0
        self._m22 = 0.0
        self._m23 = 0.0

        self._m31 = 0.0
        self._m32 = 0.0
        self._m33 = 0.0


class C2DMatrix:
    """2D Matrix class"""

    def __init__(self):
        self._matrix = Matrix()
        self.identity()

    def __repr__(self):
        return (
            "Matrix:\n"
            f"{self._matrix._m11:.4f} {self._matrix._m12:.4f} {self._matrix._m13:.4f}\n"
            f"{self._matrix._m21:.4f} {self._matrix._m22:.4f} {self._matrix._m23:.4f}\n"
            f"{self._matrix._m31:.4f} {self._matrix._m32:.4f} {self._matrix._m33:.4f}\n"
        )

    def identity(self):
        """create an identity matrix"""
        self._matrix._m11 = 1.0
        self._matrix._m12 = 0.0
        self._matrix._m13 = 0.0

        self._matrix._m21 = 0.0
        self._matrix._m22 = 1.0
        self._matrix._m23 = 0.0

        self._matrix._m31 = 0.0
        self._matrix._m32 = 0.0
        self._matrix._m33 = 1.0

    def translate(self, x: float, y: float) -> None:
        """create a transformation matrix"""
        mat = Matrix()

        mat._m11 = 1
        mat._m12 = 0
        mat._m13 = 0

        mat._m21 = 0
        mat._m22 = 1
        mat._m23 = 0

        mat._m31 = x
        mat._m32 = y
        mat._m33 = 1

        # and multiply
        self.matrix_multiply(mat)

    def scale(self, x_scale: float, y_scale: float) -> None:
        """create a scale matrix"""
        mat = Matrix()

        mat._m11 = x_scale
        mat._m12 = 0
        mat._m13 = 0

        mat._m21 = 0
        mat._m22 = y_scale
        mat._m23 = 0

        mat._m31 = 0
        mat._m32 = 0
        mat._m33 = 1

        # and multiply
        self.matrix_multiply(mat)

    def rotate_by_angle(self, rotation: float) -> None:
        """create a rotation matrix"""
        # 创建旋转矩阵的代码
        mat = Matrix()
        sin = math.sin(rotation)
        cos = math.cos(rotation)

        mat._m11 = cos
        mat._m12 = sin
        mat._m13 = 0

        mat._m21 = -sin
        mat._m22 = cos
        mat._m23 = 0

        mat._m31 = 0
        mat._m32 = 0
        mat._m33 = 1

        # and multiply
        self.matrix_multiply(mat)

    def rotate_by_vectors(self, fwd: Vector2D, side: Vector2D) -> None:
        """create a rotation matrix from a fwd and side 2D vector"""
        # 从 fwd 和 side 2D 向量创建旋转矩阵的代码
        mat = Matrix()

        mat._m11 = fwd.x
        mat._m12 = fwd.y
        mat._m13 = 0

        mat._m21 = side.x
        mat._m22 = side.y
        mat._m23 = 0

        mat._m31 = 0
        mat._m32 = 0
        mat._m33 = 1

        # and multiply
        self.matrix_multiply(mat)

    def transform_vector2ds(self, *points: Vector2D) -> None:
        """applys a transformation matrix to points"""
        for point in points:
            temp_x = (
                self._matrix._m11 * point.x
                + self._matrix._m21 * point.y
                + self._matrix._m31
            )
            temp_y = (
                self._matrix._m12 * point.x
                + self._matrix._m22 * point.y
                + self._matrix._m32
            )
            point.x = temp_x
            point.y = temp_y

    def matrix_multiply(self, m_in: Matrix) -> None:
        """multiply two matrices together"""
        mat_temp = Matrix()

        # first row
        mat_temp._m11 = (
            (self._matrix._m11 * m_in._m11)
            + (self._matrix._m12 * m_in._m21)
            + (self._matrix._m13 * m_in._m31)
        )
        mat_temp._m12 = (
            (self._matrix._m11 * m_in._m12)
            + (self._matrix._m12 * m_in._m22)
            + (self._matrix._m13 * m_in._m32)
        )
        mat_temp._m13 = (
            (self._matrix._m11 * m_in._m13)
            + (self._matrix._m12 * m_in._m23)
            + (self._matrix._m13 * m_in._m33)
        )

        # second
        mat_temp._m21 = (
            (self._matrix._m21 * m_in._m11)
            + (self._matrix._m22 * m_in._m21)
            + (self._matrix._m23 * m_in._m31)
        )
        mat_temp._m22 = (
            (self._matrix._m21 * m_in._m12)
            + (self._matrix._m22 * m_in._m22)
            + (self._matrix._m23 * m_in._m32)
        )
        mat_temp._m23 = (
            (self._matrix._m21 * m_in._m13)
            + (self._matrix._m22 * m_in._m23)
            + (self._matrix._m23 * m_in._m33)
        )

        # third
        mat_temp._m31 = (
            (self._matrix._m31 * m_in._m11)
            + (self._matrix._m32 * m_in._m21)
            + (self._matrix._m33 * m_in._m31)
        )
        mat_temp._m32 = (
            (self._matrix._m31 * m_in._m12)
            + (self._matrix._m32 * m_in._m22)
            + (self._matrix._m33 * m_in._m32)
        )
        mat_temp._m33 = (
            (self._matrix._m31 * m_in._m13)
            + (self._matrix._m32 * m_in._m23)
            + (self._matrix._m33 * m_in._m33)
        )

        self._matrix = mat_temp
