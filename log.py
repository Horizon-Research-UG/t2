# log.py - Modular Logging System
# "The best way to find out if you can trust somebody is to trust them." - Ernest Hemingway

# Import required modules for file operations, JSON handling, datetime, and path operations
import json  # Line 4: For parsing and writing JSON format log data
import os    # Line 5: For file path operations and checking file existence
import datetime  # Line 6: For timestamp generation in log entries
import inspect   # Line 7: For getting caller file information (name and path)

# Hardcoded log file name as specified in requirements (line reference: read-then-code line 15)
LOG_FILE_NAME = "log.txt"  # Line 10: Variable containing hardcoded log file name

def get_caller_info():
    """
    Function to get information about the file that called this module
    Returns: tuple containing (file_name, file_path)
    Reference: requirements 2.1 and 2.2 from read-then-code
    """
    # Get the current stack frame to find caller information
    stack = inspect.stack()  # Line 18: Get call stack to identify calling file
    
    # Get caller frame (index 2: 0=current, 1=log_run, 2=actual caller)
    caller_frame = stack[2]  # Line 21: Extract frame of actual calling file
    
    # Extract full file path from caller frame
    file_path = caller_frame.filename  # Line 24: Get complete path to calling file
    
    # Extract just the filename from the full path
    file_name = os.path.basename(file_path)  # Line 27: Extract filename from full path
    
    # Return both pieces of information as tuple
    return file_name, file_path  # Line 30: Return filename and path as specified

def read_current_runs():
    """
    Function to read existing run count from log file
    Returns: integer representing total number of previous runs
    Reference: read-then-code line 17-18 (reads sum of all calls)
    """
    # Check if log file exists before attempting to read
    if not os.path.exists(LOG_FILE_NAME):  # Line 39: Check file existence to avoid errors
        # Return 0 if file doesn't exist (first run)
        return 0  # Line 41: Return zero runs if log file not found
    
    try:
        # Open and read the existing log file
        with open(LOG_FILE_NAME, 'r', encoding='utf-8') as file:  # Line 45: Open log file for reading
            # Parse JSON content from log file
            log_data = json.load(file)  # Line 47: Load JSON data from log file
            # Return the total runs count from JSON data
            return log_data.get('total_runs', 0)  # Line 49: Extract total_runs, default to 0
    except (json.JSONDecodeError, KeyError, FileNotFoundError):
        # Return 0 if any error occurs during file reading
        return 0  # Line 52: Return zero if any parsing error occurs

def save_log_entry(runs, file_name, file_path):
    """
    Function to save log entry with runs count, filename, and filepath
    Parameters: runs (int), file_name (str), file_path (str)
    Reference: read-then-code lines 25-29 (saves runs, name, path to log file)
    """
    # Create timestamp for current log entry
    timestamp = datetime.datetime.now().isoformat()  # Line 61: Generate ISO format timestamp
    
    # Create new log entry dictionary with all required information
    new_entry = {  # Line 64: Start building new log entry object
        "timestamp": timestamp,  # Line 65: Add timestamp to log entry
        "run_number": runs,      # Line 66: Add current run number to entry
        "file_name": file_name,  # Line 67: Add calling filename to entry
        "file_path": file_path   # Line 68: Add calling file path to entry
    }  # Line 69: Complete new log entry object construction
    
    # Initialize log data structure
    log_data = {  # Line 72: Start building complete log data structure
        "total_runs": runs,  # Line 73: Set total runs count in log data
        "entries": []        # Line 74: Initialize empty entries list for log history
    }  # Line 75: Complete initial log data structure
    
    # Read existing log data if file exists
    if os.path.exists(LOG_FILE_NAME):  # Line 78: Check if log file already exists
        try:
            # Open and read existing log file content
            with open(LOG_FILE_NAME, 'r', encoding='utf-8') as file:  # Line 81: Open existing log file
                # Load existing JSON data from file
                log_data = json.load(file)  # Line 83: Parse existing log data from file
        except (json.JSONDecodeError, FileNotFoundError):
            # Use default structure if file is corrupted or missing
            pass  # Line 86: Continue with default structure if read fails
    
    # Update total runs count in log data
    log_data["total_runs"] = runs  # Line 89: Update total runs to current count
    
    # Insert new entry at the beginning (most recent at top as per requirements)
    log_data["entries"].insert(0, new_entry)  # Line 92: Insert new entry at top of list
    
    # Write updated log data back to file
    with open(LOG_FILE_NAME, 'w', encoding='utf-8') as file:  # Line 95: Open log file for writing
        # Save JSON data with pretty formatting for readability
        json.dump(log_data, file, indent=2, ensure_ascii=False)  # Line 97: Write formatted JSON to file

def log_run():
    """
    Main function to execute complete logging process
    This function can be called from other files and directories
    Reference: read-then-code line 21 (modular usage in other files/folders)
    """
    # Read current total runs count from existing log file
    current_runs = read_current_runs()  # Line 106: Get existing run count from log file
    
    # Increment runs counter by 1 as specified in requirements
    runs = current_runs + 1  # Line 109: Increment run count by 1 (runs += 1)
    
    # Get information about the calling file (name and path)
    file_name, file_path = get_caller_info()  # Line 112: Extract caller file information
    
    # Save all information to log file with most recent entry at top
    save_log_entry(runs, file_name, file_path)  # Line 115: Save complete log entry to file
    
    print(f"Log updated: Run {runs} from {file_name}")  # Line 117: Print confirmation message
    # Return the current run number for potential use by calling code

    print("\n"*2)
    print("_______________________________")

    return runs  # Line 118: Return current run number to caller

# Module can be used by importing and calling log_run() function
# Example usage: import log; log.log_run()
# Reference: read-then-code line 21 (modular usage specification)


if __name__ == "__main__":  # Check if the script is being run directly
    log_run()  # Call log_run() if this module is executed directly