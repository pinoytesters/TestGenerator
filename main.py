
def generate_tests(all_fields):
    print("Processing ... ")
    pass


field_types = "A. Text\nB. Single Select\nC. Multi Select \nX. No more fields\n"
fields = []
field = ""

while field != "X":
    field = input(f"Select input field: \n{field_types}").upper()
    if field == "A":
        field_name = input("Enter field name: ")
        min_length = input("Enter field min length: ")
        max_length = input("Enter field max length: ")
        current_field = {"Type": "Text", "Name": field_name, "MinLength": min_length, "MaxLength": max_length}
        fields.append(current_field)  
    elif field == "B":
        field_name = input("Enter field name: ")
        field_options = input("Enter options (separated by comma): ")
        field_options = field_options.split(",")
        current_field = {"Type": "Single", "Name": field_name, "Options": field_options}
        fields.append(current_field)  

    elif field == "C":
        field_name = input("Enter field name: ")
        field_options = input("Enter options (separated by comma): ")
        field_options = field_options.split(",")
        current_field = {"Type": "Multiple", "Name": field_name, "Options": field_options}
        fields.append(current_field)  

print(fields)
generate_tests(fields)