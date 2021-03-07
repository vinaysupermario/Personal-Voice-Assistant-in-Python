import wolframalpha

client = wolframalpha.Client('8REQUG-YQ7JGY96T8')

while True:
    output = ""
    query = str(input("Query : "))
    result = client.query(query)
    try:
        output = next(result.results).text
    except:
        pass
    if output:
        print(output)
    else:
        print(result)
