import time
import zipfile

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Target found, return the index
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found

def bruteForce(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if numbers[i] + numbers[j] == target:
                return True
    return False

def binarySum(numbers, target_numbers):
    numbers.sort()  # Sort the list in ascending order (O(nlogn) time)

    for target in target_numbers:
        for num in numbers:
            complement = target - num
            if binary_search(numbers, complement):
                return True
    return False


def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result

def extract_zip(zip_file_path, extract_to_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)

def read_txt_from_zip(zip_file_path, folder_inside_zip):
    txt_contents_dict = {}
    txtSol = {}

    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        # Get the list of files in the specified folder inside the ZIP archive
        file_list = [name for name in zip_file.namelist() if name.startswith(folder_inside_zip)]

        # Read the contents of TXT files and create a list for each file
        for file_name in file_list:
            if file_name.lower().endswith('.txt') and not file_name.lower().__contains__('wsol') and not file_name.lower().__contains__('1000000'):
                if file_name.lower().__contains__('nsol'):
                    with zip_file.open(file_name) as txt_file:
                        txtSol[file_name] = [int(line) for line in txt_file.read().decode('utf-8').splitlines()]
                else:
                    with zip_file.open(file_name) as txt_file:
                        txt_contents_dict[file_name] = [int(line) for line in txt_file.read().decode('utf-8').splitlines()]

    return txtSol, txt_contents_dict

def main():
    zip_file_path = r'C:\Users\fsaul\Downloads\hw2.zip'
    folder_inside_zip = 'hw2/CollectionNumbers'
    
    # Read data from the ZIP file
    txt_sol, txt_contents = read_txt_from_zip(zip_file_path, folder_inside_zip)
    
    # Iterate over the files and compare algorithms
    for file_name, numbers in txt_contents.items():
        target_numbers = txt_sol.get(file_name.replace('.txt', '-nsol.txt'), [])  # Get the corresponding target numbers

        print(f"File: {file_name}")
        print("Size of numbers list:", len(numbers))
        print("Target numbers:", target_numbers)

        # Brute-force
        brute_force_time, brute_force_result = measure_time(bruteForce, numbers, target_numbers)
        print(f"Brute-force Time: {brute_force_time:.6f} seconds")
    
        # Binary search
        binary_search_time, binary_search_result = measure_time(binarySum, numbers, target_numbers)
        print(f"Binary Search Time: {binary_search_time:.6f} seconds")
        

        print("-" * 50)

if __name__ == "__main__":
    main()
