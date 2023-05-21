
def snip_function(function_string):
    for character in function_string:
        if (character == '+') or (character == "-") or (function_string.index(character) == (len(function_string) - 1) ) :
            index = function_string.index(character)
            function_snippet = function_string[: index]
            function_snippet.replace(" ","")
            function_string = function_string[index: ]
            return function_snippet , function_string  





