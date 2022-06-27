str = "niraj narwade"

def rename(str):            # this str is local for function any modification will not reflect outside
    print(str)
    str = "narwade niraj"
rename(str)
print(str)