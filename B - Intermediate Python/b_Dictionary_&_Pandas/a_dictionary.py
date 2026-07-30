# ------- Dictionary -------
# --------------------------
# [1] Dictionary items writen with enclosed curly braces 
# [2] Dictionary items are contain key : value 
# [3] Dictionary key need to be immutable => (Number , string, tuples[])List not allowed
# [4] Dictionary value can have any data type
# [5] Dictionary key need to be unique 
# [6] Dictionary is not ardered you access its elements with key 
# --------------------------
User = {"Name":"Joseph Botros","Age": 19,"Country": "Egypt"}
print(User)
print(f"{User['Name']} and his age is {User['Age']} \nhis county is : {User['Country']}")
print(User.keys())
print(User.values())

# Two dimensional dict
languages = {
    "one": {"language":"English","Type":"Book","Number of bages":333 },
    "two": {"language":"Germany","Type":"Book","Number of bages":350 },
    "three":{"language":"French","Type":"Book","Number of bages":360 }
}
print(languages['one'].values())
print(languages['two'].keys())
print(languages['one']['Type'])