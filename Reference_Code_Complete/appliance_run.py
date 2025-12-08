import json
import os
import numpy as np
from cerebras.appliance.pb.sdk.sdk_common_pb2 import MemcpyDataType, MemcpyOrder
from cerebras.sdk.client import SdkRuntime


OUTPUT_FILE = "cerebras_summary.txt"
outfile = open(OUTPUT_FILE, 'w')

# Read the artifact_path from the JSON file
with open("artifact_path.json", "r", encoding="utf8") as f:
    data = json.load(f)
    artifact_path = data["artifact_path"]
    
# Instantiate a runner object using a context manager.
# Set simulator=False if running on CS system within appliance.
with SdkRuntime(artifact_path, simulator=False) as runner:
    # Launch the compute function on device
    runner.launch('compute', nonblock=False)
    M = 6
    N = 6
    np.set_printoptions(threshold=np.inf)   
    # Get symbols (memory addresses) for the data structures on the device
    # These symbols allow the host to copy data to/from the device.
    grid_symbol = runner.get_id('grid')
    dest_arr_right_symbol = runner.get_id('ptr_dest_arr_right')
    dest_arr_left_symbol = runner.get_id('ptr_dest_arr_left')
    dest_arr_top_symbol = runner.get_id('ptr_dest_arr_top') # Top row received from south neighbor
    dest_arr_bottom_symbol = runner.get_id('ptr_dest_arr_bottom') # Bottom row received from north neighbor
    
    # Define the PE grid dimensions. The loops below assume a 4x4 PE grid.
    PE_GRID_X_DIM = 4
    PE_GRID_Y_DIM = 4
    
    # Launch the 'compute' function on the device.
    # `nonblock=False` means the host script will wait for the compute kernel to finish.
    runner.launch('compute', nonblock=False)
    
    # Dictionary to store results and original grid for summary
    all_pe_results = {}
    
    # Loop through each Processing Element (PE) in the 4x4 grid to retrieve and compare data
    for pe_x in range(PE_GRID_X_DIM):
        for pe_y in range(PE_GRID_Y_DIM):
            # Initialize results for the current PE
            pe_status = {
                'right': False,
                'left': False,
                'top': False,
                'bottom': False
            }
    
            print(f"\n{'='*20} PE({pe_x},{pe_y}) {'='*20}", file=outfile)
    
            # --- Retrieve and Print the PE's Own Grid Data ---
            device_grid_result = np.zeros([(M+2) * (N+2)], dtype=np.float32)
            runner.memcpy_d2h(device_grid_result, grid_symbol, pe_x, pe_y, 1, 1, ((M+2) * (N+2)), streaming=False,
                              order=MemcpyOrder.ROW_MAJOR, data_type=MemcpyDataType.MEMCPY_32BIT, nonblock=False)
            current_pe_grid_reshaped = device_grid_result.reshape(M+2, N+2)
            print("--- Device PE Grid Data ---", file=outfile)
            print(current_pe_grid_reshaped, file=outfile)
            print("-" * 25, file=outfile)