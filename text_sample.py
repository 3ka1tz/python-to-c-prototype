def cipher_text(text_bytes, shift):
    result = bytearray(text_bytes)

    for i in range(len(result)):
        char = result[i]

        if 65 <= char <= 90:
            result[i] = (char - 65 + shift) % 26 + 65
 
        elif 97 <= char <= 122:
            result[i] = (char - 97 + shift) % 26 + 97

    return bytes(result)
