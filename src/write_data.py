import csv

def extract_data_to_csv(json_data, csv_filename):
    """
    Extracts data from a JSON structure and writes it to a CSV file.

    Args:
        json_data: The JSON data to process.
        csv_filename: The name of the output CSV file.
    """

    with open(csv_filename, 'w', newline='') as csvfile:
        fieldnames = ['OG Name', 'Country', 'Region',
                      'Name', 'Phone', 'Category', 'Address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Iterate through the JSON data and extract relevant information
        for og_name, element in json_data.items():
            for country_name,country_data in element.items():
                for region, province_data in country_data.items():
                    for business in province_data:
                        writer.writerow({
                            'OG Name': og_name,
                            'Country': country_name,
                            'Region': region,
                            'Name': business['name'],
                            'Phone': business['phone'],
                            'Category': business['category'],
                            'Address': business['address']
                        })



