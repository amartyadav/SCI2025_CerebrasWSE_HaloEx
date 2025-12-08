#!/usr/bin/env cs_python

import argparse
import json
import numpy as np

from cerebras.sdk.runtime.sdkruntimepybind import SdkRuntime, MemcpyDataType, MemcpyOrder # pylint: disable=no-name-in-module

# Read arguments
parser = argparse.ArgumentParser()
parser.add_argument('--name', help="the test compile output dir")
parser.add_argument('--cmaddr', help="IP:port for CS system")
args = parser.parse_args()

# Get matrix dimensions from compile metadata
with open(f"{args.name}/out.json", encoding='utf-8') as json_file:
  compile_data = json.load(json_file)
  

# Construct a runner using SdkRuntime
runner = SdkRuntime(args.name, cmaddr=args.cmaddr)

# Get symbols for A, x, y on device
grid_symbol = runner.get_id('grid')
# subgrid_symbol = runner.get_id('subgrid')
dest_arr_right_symbol = runner.get_id('ptr_dest_arr_right')
dest_arr_left_symbol = runner.get_id('ptr_dest_arr_left')


# Load and run the program
runner.load()
runner.run()


# Matrix dimensions
N = int(compile_data['params']['N'])
M = int(compile_data['params']['M'])


# Launch the compute function on device
runner.launch('compute', nonblock=False)

for pe_x in range(4):
    for pe_y in range(4):
        grid_result = np.zeros([M*N], dtype=np.float32)
        runner.memcpy_d2h(grid_result, grid_symbol, pe_x, pe_y, 1, 1, M*N, streaming=False,
          order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)
        print("=== PE({0},{1})===".format(pe_x, pe_y))
        print(grid_result.reshape(M,N))
        print("\n\n")
        
        dest_arr_right = np.zeros([M], dtype=np.float32);
        runner.memcpy_d2h(dest_arr_right, dest_arr_right_symbol, pe_x, pe_y, 1, 1, M, streaming=False,
          order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)
        print("--- dest_arr_right---")
        print(dest_arr_right)
        print("\n\n")
        
        
        dest_arr_left = np.zeros([M], dtype=np.float32);
        runner.memcpy_d2h(dest_arr_left, dest_arr_left_symbol, pe_x, pe_y, 1, 1, M, streaming=False,
          order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)
        print("--- dest_arr_left---")
        print(dest_arr_left)
        print("\n\n")
        
        


# Stop the program
runner.stop()
print("SUCCESS!")