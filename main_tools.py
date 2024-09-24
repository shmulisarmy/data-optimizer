
def optomize_data(json_data, scema) -> list:
    optomized_data = []

    for object in json_data:
        optomized_object = []
        for scem in scema:
            if scem not in object:
                optomized_object.append(f"0#")
            else:
                optomized_object.append(f"{len(str(object[scem]))}#{object[scem]}")

        optomized_data.append("".join(optomized_object))


    return optomized_data




def expand_data(optomized_data, scema) -> list:
    regular_data = []
    for object in optomized_data:
        regular_object = []
        current_field_data_string = []

        index = 0
        start_of_length_tag_index = 0
        while index != len(object):
            char = object[index]

            if char == "#":
                field_data_length = int(object[start_of_length_tag_index:index])

                index+=1
                current_field_data_string = object[index:index+field_data_length]
                regular_object.append(current_field_data_string)

                index+=field_data_length

                start_of_length_tag_index = index
            else:
                index+=1

        assert len(scema) == len(regular_object)
        matched_up_object = {scema[i]: regular_object[i] for i in range(len(scema))}


        regular_data.append(matched_up_object)


    return regular_data

