#задание 1

byte_string = b'r\xc3\xa9sum\xc3\xa9'
decoded_string = byte_string.decode('utf-8')
print("Декодированная строка:", decoded_string)
latin1_bytes = decoded_string.encode('latin1')
print("Байтовое значение в кодировке Latin1:", latin1_bytes)
decoded_latin1_string = latin1_bytes.decode('latin1')
print("Декодированная строка из байтового значения в кодировке Latin1:", decoded_latin1_string)


