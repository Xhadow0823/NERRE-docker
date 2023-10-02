from CUT import cut, input_data_str
from NER_RE import NER_RE

print("start")
cut_result = cut(input_data_str)
print("cut done")
print("start NER and RE")
result = NER_RE(cut_result)
print(result)
print("all done")
