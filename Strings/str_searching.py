def main(str):
    print(" your entered string \n\n",str)
    print(" is this str starts with good :",str.startswith("good"))
    print(" is this str ends with thon :",str.endswith("thon"))
    print(" find:",str.find('ython'))
    print(" count:",str.count("0"))

main("good start in python")