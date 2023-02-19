from cryptography.fernet import Fernet


superscript_list = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']


def superscript(num):
    output = ''
    for i in str(num):
        output += superscript_list[int(i)]
    return output


FERNET = Fernet(b'h5m7Gt2eGlX4PjU_r55Ihk_59-1_ieuEF7Ki-qMpUrU=')
CUTOFF = 15
