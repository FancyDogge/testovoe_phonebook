def min_steps_to_slices(array_length):
    if array_length <= 1:
        return 0
    elif array_length % 2 == 0:
        return min_steps_to_slices(array_length // 2) + 1
    else:
        return min_steps_to_slices(array_length // 2 + 1) + 1

# Example usage:
array_length = 10
min_steps = min_steps_to_slices(array_length)

print("Minimum Steps:", min_steps)


N = int(input())

def slice_the_roll(arr_len: int) -> None:
    if arr_len == 1:
        return 0
    elif arr_len % 2 == 0:
        return slice_the_roll(arr_len//2) + 1
    else:
        return slice_the_roll(arr_len//2+1) + 1
        
slice_count = slice_the_roll(N)
print(slice_count)

# N = int(input())

# def count_roll_slices(arr_len: int) -> int:
#     if arr_len == 1:
#         return 0
#     elif arr_len % 2 == 0:
#         return count_roll_slices(arr_len//2) + 1
#     else:
#         return count_roll_slices(arr_len//2+1) + 1
        
# slice_count = count_roll_slices(N)
# print(slice_count)