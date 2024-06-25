name  = "Fariz"
batch = 101
fee = 1245.6578
#traditionally how we do this:
inputstring = "Saya" + name + ",welcome to python class" + str(batch)
print(inputstring)

#special
inputstring = f"Hello {name:^40s}, welcome to python class {batch}"
print(inputstring)

#aligh
inputstring = f"Hello {name:>40s}, welcome to python class {batch}"
print(inputstring)

#heading
# inputstring = f"Hello {name:*.40}, welcome to python class {batch}"
# print(inputstring)

# inputstring = f"Hello {name:.3}, welcome to python class {batch:10d}"
# print(inputstring)

inputstring = f"Hello {name}, welcome to python class {batch} in KL for RM{fee:3.3f}"
print(inputstring)

inputstring = f"Hello {name}, welcome to python class {batch} in KL for RM{fee:16.3f}"
print(inputstring)

inputstring = f"Hello {name}, welcome to python class {batch:b} in KL for RM{fee:16.3f}"
print(inputstring)

inputstring = f"Hello {name}, welcome to python class {batch:b} in KL for RM{fee:,.3f}"
print(inputstring)