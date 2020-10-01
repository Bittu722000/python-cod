def disemwovel(n):
    string=""
    for i in tuple(n):
        if i not in ['a','e','i','o','u','A','E','I','O','U']:
            string=string+i
    print(string)

n=input()
disemwovel(n)



