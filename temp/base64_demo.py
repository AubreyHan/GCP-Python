import base64

def base64_str(smaple_str:str):
    base64_output=base64.b64encode(smaple_str.encode('utf-8'))
    return base64_output

def base64_file(sample_file:str):
    with open(sample_file,'rb') as fi:
        base64_output=base64.b64encode(fi.read())
    return base64_output


output=base64_file('/home/gcpvm/gcp/sample/1')

print(output)