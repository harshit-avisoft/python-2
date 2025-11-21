scores={"math":40}
extra= {"eng": 20}

record =(scores,extra)
record[0]["math"]+=10
temp=({"sci":30},)
record= record+temp
scores["math"]+=20
extra["eng"]=extra["eng"]*2
# extra["eng"]=extra["eng"]*2

record[2]["sci"]+=10

print(record)
print(scores)