def parse_and_display_address(address):
    details = address.split(',')

    labels = ["Door-no", "Street", "Area", "City", "State", "Zipcode", "Country"]

    address_dict = {label: detail for label, detail in zip(labels, details)}

    for label, detail in address_dict.items():
        print(f"{label}:{detail}")

input_address = input()
parse_and_display_address(input_address)





#721,12th stage,Gokulam,Mysuru,Karnataka,570002,India