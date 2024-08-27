import json
import pycountry
import csv
import re


def update_dict(row_dict, final):
    """
    Updates the 'final' dictionary with the data from 'row_dict'. This function
    organizes data by domain, country, and region, and appends entries
    accordingly.

    :param row_dict: A dictionary containing data from a row of input.
    :param final: A dictionary to update with parsed data.
    """
    domain = row_dict.get("domain")  # Get domain from the row
    country = row_dict.get("country_name")  # Get country name from the row

    # If country name is missing or blank, try using country code
    if not country.strip():
        country_short = row_dict.get("country_code", "")  # Get country code
        if country_short:  # Check if country code exists
            # Convert country code to country name using pycountry library
            country = pycountry.countries.get(
                alpha_2=country_short.upper()
            )
            if country:  # If country object is found, get its name
                country = country.name

    if country:
        country = country.title()  # Capitalize the first letter of each word

    # Get category or categories from the row
    # category is for google, categories for facebook
    category = row_dict.get("category", row_dict.get("categories", ""))

    # Extract other details from the row
    name = row_dict["name"]
    phone = row_dict["phone"]
    address = row_dict["address"]
    region_name = row_dict["region_name"].title()  # Capitalize region name

    # Create an element dictionary with extracted details
    elem = {
        "name": name,
        "phone": phone,
        "category": category,
        "address": address,
    }

    # Check if the domain already exists in the final dictionary
    if domain in final:
        # Check if the country exists under the domain in the final dictionary
        if country in final[domain]:
            # Check if the region exists under the country in the final dictionary
            if region_name in final[domain][country]:
                # Append the element to the existing region list
                final[domain][country][region_name].append(elem)
            else:
                # Create a new region entry with the element
                final[domain][country][region_name] = [elem]
        else:
            # Create a new country entry with the region and element
            final[domain][country] = {region_name: [elem]}
    else:
        # Create a new domain entry with the country, region, and element
        final[domain] = {
            country: {
                region_name: [elem]
            }
        }


def get_elem(str_arg, keys):
    """
    Extracts elements from a string `str_arg` based on a list of `keys` and
    returns a dictionary where the keys are from the `keys` list and the values
    are the extracted substrings from `str_arg`.

    :param str_arg: The input string to be parsed.
    :param keys: A list of keys that will be used as dictionary keys.
    :return: A dictionary containing the parsed elements or -1 if parsing fails.
    """
    index = 0  # Initialize the index for iterating over keys
    elm = {}  # Initialize an empty dictionary to store extracted elements

    while index < len(keys):  # Loop until all keys have been processed
        if not str_arg:
            # If the input string is empty or None, return -1 indicating a failure
            return -1

        if str_arg[0] == '"':
            # If the string starts with a double quote, set the splitter to '",'
            if str_arg[1] == ',':
                # If there is a comma right after the opening quote, skip it
                str_arg = str_arg[1:]
            splitter = '",'
        else:
            # If there is no starting quote, use ',' as the splitter
            splitter = ','

        try:
            # Try to find the index of the splitter in the string
            end_string = str_arg.index(splitter)
        except ValueError:
            # If the splitter is not found, take the rest of the string as the value
            var = str_arg
            end_string = 0
        else:
            # If the splitter is found, extract the substring up to the splitter
            var = str_arg[len(splitter) - 1:end_string]

        # Remove the processed part from the input string
        str_arg = str_arg[end_string + len(splitter):]

        # Assign the extracted value to the corresponding key in the dictionary
        elm[keys[index]] = var

        # Move to the next key
        index += 1

    return elm  # Return the dictionary with extracted elements


def get_data(filename):
    """
    Reads a file and processes its contents to return a dictionary of parsed
    data.

    :param filename: The name of the file to be read.
    :return: A dictionary with keys from the file's header and values extracted
             from each line.
    """
    final = {}  # Initialize an empty dictionary to store the final data

    with open(filename, 'r') as file:
        # Open the file in read mode
        keys = []  # Initialize an empty list to store header keys
        last_string = ""  # Variable to handle multi-line data

        for line in file:
            if not keys:
                # If keys are not initialized, read the first line as header keys
                keys = line.strip().split(",")
                continue  # Move to the next line after setting the header keys

            # Remove trailing newline characters and replace escaped quotes
            line_as_string = line.strip().replace('\\"', "'")

            if last_string != '':
                # If `last_string` is not empty, append the current line to it
                line_as_string = last_string + line_as_string

            # Parse the current line using the `get_elem` function
            element = get_elem(line_as_string, keys)

            if element == -1:
                # If `get_elem` returns -1, it means the line is incomplete
                # Accumulate the line in `last_string` to handle multi-line data
                last_string += line_as_string
                continue  # Its done
            else:
                # If parsing is successful, reset `last_string` to empty
                last_string = ""

            # Update the final dictionary with the parsed element
            update_dict(element, final)

    # Return the fully populated dictionary after processing all lines
    return final


def get_data_website(file_path):
    final = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        # Initialize the CSV reader with specified delimiter and quote character
        reader = csv.reader(file, delimiter=';', quotechar='"',
                            skipinitialspace=True)

        # Get the header from the first row
        header = next(reader)

        # Clean the header to remove any extra quotes and spaces
        header = [re.sub(r'^[\'"]|[\'"]$', '', field.strip()) for field in
                  header]

        # Iterate over the rest of the rows
        for row in reader:
            # Clean each field in the row to remove any extra quotes and spaces
            cleaned_row = [re.sub(r'^[\'"]|[\'"]$', '', field.strip()) for field
                           in row]

            # Create a dictionary for the current row using the header as keys
            row_dict = dict(zip(header, cleaned_row))

            try:
                domain = row_dict["\ufeffroot_domain"]
            except KeyError:
                print(json.dumps(row_dict, indent=4))
                continue
            country = row_dict.get("main_country", "")
            category = row_dict.get("s_category", "")
            name = row_dict["legal_name"]
            phone = row_dict["phone"]
            # address = row_dict["address"]
            region_name = row_dict["main_region"]

            elem = {
                "name": name,
                "phone": phone,
                "category": category,
                # "address": address
            }
            final[domain] = name
            # if domain in final:
            #     if country in final[domain]:
            #         if region_name in final[domain][country]:
            #             final[domain][country][region_name].append(elem)
            #         else:
            #             final[domain][country][region_name] = [elem]
            #     else:
            #         final[domain][country] = {region_name: [elem]}
            #
            # else:
            #     final[domain] = {
            #         country: {
            #             region_name: [elem]
            #         }
            #     }

    return final
