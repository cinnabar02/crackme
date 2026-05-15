def ctypes_int32(val):
    return val & 0xFFFFFFFF


def solve_keygen():
    v5 = 0xD6035192
    v6 = 0xA5BA2D3B
    v7 = 0x0A409BAB
    v8 = 0x000006EC

    v10 = 0  # v10 = strtoul(&::String, 0i64, 16); у нас String это не Hex-число

    for r in range(v8):

        tmp_x = ctypes_int32(v5 ^ 0x82A34C31)
        v12 = ctypes_int32(v7 + 730913689) ^ tmp_x

        v14 = ctypes_int32(tmp_x + 1084439911)

        v13 = ctypes_int32(v14 ^ (v12 >> 3))

        v6_old = ctypes_int32(ctypes_int32(v6 ^ 0x3B8282EE) - v13)

        v5_old = ctypes_int32(ctypes_int32(v12 - 513126785) ^ v6_old)

        v7_old = ctypes_int32(ctypes_int32(v13 ^ v12) - 989527920)

        v5 = v5_old
        v6 = v6_old
        v7 = v7_old

    flag = f"{v5:08X}-{v6:08X}-{v7:08X}-{v8:08X}"
    print(f"{flag}")


if __name__ == "__main__":
    solve_keygen()
