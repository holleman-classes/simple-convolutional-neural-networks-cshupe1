# -*- coding: utf-8 -*-
"""HW#2_Problem_1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DIZrItxtOLR6rTKAQaf2ZsWsweW3o727
"""

# Define parameters for each layer
layers = [
    {"name": "Conv2D", "filters": 32, "kernel_size": 3, "stride": 2, "padding": "same"},
    {"name": "BatchNorm"},
    {"name": "Conv2D", "filters": 64, "kernel_size": 3, "stride": 2, "padding": "same"},
    {"name": "BatchNorm"},
    {"name": "Conv2D", "filters": 128, "kernel_size": 3, "stride": 2, "padding": "same"},
    {"name": "BatchNorm"},
    {"name": "Conv2D", "filters": 128, "kernel_size": 3, "padding": "same"},
    {"name": "BatchNorm"},
    {"name": "Conv2D", "filters": 128, "kernel_size": 3, "padding": "same"},
    {"name": "BatchNorm"},
    {"name": "Conv2D", "filters": 128, "kernel_size": 3, "padding": "same"},
    {"name": "BatchNorm"},
    {"name": "Conv2D", "filters": 128, "kernel_size": 3, "padding": "same"},
    {"name": "BatchNorm"},
    {"name": "MaxPooling", "pool_size": 4, "stride": 4},
    {"name": "Flatten"},
    {"name": "Dense", "units": 128},
    {"name": "BatchNorm"},
    {"name": "Dense", "units": 10}
]

# Function to calculate parameters for Conv2D layer
def calc_conv_params(filters, kernel_size, input_channels=3):
    return (kernel_size ** 2) * input_channels * filters + filters

# Function to calculate output size for Conv2D layer
def calc_conv_output_size(input_size, kernel_size, stride, padding="valid"):
    if padding == "same":
        output_size = input_size // stride
    else:
        output_size = ((input_size - kernel_size) // stride) + 1
    return output_size

# Function to calculate parameters for Dense layer
def calc_dense_params(input_units, output_units):
    return input_units * output_units + output_units

# Calculate and print results for each layer
for layer in layers:
    layer_name = layer["name"]
    if layer_name == "Conv2D":
        filters = layer["filters"]
        kernel_size = layer["kernel_size"]
        stride = layer.get("stride", 1)
        padding = layer.get("padding", "valid")
        params = calc_conv_params(filters, kernel_size)
        output_size = calc_conv_output_size(32, kernel_size, stride, padding)
        mac_ops = filters * kernel_size ** 2 * output_size ** 2
    elif layer_name == "Dense":
        units = layer["units"]
        params = calc_dense_params(128, units) if units == 128 else calc_dense_params(128, 10)
        output_size = units
        mac_ops = 128 * units
    elif layer_name == "MaxPooling":
        pool_size = layer["pool_size"]
        stride = layer["stride"]
        output_size = 1
        params = 0
        mac_ops = 0
    else:
        params = 0
        mac_ops = 0
        output_size = 128 if layer_name == "Flatten" else 10
    print(f"Layer: {layer_name}, Parameters: {params}, MAC Operations: {mac_ops}, Output Size: {output_size}")