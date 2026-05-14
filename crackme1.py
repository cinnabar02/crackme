import base64


def hex_to_bytes(hex_str):
    return list(bytes.fromhex(hex_str))


unk_405060 = hex_to_bytes(
    "DF90C0A17B2EFC2A7BB340A50879607E81C9C7B9336CBA3C9BF54473620364C9C344D319A3152C20A3D719A4EA824DF7D7C9BC4A78C8C860B398D5504D1CA1BF37A83914029055E9B13E60D25413D49DF22C611C17C726582E74E87A37E8F7848C211A258B813EF446CAAFBED068356BD576E7D45184D50E"
)
unk_4050E0 = hex_to_bytes(
    "BFF621FF406220DC25051F0577D1CACDEDA421BCE062BD21EB745FE55A16F0898256D3AAD70769C8E3EE607B3AF8E7FFE8A7B288CD2A4EABEB83733D010CDBE27BA4A0F846352902A6DECD5CF8EB435AE3584FE6DA8A65DF88F221D6205CC91AD5B18AC4342BCA3A14793862956F60E11E7B2D0604EE8A43"
)

byte_404020 = [
    0x6D,
    0x42,
    0x0B,
    0x81,
    0x5F,
    0x0B,
    0xF9,
    0xF5,
    0xC7,
    0x45,
    0x58,
    0x1B,
    0x28,
    0xA0,
    0x78,
    0x35,
    0x9A,
    0xEC,
    0xED,
    0x71,
    0x65,
    0x27,
    0x14,
    0x83,
    0x6A,
    0x21,
    0xB4,
    0x8C,
    0xF9,
    0x6E,
    0x76,
    0x02,
    0x2A,
    0xC7,
    0x59,
    0x1A,
    0x96,
    0xFF,
    0xE1,
    0x30,
    0x67,
    0x34,
    0x31,
    0x8E,
    0x69,
    0x27,
    0x14,
    0x83,
    0x6A,
    0x21,
    0xB4,
    0x8C,
    0xF9,
    0x6E,
]


def inverted_sub_401679():
    data = list(byte_404020)

    for r in range(11, -1, -1):
        start = r * 10
        round_key = [unk_405060[i] ^ unk_4050E0[i] for i in range(start, start + 10)]

        for i in range(len(data)):
            data[i] ^= round_key[i % 10]

    b64_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    res_b64 = "".join(chr(b) for b in data if chr(b) in b64_alphabet)

    while len(res_b64) % 4 != 0:
        res_b64 += "="

    return res_b64


def inverted_sub_4017D2(b64_string):
    try:
        return base64.b64decode(b64_string).decode("utf-8")
    except Exception as e:
        return f"Ошибка декодирования: {e}"


final_b64 = inverted_sub_401679()
print(f"{inverted_sub_4017D2(final_b64)}")
