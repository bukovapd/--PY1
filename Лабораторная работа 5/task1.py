# TODO решить с помощью list comprehension и распечатать его
from print_1 import print_1
 dict_ = [{'bin': bin(i),'dec': i,'hex': hex(i),'oct': oct(i)} for i in range(16)]
 print_1(dict_)