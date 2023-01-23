superscript_list = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']


def superscript(num):
    output = ''
    for i in str(num):
        output += superscript_list[int(i)]
    return output
