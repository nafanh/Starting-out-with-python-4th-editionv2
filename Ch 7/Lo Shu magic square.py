# def magic_sq(square):
#     for row in range(len(square)):
#         total = 0
#         for col in range(len(square)):
#             total += square[row][col]
#
a = [[4,9,2],[3,5,7],[8,1,6]]
def magic_square(a):
    for row in range(len(a)):
        total_r = 0
        for col in range(len(a)):
            total_r += a[row][col]
        if total_r != 15:
            return False

    for col in range(len(a)):
        total_c = 0
        for row in range(len(a)):
            total_c += a[col][row]
        if total_c != 15:
            return False

    total_rd = 0
    for i in range(len(a)):
        total_rd += a[i][i]
    if total_rd != 15:
        return False

    total_ld = 0
    for i in range(len(a),0,-1):
        total_ld += a[len(a)-i][i-1]
    if total_ld != 15:
        return False
    return True

def main():
    print(magic_square(a))
main()


