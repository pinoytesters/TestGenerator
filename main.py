from pprint import pprint

def generate_tests(all_fields):
    # print(all_fields)
    the_matrix = []
    for test_field in all_fields:
        if test_field["Type"] == "Text":
            if len(the_matrix) == 0:
                the_matrix.append(f"{test_field['Name']} Valid")
                the_matrix.append(f"{test_field['Name']} Invalid")
            else:
                the_new_matrix = []
                # print("The Original Matrix")
                # pprint(the_matrix)
                # print("... ... ")
                for n in range(0, len(the_matrix)):
                    # print(f"Processing {n+1} of {len(the_matrix)}...")
                    new_item = []
                    if isinstance(the_matrix[n], list):
                        for fields in the_matrix[n]:
                            new_item.append(fields)
                    else:
                        new_item.append(the_matrix[n])

                    new_item.append(f"{test_field['Name']} Valid")
                    the_new_matrix.append(new_item) 

                    new_item = []
                    if isinstance(the_matrix[n], list):
                        for fields in the_matrix[n]:
                            new_item.append(fields)
                    else:
                        new_item.append(the_matrix[n])

                    new_item.append(f"{test_field['Name']} Invalid")
                    the_new_matrix.append(new_item) 

                the_matrix = the_new_matrix
                # print("The Updated Matrix")
                # pprint(the_matrix)
                # print("... ... ")               

        elif test_field["Type"] == "Single":
            # print("... This is a single select")
            # Single select fields will duplicate each item, and add one test for each option
            if len(the_matrix) == 0:
                # print(test_field)
                for option in test_field["Options"]:
                    # print(option)
                    the_matrix.append(f"{test_field['Name']} : {option}")
            else:
                #########
                the_new_matrix = []
                for n in range(0, len(the_matrix)):
                    # print(f"Processing {n+1} of {len(the_matrix)}...")
                    new_item = []
                    if isinstance(the_matrix[n], list):
                        for fields in the_matrix[n]:
                            new_item.append(fields)
                    else:
                        new_item.append(the_matrix[n])
                    
                    reseter = []
                    for option in test_field["Options"]:
                        reseter = new_item.copy()
                        # print(f"\noption: {option}")
                        # print(f"new item before append: {new_item}") 
                        new_item.append(f"{test_field['Name']} : {option}")
                        # print(f"new  item after append: {new_item}") 
                        # print(f"new matrix before append: {the_new_matrix}") 
                        the_new_matrix.append(new_item)
                        # print(f"new matrix after append: {the_new_matrix}") 
                        new_item = []
                        new_item = reseter
                        # print(f"new item after pop: {new_item}")
                        # print(f"new matrix before loop: {the_new_matrix}")


                    # print("\n\n")
                    # print(f"new matrix before next item: {the_new_matrix}")


                the_matrix = the_new_matrix
                ####

        elif test_field["Type"] == "Multiple":
            print("... This is a multiple select")
            # TODO: Multi select fields will duplicate each item, and add one test for each option, and another for all options
            # TODO: Do we need one more test for testing combinations
    
    print("\n\n\n")
    print("The Complete Matrix")
    print("-------------------")
    pprint(the_matrix)

# Guide
    # t_v
    # t_i

    # t_v + s1
    # t_v + s2
    # t_i + s1
    # t_i + s2

    # t_v + s1 + m1
    # t_v + s1 + m2
    # t_v + s1 + m1 + m2

    # t_v + s2 + m1
    # t_v + s2 + m2
    # t_v + s2 + m1 + m2

    # t_i + s1 + m1
    # t_i + s1 + m2
    # t_i + s1 + m1 + m2

    # t_i + s2 + m1
    # t_i + s2 + m2
    # t_i + s2 + m1 + m2

    # text_v, single1, multi1
    # text_v, single2, multi2
    # text_v, single1, multi1, multi2
    # text_v, single2, multi1, multi2
    # text_i, single1, multi1 
    # text_i, single2, multi2
    # text_i, single1, multi1, multi2
    # text_i, single2, multi1, multi2


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
if 1 == 1:

    field_name = "Text1"
    min_length = "10"
    max_length = "100"
    current_field = {"Type": "Text", "Name": field_name, "MinLength": min_length, "MaxLength": max_length}
    fields.append(current_field)  

    # field_name = "Text3"
    # min_length = "25"
    # max_length = "250"
    # current_field = {"Type": "Text", "Name": field_name, "MinLength": min_length, "MaxLength": max_length}
    # fields.append(current_field)  

    field_name = "Single1"
    field_options = "single_option1,single_option2,single_option3"
    field_options = field_options.split(",")
    current_field = {"Type": "Single", "Name": field_name, "Options": field_options}
    fields.append(current_field)  

    # field_name = "Single2"
    # field_options = "single_option21,single_option22,single_option23"
    # field_options = field_options.split(",")
    # current_field = {"Type": "Single", "Name": field_name, "Options": field_options}
    # fields.append(current_field)  

    # field_name = "Text2"
    # min_length = "50"
    # max_length = "500"
    # current_field = {"Type": "Text", "Name": field_name, "MinLength": min_length, "MaxLength": max_length}
    # fields.append(current_field)  

    # field_name = "Multi1"
    # field_options = "multi_option1, multi_option2, multi_option3"
    # field_options = field_options.split(",")
    # current_field = {"Type": "Multiple", "Name": field_name, "Options": field_options}
    # fields.append(current_field)  

generate_tests(fields)
