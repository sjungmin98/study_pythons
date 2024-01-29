

def home(value):
    html = "<body> It is home. </body>"
    return html

def error(value):
    html = "<body> Error occurred </body>"
    return html
#항시 응답하는 프로그램
while True:
    work, value = input("업무 / 해당값").split()
    print("work: {}, value: {}".format(work, value))
    if work == 'home':
        result = home(value)
        print(result)
    else:
        error(value)
        result = error
        print(result)


