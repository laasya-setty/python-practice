# Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, width=max_width)
    
 # fill is shorthanf for "\n".join(wrap(text, ...))   

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)