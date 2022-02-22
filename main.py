## 필요한 패키지 import 하기
import numpy as np
import matplotlib.pyplot as plt

from tvtk.api import tvtk, write_data

## Skull dataset 불러오기
sz = (68, 256, 256)

name_data = "Skull.vol"

fid = open(name_data, "rb")
data = np.fromfile(fid, dtype=np.uint8)
data = data[28:]

data = np.reshape(data, sz)

## numpy2vtk
spacing = (1, 1, 1)
origin = (0, 0, 0)

vtk_data = tvtk.ImageData(spacing=spacing, origin=origin, dimensions=sz)
vtk_data.point_data.scalars = data.ravel(order='F')
vtk_data.point_data.scalars.name = "Skull_python"

write_data(vtk_data, "Skull_python_spacing_111.vtk")

## ioahKwon
