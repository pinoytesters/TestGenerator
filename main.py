
def generate_tests(all_fields):
    print("Processing ... ")
    for test_field in all_fields:
        print(test_field["Type"])
        if test_field["Type"] == "Text":
            print("... This is a text")
        elif test_field["Type"] == "Single":
            print("... This is a single option")
        elif test_field["Type"] == "Multiple":
            print("... This is a multiple option")
    pass


field_types = "A. Text\nB. Single Select\nC. Multi Select \nX. No more fields\n"
fields = []

### TODO: Revert field value
field = "X" # field = ""


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

### TODO: Remove Samples 
field_name = "Text1"
min_length = "10"
max_length = "100"
current_field = {"Type": "Text", "Name": field_name, "MinLength": min_length, "MaxLength": max_length}
fields.append(current_field)  

field_name = "Single1"
field_options = "single_option1, single_option2, single_option3"
field_options = field_options.split(",")
current_field = {"Type": "Single", "Name": field_name, "Options": field_options}
fields.append(current_field)  

field_name = "Multi1"
field_options = "multi_option1, multi_option2, multi_option3"
field_options = field_options.split(",")
current_field = {"Type": "Multiple", "Name": field_name, "Options": field_options}
fields.append(current_field)  

generate_tests(fields)