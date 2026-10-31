import numpy as np

# Example 1: reshape()
arr1 = np.arange(1, 13)
print("Reshape:\n", arr1.reshape(3, 4))

# Example 2: Reshape 2D
arr2 = np.arange(1, 13)
print("2x6:\n", arr2.reshape(2, 6))

# Example 3: Reshape 3D
arr3 = np.arange(1, 25)
print("3D:\n", arr3.reshape(2, 3, 4))

# Example 4: Automatic Dimension (-1)
arr4 = np.arange(1, 13)
print("Auto Shape:\n", arr4.reshape(3, -1))

# Example 5: flatten()
arr5 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("Flatten:", arr5.flatten())

# Example 6: ravel()
print("Ravel:", arr5.ravel())

# Example 7: Transpose
print("Transpose:\n", arr5.T)

# Example 8: transpose()
print("Transpose Function:\n", np.transpose(arr5))

# Example 9: swapaxes()
print("Swapaxes:\n", np.swapaxes(arr5, 0, 1))

# Example 10: expand_dims()
arr6 = np.array([1, 2, 3])
print("Expand Axis 0:\n", np.expand_dims(arr6, axis=0))
print("Expand Axis 1:\n", np.expand_dims(arr6, axis=1))

# Example 11: squeeze()
arr7 = np.array([[[1, 2, 3]]])
print("Squeeze:", np.squeeze(arr7))

# Example 12: resize()
arr8 = np.array([1, 2, 3, 4])
print("Resize:\n", np.resize(arr8, (2, 3)))

# Example 13: flip()
arr9 = np.array([10, 20, 30, 40])
print("Flip:", np.flip(arr9))

# Example 14: flipud()
arr10 = np.array([
    [1, 2],
    [3, 4]
])
print("Flip Up Down:\n", np.flipud(arr10))

# Example 15: fliplr()
print("Flip Left Right:\n", np.fliplr(arr10))

# Example 16: roll()
arr11 = np.array([1, 2, 3, 4, 5])
print("Roll:", np.roll(arr11, 2))

# Example 17: rot90()
print("Rotate 90:\n", np.rot90(arr10))

# Example 18: moveaxis()
arr12 = np.zeros((2, 3, 4))
result = np.moveaxis(arr12, 0, -1)
print("Moveaxis Shape:", result.shape)

# Example 19: swapaxes() 3D
arr13 = np.zeros((2, 3, 4))
result = np.swapaxes(arr13, 0, 2)
print("Swapaxes Shape:", result.shape)