# Question 4
def is_an_ip_number(str_):
    if str_.isdigit():
        number = int(str_)
        return 0 <= number <= 255
    return False


def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")

    return len(dot_separated_words) == 4 and all(
        is_an_ip_number(word) for word in dot_separated_words)


print(is_dot_separated_ip_address('192.168.127.12'))
print(is_dot_separated_ip_address('256.255.255.255'))
