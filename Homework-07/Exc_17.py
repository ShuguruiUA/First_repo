def encode_repeated_data(input_str, start_index=0):
    if start_index == len(input_str):
        return []

    current_char = input_str[start_index]
    count = 1

    # Check for consecutive repeated characters
    while start_index + count < len(input_str) and input_str[start_index + count] == current_char:
        count += 1

    # Recursively process the rest of the string
    rest_of_result = encode_repeated_data(input_str, start_index + count)

    # Create a key-value pair and add it to the result
    result = [(current_char, count)]
    result.extend(rest_of_result)

    return result

# Example usage
input_string = "aaabbcccdd"
result_list = encode_repeated_data(input_string)
print(result_list)


def encode(data):
    def recur(start_index=0):
        if start_index == len(data):
            return []
        current_char = data[start_index]
        count = 1
        
        while start_index + count < len(data) and data[start_index + count] == current_char:
            count += 1
            
        counting_chars = recur(start_index + count)
        
        result = [current_char, count]
        result.extend(counting_chars)
        
        return result
    return recur()

data = "XXXZZXXYYYZZ"

print(encode(data))